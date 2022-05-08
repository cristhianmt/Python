"""always use try with except"""

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
