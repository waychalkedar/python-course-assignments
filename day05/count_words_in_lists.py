celestial_objects = [
    'Moon', 'Gas', 'Asteroid', 'Dwarf', 'Asteroid', 'Moon', 'Asteroid'
]

# The input is converted to a set to extract unique values
# The set is back-converted to a list to sort
working_list = list(set(celestial_objects)) 
working_list.sort()
count = []

for element in working_list:
    count.append(celestial_objects.count(element))

for i in range(len(working_list)):
    print("{:<10} {:>3}".format(list(working_list)[i], count[i]))