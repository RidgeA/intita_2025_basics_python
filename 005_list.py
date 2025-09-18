empty_list = []
fibonacci_sequence = [1, 1, 2, 3, 5, 8, 13]
empty_list_with_constructor = list()

# <list> = [<expression> for <var> in <iterable> if <condition>]
list_comprehension = [2**x for x in range(0, 11) if x % 2 == 0]
# print(list_comprehension)

a = [10, 20, 30, 40, 50]
# print(a[:1], a[1:])
# print(100 not in a)


a = []
a.append(10)
a = a + [20, 30] # a.extend([20, 30])
a.insert(1, 15)
a[3] = 25
# a.clear()
a.remove(25)
del a[0]
# print(a.pop(1))

# print("=========")
# print(a)
# print("=========")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
# print(matrix[0][0])

matrix1 = matrix.copy()
matrix2 = list(matrix)
matrix3 = matrix[:]

matrix[0][0] = 0
# print(matrix)
# print(matrix1)
# print(matrix2)
# print(matrix3)

fruits = ['apple', 'banana', 'orange']
for fruitId in range(len(fruits)):
    print(fruits[fruitId])


