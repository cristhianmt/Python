'''
9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user.
'''
print("\n9-3 User")

class User:
    """Represent a simple user profile."""
    def __init__(self, first_name, last_name, email, country):
        """Initialize the user."""
        self.first = first_name
        self.last = last_name
        self.email = email
        self.country = country

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"""The information about:
{self.first} {self.last} 
    Email: {self.email} 
    Country {self.country}""")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f'Hi {self.first}!, What is going on?')

cris = User('Willi', 'Scott', 'wscott@gmail.com', 'Usa')

print()
cris.describe_user()

print()
cris.greet_user()