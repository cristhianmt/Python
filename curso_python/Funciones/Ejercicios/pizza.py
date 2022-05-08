def make_pizza(size, *toppings):
    print(f'\nMakeing a {size}-inch pizza with the following toppings: ')
    for x in toppings:
        print(f'- {x}')