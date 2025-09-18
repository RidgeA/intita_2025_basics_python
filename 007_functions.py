# def greet(name, greeting="hello"):
#     print(f"{greeting}, {name}")
# greet(greeting="hola", name="john doe")

# def greet(greeting, *args, **kvargs):
#    print(greeting)
#    print(args)
#    print(kvargs)
#    print(f"{greeting}, {kvargs.get("name", "nemo")}")

# greet("hola", "something", "else", name="john doe", )

def sumPositive(a, b):
    if a < 0 or b < 0:
        print("a or b is less than 0")
        return
    
    return a+b

s = sumPositive(0, 3)
print(s)

def sortTwo(a, b):
    if a > b:
        return a, b
    else:
        return b, a
    
sorted = sortTwo(5, 3)
print(sorted[0])
print(sorted[1])