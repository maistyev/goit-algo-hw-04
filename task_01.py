import timeit
from random import randint

def insertion_sort(lst):
    for i in range(1, len(lst)):  # Починаємо з другого елемента масиву
        key = lst[i]  # Зберігаємо поточний елемент як ключ
        j = i - 1  # Починаємо порівнювати з попереднім елементом
        while j >= 0 and key < lst[j]:  # Поки не дійшли до початку масиву і ключ менший за поточний елемент
            lst[j + 1] = lst[j]  # Зсуваємо поточний елемент вправо
            j -= 1  # Переміщаємось на одну позицію вліво
        lst[j + 1] = key  # Вставляємо ключ на правильну позицію
    return lst  # Повертаємо відсортований масив

# Функція сортування злиттям
def merge_sort(arr):
    # Якщо довжина масиву менше або дорівнює 1, повертаємо масив як є
    if len(arr) <= 1:
        return arr

    # Визначаємо середину масиву
    mid = len(arr) // 2
    # Ділимо масив на ліву і праву половини
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Рекурсивно сортуємо обидві половини
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Зливаємо дві відсортовані половини
    return merge(left_half, right_half)


# Функція злиття двох відсортованих масивів
def merge(left, right):
    result = []  # Результуючий масив
    left_index, right_index = 0, 0  # Індекси для лівого і правого масивів

    # Зливаємо масиви, порівнюючи елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Додаємо залишкові елементи з обох масивів
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result  # Повертаємо злитий масив


def main():
    arr_1 = [randint(0, 1000) for _ in range(100)]
    print(f"Given array is {arr_1}")
    arr_2 = arr_1.copy()
    arr_3 = arr_1.copy()

    insertion_sort_time = timeit.timeit(f"insertion_sort({arr_1})", setup="from __main__ import insertion_sort")
    merger_sort_time = timeit.timeit(f"merge_sort({arr_2})", setup="from __main__ import merge_sort, merge")
    timsort_sort_time = timeit.timeit(f"sorted({arr_3})")

    print(f"Insertion sort time: {insertion_sort_time}")
    print(f"Merge sort time: {merger_sort_time}")
    print(f"Timsort time: {timsort_sort_time}")
    print(f"timSort is {insertion_sort_time / timsort_sort_time} times faster than insertion sort")
    print(f"timSort is {merger_sort_time / timsort_sort_time} times faster than merge sort")
    
if __name__ == "__main__":
    main()