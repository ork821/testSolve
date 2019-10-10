import random


array = []
# Создание массива для задачи
for i in range(20):
    array.append(random.randint(1, 20))
print(array)

def search_max_numbers(array):
    max_value = max(array)
    count_max = array.count(max_value)
    if (count_max != 1): #если в массиве есть второй такой элемент, то максимально произведение - его квадрат
        print(max_value**2)
        return [max_value, max_value]
    else:
        min_differ = max_value
        for i in array:
            differ = max_value - i
            if (differ == 0): #поймали то же самое число
                continue
            elif (differ < min_differ):
                min_differ = differ
        print(max_value * (max_value - min_differ)) #их произведение
        return ([max_value, max_value - min_differ])

print(search_max_numbers(array))




