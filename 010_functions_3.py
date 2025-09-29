import time

def create_counter():
    cnt = 0

    def increment():
        nonlocal cnt
        cnt += 1
        print(cnt)
        return cnt

    return increment

counter = create_counter()

counter()

l = [1, 2, 3, 4, 5]

def pow(power):
    return lambda x: x**power

pow2 = pow(2)
pow3 = pow(3)
pow10 = pow(10)

print(pow3(2))

print(list(map(pow3, l))) 


def f(a, b):
    time.sleep(5)
    return a+b

def memorize(fn):

    cache = dict()

    def fn2(*args):

        result = cache.get(args, None)
        if result != None:
            print("result from cache")
            return result

        print("calculate result")
        result = fn(*args)

        cache[args] = result

        return result

    return fn2

print("++++++++++++++++++++++++++")
f_memorized = memorize(f)

print(f_memorized(2, 2))
print(f_memorized(2, 2))
print(f_memorized(2, 2))


print(f_memorized(2, 3))
print(f_memorized(2, 3))
print(f_memorized(2, 3))