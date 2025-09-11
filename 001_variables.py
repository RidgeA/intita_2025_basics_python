message = "Hello world"
Message = "Hello World"
_message = "Hello_world"
message2 = "message 2"
a = 1
pi = 3.14
is_active = True

# Bad: 
# 1Message = "Hello world"
# if = "doesn't work"

print(message)
# name = input("Enter your name: ")
#print(name)

#Math 
print(10 + 10)
print(30 - 10)
print(20 * 1)
print(100/5)
print(101//5) # цілочислене ділення
print(11 % 2) # залишок від ділення
print(2 ** 10) # піднесення в ступінь

# Strings
print("Hello" + " " + "world")
print("Hello world " + str(2))
print("Hello world %d" % 2)
n = 3
print(f"Hello world {n}, {2 ** 8}")

name = "Anton"
print("my name is %s" % name)

#Comparison 
print(10 > 5) # True
print(10 != 42) # True
print(10 < 20) # True
print(not (10 != 5)) # False
print(10 >= 10) # True
print(10 > 10) # False
print(10 == 10) # True

a = 10
print(a == 20) 

#Logical
b = 42
print((b % 2 == 0) and (b > 10)) # парне число та більше 10 - True
print((b % 2 == 0) or (b > 100)) # парне число або більше 100 - True


print(10 + 10 * 5)
print((10 + 10) * 5)

c = b * 10 - 2 ** 4;
print(c)

d = 10
d += 1 # d = d + 1
print(d)