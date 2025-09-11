
# while <condition>:
#    <commands>

num = 0
while num < 10 :
    num += 1
    if num % 2 == 0:
        continue

    print(num)
    if num >= 10:
        break
else:
    print("The while loop is over")

print("While loop End")

print("=================For loop==================")

for i in range(10):
    print(i)

for i in range(5, 10):
    print(i)

for i in range(0, 100, 10):
    print(i)

for i in range(10, 0, -1):
    print(i)