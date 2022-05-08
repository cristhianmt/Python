"""
9-11. Imported Admin: Start with your work from Exercise 9-8 (page 173).
Store the classes User, Privileges, and Admin in one module. Create a separate
file, make an Admin instance, and call show_privileges() to show that
everything is working correctly.
"""

from User import Admin

root = Admin("Cristhian", "Solo", "wscott@gmail.com", "Mexico")
root.describe_user()

root_cris = ["add post", "delete post", "ban user"]
root.privileges.privileges_list = root_cris

print(f"\nPivileges from {root.first} has these privileges")
root.privileges.show_privileges()


