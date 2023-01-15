
#créer une liste en choisissant des éléments d'index impair dans la première liste et des éléments d'index pair dans la seconde
#Etant doné deux listes , l1 et l2, écrivez un programme pour créer une troisième liste l3 en choisissant un élément d'indice 

l1 = [3,6,9,12,15,18,21]
l2 = [4,8,12,16,20,24,28]
l3 = []

for i in range(0, len(l1), 2):
    l3.append(l1[i])
    l3.append(l2[i])

print(l3)    


#exercice 2

lst = [11, 45, 8, 23, 14, 12, 78, 45, 89]

# Determine the length of the list
length = len(lst)

# Divide the length of the list by 3 to get the size of each part
size = length // 3

# Initialize empty lists for each part
part1 = []
part2 = []
part3 = []

# Iterate over the list and append the elements to part1
for i in range(size):
  part1.append(lst[i])

# Reverse the list part1
part1.reverse()

# Iterate over the list and append the elements to part2
for i in range(size, size * 2):
  part2.append(lst[i])

# Reverse the list part2
part2.reverse()

# Iterate over the list and append the elements to part3
for i in range(size * 2, length):
  part3.append(lst[i])

# Reverse the list part3
part3.reverse()

# Print the resulting lists
print(part1)
print(part2)
print(part3)

#exercice 3

lst = [11, 45, 8, 11, 23, 45, 23, 45, 89]

# Initialize an empty dictionary
counts = {}

# Iterate over the list
for element in lst:
  # Check if the element exists in the dictionary as a key
  if element in counts:
    # If it does, increment the value for that key by 1
    counts[element] += 1
  else:
    # If it does not, add it to the dictionary with a value of 1
    counts[element] = 1

# Print the resulting dictionary
print(counts)

#exercice 4
set1 = {23, 42, 65, 57, 78, 83, 29}
set2 = {57, 83, 29, 67, 73, 43, 48}

# Find the intersection of the two sets
intersection = set1.intersection(set2)

# Remove the intersection from set1
set1.difference_update(intersection)

# Print the resulting sets
print(set1)
print(set2)

#exercice 5

lst = [47, 64, 69, 37, 76, 83, 95, 97]
dct = {'Yassine':47, 'Imane':69, 'Mohammed':76, 'Abir':97}

# Iterate over the list
for element in lst:
  # Check if the element exists in the dictionary as a value for any key
  if element not in dct.values():
    # If it does not, remove it from the list
    lst.remove(element)

# Print the resulting list
print(lst)







