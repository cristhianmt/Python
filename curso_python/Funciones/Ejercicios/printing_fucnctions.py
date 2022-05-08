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