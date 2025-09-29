def func(arr):
    arr2 = arr[:]
    arr2[0].append(6)
    return arr

l = [list(range(1, 6))]

# print(l)
# print(func(l))
# print(l)

def func2(arr = None):
    if arr == None:
        arr = []
    arr.append(1)
    return arr

print(func2())
print(func2())
print(func2())

