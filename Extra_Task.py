# Напишите функцию any_duplicates, которая принимает двумерный массив размера 3х3 (9 элементов). 
# Двумерный массив заполнен числами от 1 до 9.
# Функция должна вернуть False, если в массиве все числа от 1 до 9 встречаются ровно один раз. В противном случае True.
# [[1, 3, 2], [9, 7, 8], [4, 5, 6]] ➞ False
# [[8, 9, 2], [5, 6, 1], [3, 7, 4]] ➞ False
# [[1, 1, 3], [6, 5, 4], [8, 7, 9]] ➞ True # 1 дублируется
# [[1, 2, 3], [3, 4, 5], [9, 8, 7]] ➞ True # 3 дублируется

# Первый способ:
matrix = [[1, 3, 2], [9, 7, 8], [4, 5, 6]]
# def any_duplicates(matr):
#     perfect_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     array = []
#     for i in matr:
#         for j in i:
#             array.append(j)
#     sorted_array = sorted(array)
#     return sorted_array != perfect_array
# print(any_duplicates(matrix))

# Второй способ:
matrix1 = [item for j in matrix for item in j]
print(sorted(matrix) != [1, 2, 3, 4, 5, 6, 7, 8, 9])
