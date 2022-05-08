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
    Country: {self.country}""")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f'Hi {self.first}!, What is going on?')

    def increment_login_attempts(self):
        """Increment the value of login_attempts"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0"""
        self.login_attempts = 0
