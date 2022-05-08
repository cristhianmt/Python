"""
9-5. Login Attempts: Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 162). Write a method called increment_login
_attempts() that increments the value of login_attempts by 1. Write another
method called reset_login_attempts() that resets the value of login_attempts
to 0.

Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.
"""

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

cris = User('Willi', 'Scott', 'wscott@gmail.com', 'Usa')
cris.describe_user()
cris.greet_user()

print("\nMaking 3 login attempts") # Haciendo tres intentos de login
cris.increment_login_attempts()
cris.increment_login_attempts()
cris.increment_login_attempts()
cris.increment_login_attempts()
print(f"Login attempts: {cris.login_attempts}")

print("\nResetting login attempts") # Haciendo tres intentos de login
cris.reset_login_attempts()
print(f"Login attempts: {cris.login_attempts}")