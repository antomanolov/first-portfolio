# arr = [int(x) for x in input().split()]
#
# for idx in range(len(arr)):
#     min_number = min(arr[idx:])
#     min_number_idx = arr.index(min_number, idx, len(arr))
#     if arr[idx] > min_number:
#         arr[idx], arr[min_number_idx] = arr[min_number_idx], arr[idx]


# ---------------------------------------------------------------------------

# Binary search

# ----------------------------------------------------------------------------

# some_array = [int(num) for num in input().split()]
# target = int(input())
#
#
# def binary_search(arr, searched_num):
#     left = 0
#     right = len(arr) - 1
#
#     while right >= left:
#         mid_idx = (right + left) // 2
#         mid_num = arr[mid_idx]
#
#         if mid_num == searched_num:
#             return mid_idx
#
#         if target < mid_num:
#             right = mid_idx - 1
#         else:
#             left = mid_idx + 1
#     return -1
#
#
# print(binary_search(some_array, target))


# Selection Sort


# def selection_sort(arr_to_sort, len_arr):
#     for ind in range(len_arr):
#         min_ind = ind
#         for i in range(ind + 1, len_arr):
#             if arr_to_sort[min_ind] > arr_to_sort[i]:
#                 min_ind = i
#         arr_to_sort[ind], arr_to_sort[min_ind] = arr_to_sort[min_ind], arr_to_sort[ind]
#     return arr_to_sort
#
#
# arr = [int(el) for el in input().split()]
# result = selection_sort(arr, len(arr))
# print(' '.join(str(el) for el in result))

# Bubble Sort

# def bubble_sort(arr_to_sort):
#     for i in range(len(arr_to_sort)):
#         is_sorted = True
#         next_step = 0
#         while next_step < len(arr_to_sort) - 1:
#             if arr_to_sort[next_step] > arr_to_sort[next_step + 1]:
#                 is_sorted = False
#                 arr_to_sort[next_step], arr_to_sort[next_step + 1] =
#                 arr_to_sort[next_step + 1], arr_to_sort[next_step]
#             next_step += 1
#         if is_sorted:
#             break
#     return arr_to_sort
#
#
# arr = [int(el) for el in input().split()]
# result = bubble_sort(arr)
# print(' '.join(str(el) for el in result))

# Insertion sort


# def insertion_sort(arr):
#     size = len(arr)
#     for ind in range(1, size):
#         move_ind = ind
#         while move_ind > 0 and arr[move_ind - 1] > arr[move_ind]:
#             arr[move_ind - 1], arr[move_ind] = arr[move_ind], arr[move_ind - 1]
#             move_ind -= 1
#     return arr
#
#
# arr = [int(el) for el in input().split()]
# result = insertion_sort(arr)
# print(' '.join(str(el) for el in result))


# QuickSort


# def quick_sort(start, end, arr):
#     if start >= end:
#         return
#
#     piv = start
#     left = start + 1
#     right = end
#
#     while right >= left:
#         if arr[left] > arr[piv] > arr[right]:
#             arr[left], arr[right] = arr[right], arr[left]
#
#         if arr[left] <= arr[piv]:
#             left += 1
#
#         if arr[right] >= arr[piv]:
#             right -= 1
#     arr[piv], arr[right] = arr[right], arr[piv]
#
#     quick_sort(start, right-1, arr)
#     quick_sort(right + 1, end, arr)
#
#
# arr = [int(el) for el in input().split()]
# quick_sort(0, len(arr) - 1, arr)
# print(' '.join(str(el) for el in arr))
