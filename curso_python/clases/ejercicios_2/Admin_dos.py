from User_dos  import User

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
                print(f"- {privileges}")
        else:
            print("Don't have privileges")


