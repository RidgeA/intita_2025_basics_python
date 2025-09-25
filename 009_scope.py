
x = "global"

def outer():
    x = "enclosing"
    
    def inner():
        x = "local"
        print(x)
    
    inner()
    print(x) # enclosing

outer()  # local
print(x)  # global

print("=======================")
a = 10
def change_a():
    global a
    a = 5

change_a()
print(a)


print("=======================")
def parent():
    b = 100

    def child():
        nonlocal b;
        b = 50
    child()
    print(b)

parent() 
# print(b)

def create_counter():
    cnt = 0

    def increment():
        nonlocal cnt
        cnt += 1
        print(cnt)

    return increment

counter = create_counter()

counter()
counter()

counter()
counter()
counter()
counter()
counter()
counter()
counter()
counter()