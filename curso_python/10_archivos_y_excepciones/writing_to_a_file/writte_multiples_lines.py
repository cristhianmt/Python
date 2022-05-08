#Writing Multiple Lines
file_name = "programming_multipleslines.txt"
with open(file_name, 'w') as file_objet:
    file_objet.write("I love programing.\n")
    file_objet.write("I love creating new games.")

with open(file_name) as file_objet:
    lines = file_objet.read()
print(lines)
