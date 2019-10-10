import random


array = []
# Создание массива для задачи
for i in range(20):
    array.append(random.randint(-20, 20))
print(array)

def max_of_array(array):
    max = 0
    max_index = 0
    min = 0
    min_index = 0
    array_len = len(array)
    for i in range(0, array_len):
        if array[i] > 0:
            if array[i] > max:
                max = array[i]
                max_index = i
        elif array[i] < 0:
            if array[i] < min:
                min = array[i]
                min_index = i
    array[max_index], array[min_index] = 0, 0
    print(min, max)
    return [min, max]


def search_multi(array):
    min1, max1 = max_of_array(array)
    min2, max2 = max_of_array(array)
    if (min1 * min2) > (max1 * max2):
        print('Result is:')
        print(min1, min2)
    elif (min1 * min2) < (max1 * max2):
        print('Result is:')
        print(max1, max2)
    else:
        print('Result is:')
        print(min1, min2)
        print(max1, max2)

search_multi(array)





