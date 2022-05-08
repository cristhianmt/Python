#Creating the dog class
print('Creating the Dog Class, line 3')


#1
class Dog:  #Simpre las clase deben esta en mayusculas
    #2
    '''A simple attempt to model a dog'''

    #3
    def __init__(self, name, age): # __init__ Nombra a los objetos que se utilizaran
        '''Initialize name and age attributes.'''
     #4
        self.name = name        #self hace que las variables este disponible para todos los metodos
        self.age = age

    #5
    'Esto es un metodo'
    def sit(self):
        '''Simulate a dog sitting in response to a command'''
        print(f'{self.name} is now sitting')

    'Metodo'
    def roll_over(self):
        '''Simulate rolling over in response to command'''
        print(f'{self.name} rolled over')




print('\nMaking an Instance from a Class, line 24')#Hace una instancia desde una clase

my_dog = Dog('Willlie', 6)
print(f"My dog's name is { my_dog.name}")
print(f"My dog is  {my_dog.age} years old")



print('\nAccessing Attributes, line 30')

my_dog.name



print('\nCalling methods, line 39')

my_dog = Dog('Willlie', 6)
my_dog.sit()
my_dog.roll_over()


my_dog = Dog('Cairo', 12)
my_dog.sit()
my_dog.roll_over()


print('\nCreating multiples instances, line 57')

my_dog = Dog('Willie',6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()


print(f"\nMy dog's name is {your_dog.name}.")
print(f"My dog is {your_dog.age} years old.")
your_dog.sit()


print('\nCreating multiples instances, line 57')
