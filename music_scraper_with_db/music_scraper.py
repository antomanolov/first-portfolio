from datetime import datetime
import requests_html
import parsedatetime
import sqlite3

session = requests_html.HTMLSession()

# this function is made to cast ints and floats to their true values
def try_cast(value, cast):
    try:
        return cast(value)
    except ValueError:
        return 0

# the class in which will be saved the scrapped info for every album which is scrapped
class Album:
    def __init__(self, in_html):
        self.title = in_html.find('.page_charts_section_charts_item_title', first=True).text
        self.artist = in_html.find('.page_charts_section_charts_item_credited_links_primary', 
                                   first=True).text
        date_str = in_html.find('.page_charts_section_charts_item_date', first=True).text
        parsed_date, _ = parsedatetime.Calendar().parse(date_str)
        self.date = datetime(*parsed_date[:6])
        
        try:
            self.genres = in_html.find('.page_charts_section_charts_item_genres_primary', first=True).find('.comma_separated')
            self.genres = [el.text for el in self.genres]
        except Exception:
            self.genres = []
        
        try:
            self.sub_genres = in_html.find('.page_charts_section_charts_item_genres_secondary', first=True).find(".comma_separated")
            self.sub_genres = [el.text for el in self.sub_genres]
        except Exception:
            self.sub_genres = []
        
        try:
            self.genre_tags = in_html.find('.page_charts_section_charts_item_genre_descriptors', first=True).find(".comma_separated")
            self.genre_tags = [el.text for el in self.descriptors]
        except Exception:
            self.genre_tags = []
        
        self.average = try_cast(in_html.find('.page_charts_section_charts_item_details_average_num',first=True).text, float)
        self.voters = try_cast(in_html.find('.page_charts_section_charts_item_details_ratings',first=True).find('.full',first=True).text, int)
        self.reviews = try_cast(in_html.find('.page_charts_section_charts_item_details_reviews',first=True).find('.full',first=True).text, int)
    
    def __str__(self) -> str:
        return f'{self.title} by {self.artist} on {self.date}({self.average} from {self.voters} voters)'

all_scrapped = []
genre_counter = {}

# the loop wich is ressponsible for scrapping the info from the web page
for page in range(1, 2):
    response = session.get(f'https://rateyourmusic.com/charts/esoteric/album/2022/{page}')
    elements = response.html.find('.page_section_charts_item_wrapper')
    all_scrapped.extend(Album(el) for el in elements)

# making DB to save the scraped info
connect_db = sqlite3.connect('music_scraper.db')
connect_db.execute('''CREATE TABLE IF NOT EXISTS albums (
                      albumTitle TEXT PRIMARY KEY,
                      albumArtist TEXT,
                      albumDate  TEXT,
                      albumVoters INTEGER 
                    )''')

connect_db.commit()
# this loop is responsible for printing the results in human readable way 
# + making counter for every genre in scrapping info
for el in all_scrapped:
    #actualy make cols for the table with every album
    connect_db.execute('''INSERT OR IGNORE INTO albums VALUES(?,?,?,?)''',
                       (el.title, el.artist, el.date, el.voters))
    for genre in el.genres:
        if genre not in genre_counter:
            genre_counter[genre] = 0
        genre_counter[genre] += 1
# commit the changes to the DB
connect_db.commit()
# sorting the dictionary reversed so that the genre with most albums to be on first place
sorted_genre_dict = sorted(genre_counter, key=genre_counter.get, reverse=True)

# loop to print the Genre: count of genre in albums to test if it works
# for genre in sorted_genre_dict[:10]:
#     print(f'{genre}: {genre_counter[genre]}')

