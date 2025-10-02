class Person:
    def __init__(self, name):
        self.name = name
        self.roles = []

    def info(self):
        return f"User name: {self.name}, roles {[r.info() for r in self.roles]}"
    
    def add_role(self, role):
        self.roles.append(role)

class Admin:
    def __init__(self):
        self.role = "admin"

    def info(self):
        return self.role
    
class Moderator:
    def __init__(self):
        self.role = "moderator"

    def info(self):
        return self.role
    
user = Person("John")
user.add_role(Admin())
user.add_role(Moderator())

print(user.info())
