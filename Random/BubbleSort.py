def BubbleSort(array):

    size = len(array)

    for j in range(size-1):
        swapped = False        # if the element is element is already sorted while complting a loop this wont become true in that case we know it is not sorted so we will break out of the loop
        for i in range(size-1-j):
            if array[i] > array[i+1]:
                tmp = array[i]
                array[i] = array[i+1]
                array[i+1] = tmp
                swapped = True

        if not swapped:
            break


array = [1, 2, 3]
BubbleSort(array)
print(array)
