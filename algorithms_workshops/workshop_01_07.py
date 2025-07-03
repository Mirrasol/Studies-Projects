# 1. Дан массив чисел, от 0, где каждое число больше другого на 1.
# В нем одно число пропущено. Найти это число или вернуть следующее,
# если нет пропуска.
def find_missing_1(array):
    if not array:
        return 0
    
    max_element = max(array)
    set_array = set(array)
    
    for num in range(max_element + 1):
        if num not in set_array:
            return num

    return max_element + 1


def find_missing_2(array):
    n = len(array)
    expected_sum = n * (n + 1) // 2 # по формуле суммы последовательных чисел
    actual_sum = sum(array)
    return expected_sum - actual_sum


# 2. Дана строка из скобок. Надо проверить, правильно ли скобки расставлены: 
# количество открывающих равно количеству закрывающих, 
# сначала открываем - потом закрываем. 
# '(())' = True 
# ')()(' = False
def is_valid_brackets(brackets):
    counter = 0

    for bracket in brackets:
        if bracket == '(':
            counter += 1
        else:
            if counter == 0:
                return False
            counter -= 1

    return counter == 0             


# 3. Даны два несортированных массива (в них рандомные числа, могут быть дубликаты). 
# Найти их пересечение, вернуть в отсортированном виде.

# Если через Counter: TC = O(n), SC = O(n)
# Если через индексы-маркеры: ТС = O(nlogn), тк сортировка, SC = O(1)
def find_intersection(arr1, arr2):
    arr1.sort()
    arr2.sort()

    result = []

    index1 = 0
    index2 = 0

    while index1 < len(arr1) and index2 < len(arr2):
        if arr1[index1] == arr2[index2]:
            result.append(arr1[index1])
            index1 += 1
            index2 += 1
        elif arr1[index1] < arr2[index2]:
            index1 += 1
        else:
            index2 += 1
    
    return result


print(find_intersection([1, 2, 3, 3, 3, 4], [1, 3, 3, 4]))


# 4. Даны часы со стрелками, в формате 12 часов.
# Написать ф., которая принимает часы и минуты, 
# а возвращает острый угол между стрелками.