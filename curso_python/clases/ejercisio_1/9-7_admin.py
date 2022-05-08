"""
9-7. Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method.
"""

# Parent Class
class User:
    """Represent a simple user profile."""
    def __init__(self, first_name, last_name, email, country):
        """Initialize the user."""
        self.first = first_name
        self.last = last_name
        self.email = email
        self.country = country
        self.login_attempts = 0


    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"""The information about:
{self.first} {self.last} 
    Email: {self.email} 
    Country {self.country}""")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f'Hi {self.first}!, What is going on?')

    def increment_login_attempts(self):
        """Increment the value of login_attempts"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0"""
        self.login_attempts = 0

# Child Class
class Admin(User):
    """A user with administrative privileges."""
    def __init__(self, first_name, last_name, email,country ):
        """Initialize the admin."""
        super().__init__(first_name, last_name, email, country)
        self.privileges = []

    def show_privileges(self):
        """Display the privileges this administrator has."""
        print(f"This user {self.first}")
        for privileges in self.privileges:
            print(f"cas {privileges}")

root = Admin('Cristhian', 'Solo', 'wscott@gmail.com', 'Mexico')
root.privileges = ["add post", "delete post", "ban user"]
root.describe_user()
root.show_privileges()