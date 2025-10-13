while True:
    try:
        # import sys
        # sys.exit(0)
        print(input("enter data:"))
    # except KeyboardInterrupt:
    #     print("Keyboard interrupt")
    # except SystemExit:
    #     print("System exit")
    except Exception:
        print("Something went wrong")


# BaseException
# ├── SystemExit
# ├── KeyboardInterrupt
# ├── GeneratorExit
# └── Exception
#     ├── StopIteration
#     ├── ArithmeticError
#     │   ├── ZeroDivisionError
#     │   └── ...
#     ├── OSError
#     │   ├── FileNotFoundError
#     │   └── ...
#     ├── ValueError
#     └── ...
