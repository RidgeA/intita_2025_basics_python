class Person:
    def __init__(self, name):
        self.name = name

    def info(self):
        return f"User name: {self.name}"

class AdminUser(Person):
    def __init__(self, name):
        super().__init__(name)
        self.role = "admin"

    def info(self):
        person_info = super().info()
        return f"{person_info}. Role: {self.role}"
    
class Moderator(Person):
    def __init__(self, name):
        super().__init__(name)
        self.role = "moderator"

    def info(self):
        person_info = super().info()
        return f"{person_info}. Role: {self.role}"
    
user = AdminUser("John");
mod = Moderator("Jane")

print(user.info())
print(mod.info())
