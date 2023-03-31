from typing import Callable


class SortingAlgorithm:
    def __init__(self, name: str, function: Callable):
        self.name = name
        self.function = function


def bubble_sort(arr, visualize):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                visualize(arr)


def selection_sort(arr, visualize):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        visualize(arr)


def insertion_sort(arr, visualize):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            visualize(arr)
        arr[j + 1] = key


def merge_sort(arr, visualize):
    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def _merge_sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = _merge_sort(arr[:mid])
        right = _merge_sort(arr[mid:])
        merged = merge(left, right)
        visualize(merged)
        return merged

    return _merge_sort(arr)


def quick_sort(arr, visualize):
    def _quick_sort(arr, low, high):
        if low < high:
            pivot_idx = partition(arr, low, high)
            _quick_sort(arr, low, pivot_idx)
            _quick_sort(arr, pivot_idx + 1, high)

    def partition(arr, low, high):
        pivot = arr[low]
        left = low + 1
        right = high
        done = False
        while not done:
            while left <= right and arr[left] <= pivot:
                left = left + 1
            while arr[right] >= pivot and right >= left:
                right = right - 1
            if right < left:
                done = True
            else:
                arr[left], arr[right] = arr[right], arr[left]
                visualize(arr)
        arr[low], arr[right] = arr[right], arr[low]
        visualize(arr)
        return right

    _quick_sort(arr, 0, len(arr) - 1)
