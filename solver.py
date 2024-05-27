cities = ['Dabokva', 'Karnaca', 'Dunwall', 'Fraeport', 'Baleton']
colors = ['blue', 'purple', 'red', 'green', 'white']
names = ['Finch', 'Winslow', 'Marcolla', 'Contee', 'Natsiou']
drinks = ['beer', 'rum', 'absinthe', 'wine', 'whiskey']
heirlooms = ['bird', 'snuff tin', 'medal', 'diamond', 'ring']


class Woman:
    def __init__(self, color, city, drink, heirloom, name):
        self.color = color
        self.city = city
        self.drink = drink
        self.heirloom = heirloom
        self.name = name


# def check_constraint_1(combination):
#     # The Baroness Finch wore a blue hat.
#     return any(woman.name == 'Finch' and woman.color == 'blue' for woman in combination)
# 
# def check_constraint_2(combination):
#     # Lady Winslow sat at the far left.
#     return combination[0].name == 'Winslow'

def check_constraint_3(combination):
    # Lady Winslow sat next to someone wearing red.
    # Since winslow is at position 0, only position 1 works.
    return combination[1].color == 'red'


def check_constraint_4(combination):
    # The lady wearing purple sat next to someone wearing green.
    purple_index = None
    green_index = None

    # Find the indices of the women wearing purple and green
    for i, woman in enumerate(combination):
        if woman.color == 'purple':
            purple_index = i
        elif woman.color == 'green':
            green_index = i

    # If either woman is not found, the constraint is not satisfied
    if purple_index is None or green_index is None:
        return False

    # Check if the women are sitting next to each other
    return abs(purple_index - green_index) == 1


# def check_constraint_5(combination):
#     # The lady in purple spilled her beer
#     return any(woman.color == 'purple' and woman.drink == 'beer' for woman in combination)
# 
def check_constraint_6(combination):
    # The woman who had the diamond heirloom sat next to someone from the city Dabokva.
    diamond_index = None
    dabokva_index = None

    for i, woman in enumerate(combination):
        if woman.heirloom == 'diamond':
            diamond_index = i
        elif woman.city == 'Dabokva':
            dabokva_index = i

    if diamond_index is None or dabokva_index is None:
        return False

    return abs(diamond_index - dabokva_index) == 1


#
# 
# def check_constraint_7(combination):
#     #The woman from Dabokva wore white.
#     return any(woman.city == 'Dabokva' and woman.color == 'white' for woman in combination)
# 
# def check_constraint_8(combination):
#     # Countess Contee has the bird heirloom.
#     return any(woman.name == 'Contee' and woman.heirloom == 'bird' for woman in combination)
# 
# def check_constraint_9(combination):
#     # The lady from the city of Karnaca has the snuff tin heirloom.
#     return any(woman.city == 'Karnaca' and woman.heirloom == 'snuff tin' for woman in combination)
# 
# 
def check_constraint_10(combination):
    # The lady from the city of Baleton sat next to a woman drinking absinthe.
    baleton_index = None
    absinthe_index = None

    for i, woman in enumerate(combination):
        if woman.city == 'Baleton':
            baleton_index = i
        elif woman.drink == 'absinthe':
            absinthe_index = i

    if absinthe_index is None or baleton_index is None:
        return False

    return abs(absinthe_index - baleton_index) == 1


#
# 
# def check_constraint_11(combination):
#     # The lady Doctor Marcolla drank whiskey.
#     return any(woman.name == 'Marcolla' and woman.drink == 'whiskey' for woman in combination)
# 
# def check_constraint_12(combination):
#     # The woman from the city Dunwall drank rum.
#     return any(woman.city == 'Dunwall' and woman.drink == 'rum' for woman in combination)
# 
# 
# def check_constraint_13(combination):
#     # The woman who sat in the center seat drank wine.
#     return combination[2].drink == 'wine'
# 
# 
# def check_constraint_14(combination):
#     # The lady Madam Natsiou originates from the city Fraeport.
#     return any(woman.city == 'Fraeport' and woman.name == 'Natsiou' for woman in combination)    


# combinations = generate_combinations()
# print("Checking", len(combinations), "different possible solutions")
# 25 Billion combinations - not feasible to search




from ortools.constraint_solver import pywrapcp

# Create the solver
solver = pywrapcp.Solver('Women Puzzle')

# Define variables for each attribute
color_vars = [solver.IntVar(0, len(colors) - 1, f'color_{i}') for i in range(5)]
city_vars = [solver.IntVar(0, len(cities) - 1, f'city_{i}') for i in range(5)]
drink_vars = [solver.IntVar(0, len(drinks) - 1, f'drink_{i}') for i in range(5)]
heirloom_vars = [solver.IntVar(0, len(heirlooms) - 1, f'heirloom_{i}') for i in range(5)]
name_vars = [solver.IntVar(0, len(names) - 1, f'name_{i}') for i in range(5)]

# Add constraints
# The Baroness Finch wore a blue hat.
finch_index = solver.IntVar(0, 4, 'finch_index')
solver.Add(solver.Element(name_vars, finch_index) == names.index('Finch'))
solver.Add(solver.Element(color_vars, finch_index) == colors.index('blue'))

# Lady Winslow sat at the far left.
solver.Add(name_vars[0] == names.index('Winslow'))

# The woman from Dabokva wore white.
dabokva_index = solver.IntVar(0, 4, 'dabokva_index')
solver.Add(solver.Element(city_vars, dabokva_index) == cities.index('Dabokva'))
solver.Add(solver.Element(color_vars, dabokva_index) == colors.index('white'))

