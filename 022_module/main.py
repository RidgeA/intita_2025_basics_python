import user;
import main2;
import math_utils;
import math

if __name__ == "__main__":
    u = user.User("John")
    print(user.greet(u))

    # user.max_age = 300
    # u = user.User("John", 160)
    # print(user.greet(u))

    main2.greetUser("Jane")

    print(math_utils.add(1, 2))
    print(math.pi)