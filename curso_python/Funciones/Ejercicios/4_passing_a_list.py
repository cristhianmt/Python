print('\nPassing list, line 2'.upper())
def greet_user(names):
    '''Print a simple greeting to each user in the list'''
    for name in names:
        msg = f'Hello, {name.title()}'
        print(msg)
usernames = ['Hanna', 'ty', 'margot']
greet_user(usernames)



print('\nmodifying a list in a function, line 11'.upper())
# Start whit some designs that need to be printed.
unprited_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, untl none are left.
# Move each desing to completed_models after printing
while unprited_designs:
    current_design = unprited_designs.pop()
    print(f'Printing model: {current_design}')
    completed_models.append(current_design)
#Display all completed models
print('\nThe following models have been printed: ')
for completed_models in completed_models:
    print(completed_models)



print('\nmodifying a list in a function , line 29'.upper())
def print_model(unprited_designs, completed_models):
    '''Simulate printing each design, until none are left.
        Move each design to complete_models after printing'''
    while unprited_designs:
        current_design = unprited_designs.pop()
        print(f'Printing model: {current_design}')
        completed_models.append(current_design)

def show_competed_models(completed_models):
    '''Show all the models that were printed'''
    print('\nThe following models have been printed: ')
    for completed_models in completed_models:
        print(completed_models)

unprited_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_model(unprited_designs, completed_models)
show_competed_models(completed_models)



print('\nEvitar que una funcion modifique una lista , line 53'.upper())
def print_model(unprited_designs, copy_completed_models):
    '''Copy current models to another list(copy_completed_models)'''
    print('\n1. All elements have been copied')
    current_design = unprited_designs.copy()
    copy_completed_models.append(current_design)

def copy_models(copy_completed_models, copy_models_list):
    '''Eliminate models from copy list and add
        to (copy_models_list)'''
    while copy_completed_models:
        copy_designs = copy_completed_models.pop()
        print(f'\n2. Printing copy and eliminate models: {copy_designs}')
        copy_models_list.extend(copy_designs)

def show_completed_models(copy_models_list):
    '''Show all the models that were printed'''
    print('\n3. The following models have been copied and printed : ')
    for x in copy_models_list:
        print(x)

unprited_designs = ['phone case', 'robot pendant', 'dodecahedron']
copy_completed_models = []
copy_models_list = []
print_model(unprited_designs, copy_completed_models)
copy_models(copy_completed_models, copy_models_list)
show_completed_models(copy_models_list)
print(f'\nlista original: {unprited_designs}')
print(f'\nlista copiada pero elementos eliminados: {copy_completed_models}')
print(f'\nlista copiada: {copy_models_list}',)





print('\nExercises, line 85 '.upper())
'''
8-9. Messages: Make a list containing a series of short text messages. Pass the
list to a function called show_messages(), which prints each text message.
'''
print('\n8-9 Messages, line 94')
def show_messages(airplanes):
    for x in airplanes:
        print(x)

airplanes = ['Airbus', 'Boeing', 'Xspace', 'Bombardier Aerospace']
show_messages(airplanes)



'''
8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.
Write a function called send_messages() that prints each text message and
moves each message to a new list called sent_messages as it’s printed. After
calling the function, print both of your lists to make sure the messages were
moved correctly.
'''
print('\n8-10 Sending messages, line 111')
def send_messages(airplanes, new_list=None):
    new_list = []
    while airplanes:
        current_list = airplanes.pop()
        print(f'It´s printed: {current_list}')
        new_list.append(current_list)
    show_messages(new_list)

def show_messages(new_list):
    print('\nPrinted new list')
    for x in new_list:
        print(x,'This is a airplane company')
airplanes = ['Airbus', 'Boeing', 'Xspace', 'Bombardier Aerospace']
send_messages(airplanes)
print(f'\nOld list {airplanes}')




'''
8-11. Archived Messages: Start with your work from Exercise 8-10. Call the
function send_messages() with a copy of the list of messages. After calling the
function, print both of your lists to show that the original list has retained its
messages.'''

print('\n8-10 Sending messages, line 137')
def send_messages(airplanes, new_list):
    current_list = airplanes.copy()
    new_list.extend(current_list)
    for x in  new_list:
        print(f'It´s copy airplanes to new_list: {x}')

def show_messages(new_list):
    print('\nPrinted new list')
    for x in new_list:
        print(x,'This is a airplane company')
airplanes = ['Airbus', 'Boeing', 'Xspace', 'Bombardier Aerospace']
new_list = []

send_messages(airplanes, new_list)
show_messages(new_list)
print(f'\nOld list {airplanes}')
print(f'\nNew list {new_list}')