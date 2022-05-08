"""
9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module.
Make a separate file that imports Restaurant. Make a Restaurant instance,
and call one of Restaurant’s methods to show that the import statement is working
properly.

"""

from Restaurant import Restaurant as R

los_cuñaos = R("los cuñaos", "mexicana")
los_cuñaos.describe_restaurant()

los_cuñaos.open_restaurant()


