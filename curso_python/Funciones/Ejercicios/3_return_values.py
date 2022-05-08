print('Return a simple values, line 2')
def get_formatted_name_1(first_name, last_name):
    full_name= f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name_1('Jimi', 'hendrix')
print(musician)

print('\nMaking an Argument Optional, line 9')
def get_formatted_name_2(first_name, middle_name, last_name):
    '''return a full nname, neatly formatted'''
    full_name = f'{first_name} {middle_name} {last_name}'
    return full_name.title()
musician = get_formatted_name_2('john' , 'lee', 'hooker')
print(musician)

print('\nReturning a Dictionary, line 17')
def build_person(first_name, last_name):
    '''Return a dictionary of information about a person'''
    person={'fist': first_name, 'last':last_name}
    return person
musician = build_person('jimi', 'hendrix')
print(type(musician), musician)

def build_person(first_name, last_name, age=None):
    '''Return a dictionary of information abput a person'''
    person = {'first': first_name, 'last':last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', age = 23)
print(type(musician),musician)
musician = build_person('lemmy', 'kilmister')
print(musician)


print('\nUsing a function with a while loop, linea 37')
def get_formatted_name_3(first_name, last_name):
    '''Return a full name, neatly formatted'''
    full_name = f'{first_name} {last_name}'
    return full_name
# This is an infinite loop!
while True:
    print('\nPlease tell me your name: ')
    f_name = input('First name: ')
    l_name = input('Last name: ')
    option= input('continue [y]es or [n]o: ')
    formatted_name = get_formatted_name_3(f_name, l_name)
    print(f'\nHello, {formatted_name}!')
    if option == 'n':
        break

def get_formatted_name(first_name, last_neme):
    '''Return a full name, neatly formatted'''
    full_name = f'{first_name} {last_neme}'
    return full_name
while True:
    print('\nPlease tell me your name: ')
    print("(enter 'q' at any time to quit )")
    f_name = input('First name: ')
    if f_name == 'q':
        break
    l_name = input('Last name: ')
    if l_name == 'q':
        build_person()
    formatted_name = get_formatted_name_3(f_name, l_name)
    print(f'\nHello, {formatted_name}!')


print('\nExercises, line 70 '.upper())
"""8-6. City Names: Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the
values that are returned.
"""
def city_coutry(name_city, name_country):
    full_name = f"'{name_city}, {name_country}'"
    return full_name
print(city_coutry('\nCDMX','Mexico'))
print(city_coutry('Los Angeles','USA'))
print(city_coutry('Moscu','Russia'))


"""
8-7. Album: Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.
Use None to add an optional parameter to make_album() that allows you to
store the number of songs on an album. If the calling line includes a value for
the number of songs, add that value to the album’s dictionary. Make at least
one new function call that includes the number of songs on an album.
"""
def make_album(artist_name, album_title, number_songs=None):
    full_album={'Name': artist_name, 'Title': album_title}
    if number_songs:
        full_album['Songs'] = number_songs
    return full_album
print(make_album('\nmotorhead','overkill','8'))
print(make_album('jimi hendrix','electric kadyl land'))
print(make_album('Kurt Cobain','never mind','8'))


"""8-8. User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop."""
def make_album(artist_name, album_title, number_songs=None):
    full_album={'Name': artist_name, 'Title': album_title}
    if number_songs:
        full_album['Songs'] = number_songs
    return full_album

while True:
    print("\n(enter 'q' at any time to quit )")
    a_name = input('Artist name: ')
    if a_name == 'q':
        break
    a_title = input('Album name: ')
    if a_title == 'q':
        break
    album = make_album(a_name, a_title)
    print(f'{album}')