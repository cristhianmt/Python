def describe_pet(animal_type, pet_name):
    print(f"\nI have  a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('dog','cairo')
describe_pet('fish', 'astro')

def describe_pet(animal_type, pet_name):
    print(f'\nI have a {animal_type}')
    print(f'My {animal_type}\' name is {pet_name}')
describe_pet(animal_type='dog', pet_name='argos')
describe_pet(pet_name='pupi', animal_type='fish')


print()
def describe_pet(pet_name, animal_type='dog'):
    print(f'\nI have a {animal_type}')
    print(f'My {animal_type}\' name is {pet_name}')
describe_pet('willie')

print()

##-----------------Exercises
'''3. T-Shirt: Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print
a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to
'''
def make_shirt(size, text):
    print(f'\nI goingo to make a {size} t-shirt')
    print(f'It will say {text}')
make_shirt('24', 'i love python')
make_shirt(size='24', text='i love python')


'''8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message.'''
def large_shirt(size='large', text='i love python'):
    print(f'\nI goingo to make a {size} t-shirt')
    print(f'It will say {text}')
large_shirt()
large_shirt('medium')
large_shirt('small', 'hacker')


'''
8-5. Cities: Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the
default country.
'''
def describe_city(name_city, country='Mexico'):
    print(f'\n{name_city} is in {country}')
describe_city('CDMX')
describe_city('Oaxaca')
describe_city('Califonia', 'USA')