# The lady wearing purple drank beer.
purple_index = solver.IntVar(0, 4, 'purple_index')
solver.Add(solver.Element(color_vars, purple_index) == colors.index('purple'))
solver.Add(solver.Element(drink_vars, purple_index) == drinks.index('beer'))

# The lady Doctor Marcolla drank whiskey.
marcolla_index = solver.IntVar(0, 4, 'marcolla_index')
solver.Add(solver.Element(name_vars, marcolla_index) == names.index('Marcolla'))
solver.Add(solver.Element(drink_vars, marcolla_index) == drinks.index('whiskey'))

# The woman from the city Dunwall drank rum.
dunwall_index = solver.IntVar(0, 4, 'dunwall_index')
solver.Add(solver.Element(city_vars, dunwall_index) == cities.index('Dunwall'))
solver.Add(solver.Element(drink_vars, dunwall_index) == drinks.index('rum'))

# The woman who sat in the center seat drank wine.
solver.Add(drink_vars[2] == drinks.index('wine'))

# The lady Madam Natsiou originates from the city Fraeport.
natsiou_index = solver.IntVar(0, 4, 'natsiou_index')
solver.Add(solver.Element(name_vars, natsiou_index) == names.index('Natsiou'))
solver.Add(solver.Element(city_vars, natsiou_index) == cities.index('Fraeport'))

# Countess Contee has the bird heirloom.
contee_index = solver.IntVar(0, 4, 'contee_index')
solver.Add(solver.Element(name_vars, contee_index) == names.index('Contee'))
solver.Add(solver.Element(heirloom_vars, contee_index) == heirlooms.index('bird'))

# The lady from the city of Karnaka has the snuff tin heirloom.
karnaca_index = solver.IntVar(0, 4, 'karnaca_index')
solver.Add(solver.Element(city_vars, karnaca_index) == cities.index('Karnaca'))
solver.Add(solver.Element(heirloom_vars, karnaca_index) == heirlooms.index('snuff tin'))

# # Lady Winslow sat next to someone wearing red.
# winslow_index = solver.IntVar(0, 4, 'winslow_index')
# red_index = solver.IntVar(0, 4, 'red_index')
# is_red_left = solver.IntVar(0, 1, 'is_red_left')
# is_red_right = solver.IntVar(0, 1, 'is_red_right')
# solver.Add(solver.Element(name_vars, winslow_index) == names.index('Winslow'))
# solver.Add(solver.Element(color_vars, red_index) == colors.index('red'))
# solver.Add(is_red_left + is_red_right == 1)
# solver.Max?

# # The lady wearing purple sat next to someone wearing green.
# purple_index = solver.IntVar(0, 4, 'purple_index')
# green_index = solver.IntVar(0, 4, 'green_index')
# solver.Add(solver.Element(color_vars, purple_index) == colors.index('purple'))
# solver.Add(solver.Element(color_vars, green_index) == colors.index('green'))
# solver.Add(solver.AbsEquality(purple_index - green_index, 1))
#
# # The woman who had the diamond heirloom sat next to someone from the city Dabokva.
# diamond_index = solver.IntVar(0, 4, 'diamond_index')
# dabokva_index = solver.IntVar(0, 4, 'dabokva_index')
# solver.Add(solver.Element(heirloom_vars, diamond_index) == heirlooms.index('diamond'))
# solver.Add(solver.Element(city_vars, dabokva_index) == cities.index('Dabokva'))
# solver.Add(solver.AbsEquality(diamond_index - dabokva_index, 1))
#
# # The lady from the city of Baleton sat next to a woman drinking absinthe.
# baleton_index = solver.IntVar(0, 4, 'baleton_index')
# absinthe_index = solver.IntVar(0, 4, 'absinthe_index')
# solver.Add(solver.Element(city_vars, baleton_index) == cities.index('Baleton'))
# solver.Add(solver.Element(drink_vars, absinthe_index) == drinks.index('absinthe'))
# solver.Add(solver.AbsEquality(baleton_index - absinthe_index, 1))


# All values must be unique for each attribute
solver.Add(solver.AllDifferent(color_vars))
solver.Add(solver.AllDifferent(city_vars))
solver.Add(solver.AllDifferent(drink_vars))
solver.Add(solver.AllDifferent(heirloom_vars))
solver.Add(solver.AllDifferent(name_vars))

# Search for a solution
db = solver.Phase(color_vars + city_vars + drink_vars + heirloom_vars + name_vars,
                  solver.CHOOSE_FIRST_UNBOUND,
                  solver.ASSIGN_MIN_VALUE)

solver.NewSearch(db)

combinations = []
while solver.NextSolution():
    combinations.append([
        Woman(
            colors[color_vars[i].Value()],
            cities[city_vars[i].Value()],
            drinks[drink_vars[i].Value()],
            heirlooms[heirloom_vars[i].Value()],
            names[name_vars[i].Value()]
        ) for i in range(5)])

# Brute force. Instead of trying to force the constraint solver to work with the neighbor
# rules, instead we'll use it to generate potential solutions (only 2016 of them)
# then we can filter this very small list using the constraint checking functions above.

for combination in combinations:
    if (check_constraint_3(combination) and check_constraint_4(combination) and check_constraint_6(
            combination) and check_constraint_10(combination)):
        print("Solution found:")
        for woman in combination:
            print(f"{woman.name} - {woman.color}, {woman.city}, {woman.drink}, {woman.heirloom}")
