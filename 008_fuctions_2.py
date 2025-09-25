# def f():
#     return 1, 2, 3

# head, *tail = f()

# print(head, tail)


# import functools
# ls = sorted(l, key=functools.cmp_to_key(lambda x, y: y - x))
# print(ls)
# print(list(map(lambda x: x**2, ls)))

# def fib(n):
#     if n == 0 or n == 1:
#         return 1
#     return fib(n-1)+fib(n-2)

# print(fib(5))

# def rec_indef():
#     rec_indef()
# rec_indef()

filesystem = {
    "name": "root",
    "children": [
        {"name": "file1.txt", "children": []},
        {"name": "folder1", "children": [
            {"name": "file2.txt", "children": []},
            {"name": "file3.txt", "children": []}
        ]},
        {"name": "folder2", "children": [
            {"name": "folder3", "children": [
                {"name": "file4.txt", "children": []}
            ]}
        ]}
    ]
}
# root/file1.txt
# root/folder1/file2.txt
# root/folder1/file3.txt
# root/folder2/file3.txt
# root/folder2/file4.txt

# Recursive traversal
def traverse_recursive(node, indent=0):
    print("  " * indent + node["name"])  # print current node
    for child in node["children"]:       # traverse children recursively
        traverse_recursive(child, indent + 1)

print("Recursive traversal:")
traverse_recursive(filesystem)

# Iterative traversal
def traverse_iterative(root):
    stack = [(root, 0)]  # stack stores tuples of (node, indentation level)
    while stack:
        node, indent = stack.pop()
        print("  " * indent + node["name"])  # print current node
        # add children to stack in reverse order for correct traversal order
        for child in reversed(node["children"]):
            stack.append((child, indent + 1))

print("\nIterative traversal:")
traverse_iterative(filesystem)