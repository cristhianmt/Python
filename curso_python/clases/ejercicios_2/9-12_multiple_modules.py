"""
9-12. Multiple Modules: Store the User class in one module, and store the
Privileges and Admin classes in a separate module. In a separate file, create
an Admin instance and call show_privileges() to show that everything is still
working correctly.
"""
from Admin_dos import Admin


kali = Admin('kali', 'linux', 'solo@kaili.offensive', 'california')
kali.describe_user()


kali_root = ['root', 'Admin']
kali.privileges.privileges_list = kali_root

print(f"The user {kali.first} has privileges: ")
kali.privileges.show_privileges()













