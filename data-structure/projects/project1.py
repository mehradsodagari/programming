import time
import random
from tabulate import tabulate


def decorator_calculate_running_time(func):
    def calculate_running_time(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        return end - start

    return calculate_running_time


@decorator_calculate_running_time
def bubble_sort(lst):
    length = len(lst)
    while length > 1:
        swapped = False
        i = 1
        while i < length:
            if lst[i] < lst[i - 1]:
                lst[i], lst[i - 1] = lst[i - 1], lst[i]
                swapped = True
            i += 1
        if not swapped:
            break
        length -= 1
    return lst


@decorator_calculate_running_time
def insertion_sort(lst):
    i = 1
    while i < len(lst):
        itemToInsert = lst[i]
        j = i - 1
        while j >= 0:
            if itemToInsert < lst[j]:
                lst[j + 1] = lst[j]
                j -= 1
            else:
                break
        lst[j + 1] = itemToInsert
        i += 1


@decorator_calculate_running_time
def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]

    def merge_sort_plain(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort_plain(arr[:mid])
        right = merge_sort_plain(arr[mid:])
        return merge(left, right)

    def merge(left, right):
        merged = []
        left_idx, right_idx = 0, 0

        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] <= right[right_idx]:
                merged.append(left[left_idx])
                left_idx += 1
            else:
                merged.append(right[right_idx])
                right_idx += 1

        merged.extend(left[left_idx:])
        merged.extend(right[right_idx:])
        return merged

    sorted_list = merge_sort_plain(lst)

    for i in range(len(lst)):
        lst[i] = sorted_list[i]
    return lst


@decorator_calculate_running_time
def quick_sort(lst):
    if len(lst) <= 1:
        return lst

    def quick_sort_plain(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort_plain(left) + middle + quick_sort_plain(right)

    sorted_list = quick_sort_plain(lst)
    for i in range(len(lst)):
        lst[i] = sorted_list[i]
    return lst


def run_experiment(n):
    original = random.sample(range(n * 10), n)

    best_case = sorted(original)
    average_case = original[:]
    worst_case = sorted(original, reverse=True)

    algorithms = {
        "Bubble Sort": bubble_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort,
    }

    results = []

    for name, algo in algorithms.items():
        t_best = algo(best_case.copy())
        t_avg = algo(average_case.copy())
        t_worst = algo(worst_case.copy())

        results.append([name, f"{t_best:.6f}", f"{t_avg:.6f}", f"{t_worst:.6f}"])

    return results


N = 100
table = run_experiment(N)

headers = ["Algorithm", "Best Case (s)", "Average Case (s)", "Worst Case (s)"]
print(tabulate(table, headers=headers, tablefmt="grid"))
