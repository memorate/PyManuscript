def print_models(unprinted, completed):
    """
    Simulate printing each design, until there are none left.
    Move each design to completed_models after printing.
    """
    while unprinted:
        current_design = unprinted.pop()

        # Simulate creating a 3d print from the design.
        print("Printing model: " + current_design)
        completed.append(current_design)


def show_completed_models(completed):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)