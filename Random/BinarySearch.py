def linearSearch(list, number_to_find):
    for index, element in enumerate(list):
        if element == number_to_find:
            return index
    return -1


def BinarySearch(Array, number_to_find):

    left_pointer = 0
    right_pointer = len(Array) - 1
    mid = 0

    while left_pointer <= right_pointer:
        mid = (left_pointer + right_pointer) // 2
        mid_number = Array[mid]

        if mid_number == number_to_find:
            return mid

        if number_to_find > mid_number:
            left_pointer = mid + 1

        if number_to_find < mid_number:
            right_pointer = mid - 1

    return -1


Array = [19, 1, 4, 59, 9, 28, 52, 22, 6, 8]
print(BinarySearch(Array, 9))
