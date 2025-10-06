# if a > 5:
#     print(a)

# SyntaxError

# # ZeroDivisionError
# def divide(a, b):
#     return a / b

# def calculate(x, y):
#     result = divide(x, y)
#     return result

# print(calculate(10, 0))

# # TypeError
# a = 5 + "hello"

# # ValueError
# int("abc")

# # IndexError
# a = [1, 2, 3]
# print(a[10])

# # KeyError
# a = {"name":"John"}
# print(a["age"])

# # AttributeError
# a = []
# a.qwerty()

# try:
#     print("before")
#     result = 10/0
#     print("after")
# except ZeroDivisionError:
#     print("cannot divide by zero")

# print("done")

# def process_data(data, index):
#     try:
#         value = int(data[index])
#         result = 100 / value
#         return result
#     except IndexError:
#         print("Index out of range")
#     except ValueError:
#         print("Cannot convert to integer")
#     except ZeroDivisionError:
#         print("Cannot divide by zero")

# def process_data(data, index):
#     try:
#         value = int(data[index])
#         result = 100 / value
#         return result
#     except (IndexError, ValueError, ZeroDivisionError):
#         print("Index out of range")
#         print("Cannot convert to integer")
#         print("Cannot divide by zero")

# def process_data(data, index):
#     try:
#         value = int(data[index])
#         result = 100 / value
#         data.qwerty()
#         return result
#     except IndexError:
#         print("Index out of range")
#     except ValueError:
#         print("Cannot convert to integer")
#     except ZeroDivisionError:
#         print("Cannot divide by zero")
#     except Exception:
#         print("Something went wrong")

# process_data(["10", "0", "abc"], 0)
# process_data(["10", "0", "abc"], 5)
# process_data(["10", "0", "abc"], 2)

# try:
#     number = int("abc")
# except ValueError as e:
#     print(f"Error occurred: {e}")


# # ExceptionGroup
# def process_multiple_items(items):
#     errors = []
#     for item in items:
#         if item < 0:
#             errors.append(ValueError(f"Negative value: {item}"))
#         if item == 0:
#             errors.append(ZeroDivisionError(f"Zero value: {item}"))
#     if errors:
#         raise ExceptionGroup("Multiple errors occurred", errors)
# try:
#     process_multiple_items([1, -5, 0, 10, -3])
# except ExceptionGroup as eg:
#     print(f"Caught exception group with {len(eg.exceptions)} exceptions")
#     for exc in eg.exceptions:
#         print(f"  - {type(exc).__name__}: {exc}")

# try:
#     raise ExceptionGroup("group", [
#         ValueError("invalid value"),
#         TypeError("wrong type"),
#         ValueError("another invalid value")
#     ])
# except* ValueError as eg:
#     print(f"Caught {len(eg.exceptions)} ValueError(s)")
#     for e in eg.exceptions:
#         print(f"  {e}")
# except* TypeError as eg:
#     print(f"Caught {len(eg.exceptions)} TypeError(s)")
#     for e in eg.exceptions:
#         print(f"  {e}")

# try:
#     number = int(input("Enter a number: "))
# except ValueError:
#     print("Invalid number")
# else:
#     print(f"You entered: {number}")
# finally:
#     print("done")

# def calculate_percentage(part, total):
#     if total == 0:
#         raise ValueError("Total cannot be zero")
#     if part < 0 or total < 0:
#         raise ValueError("Values cannot be negative")
#     return (part / total) * 100

# try:
#     result = calculate_percentage(50, 0)
# except ValueError as e:
#     print(f"Error: {e}")

# def process_file(filename):
#     try:
#         file = open(filename, "r")
#         data = file.read()
#         file.close()
#         return data
#     except FileNotFoundError:
#         print(f"Logging: File {filename} not found")
#         raise
# try:
#     content = process_file("missing.txt")
# except FileNotFoundError:
#     print("Handling error at higher level")


# class NegativeNumberError(Exception):
#     def __init__(self):
#         self.code = 42
#         super().__init__(self, "Cannot calculate square root of negative number")

# def calculate_square_root(number):
#     if number < 0:
#         raise NegativeNumberError()
#     return number ** 0.5

# try:
#     result = calculate_square_root(-5)
# except NegativeNumberError as e:
#     print(f"Error: {e.code}")


# def parse_config(filename):
#     try:
#         with open(filename) as f:
#             import json
#             return json.load(f)
#     except FileNotFoundError as e:
#         raise ConfigError(f"Cannot load config from {filename}") from e
#     except json.JSONDecodeError as e:
#         raise ConfigError(f"Invalid JSON in {filename}") from e
# class ConfigError(Exception):
#     pass
# parse_config("missing.json")

def get_user_age(user_id):
    try:
        user_data = {"name":"John"}
        return user_data["age"]
    except KeyError:
        raise ValueError(f"User {user_id} has no age") from None

try:
    age = get_user_age(123)
except ValueError as e:
    print(e)