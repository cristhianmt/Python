class Employees():
    def __init__(self, first, last, salary):
        self.first = first.title()
        self.last = last.title()
        self.salary = salary

    def give_raise(self, amount=5000):
        """Give the employes a raise"""
        self.salary += amount
        print(f"{self.first} {self.last} {self.salary}")

