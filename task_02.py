from random import randint

def merge_k_lists(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def main():
    k = int(input("Enter the number of arrays: "))
    lists = []
    for i in range(k):
        lists.append([randint(0, 1000) for _ in range(10)])
        print(f"Given array is {lists[i]}")
        lists[i] = sorted(lists[i])
        print(f"Sorted array is {lists[i]}")
    
    # Злиття всіх відсортованих масивів
    merged_list = lists[0]
    for i in range(1, k):
        merged_list = merge_k_lists(merged_list, lists[i])
    print(f"Merged list is {merged_list}")

if __name__ == "__main__":
    main()

