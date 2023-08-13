from random import randint


def create_array(min, max, size):
    my_list = [randint(min, max) for _ in range(size)]
    return my_list


def heap_sort(array):
    for i in range(int(len(array)/2 - 1), -1, -1):
        heapify(array, len(array), i)

    for i in range(len(array) - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)

    return array


def heapify(my_array, size, root_index):
    largest = root_index
    left = 2 * root_index + 1
    right = 2 * root_index + 2

    if left < size and my_array[left] > my_array[largest]:
        largest = left

    if right < size and my_array[right] > my_array[largest]:
        largest = right

    if largest != root_index:
        temp = my_array[root_index]
        my_array[root_index] = my_array[largest]
        my_array[largest] = temp

        heapify(my_array, size, largest)






my_list_1 = create_array(1, 20, 20)
print(my_list_1)
print(heap_sort(my_list_1))



