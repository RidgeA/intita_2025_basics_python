max_age = 150

class User:
    def __init__(self, name, age=0):
        if age > max_age:
            raise ValueError(f"age must be below {max_age}")
        self.name = name

    def getName(self):
        return self.name

def greet(u):
    return f"Hello {u.getName()}"

if __name__ == "__main__":
    print("user module in user package")