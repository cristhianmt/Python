"""
9-8. Privileges: Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges.
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
        # Initialize an empty set of privileges
        self.privileges = Privileges()


class Privileges:
    """A class to store an admin's privileges."""
    def __init__(self, privileges_list=[]):

        self.privileges_list = privileges_list


    def show_privileges(self):
        """Display the privileges this administrator has."""
        if self.privileges_list:
            for privileges in self.privileges_list:
                print(f"has {privileges}")
        else:
            print("Don't have privileges")


