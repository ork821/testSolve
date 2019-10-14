import random

array = []
# Создание массива для задачи
for i in range(20):
    array.append(random.randint(-20, 20))
print(array)

def search_max_multi(array):
    array.sort() # outputs sorted array
    max1, max2 = array[-1], array[-2] # last numbers is maximum
    min1, min2 = array[0], array[1] # first numbers is minimum

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

search_max_multi(array)
