#Handling the FileNotFoundError Exception
#

print("\ntratar de abrir archivos que no existen, line 4")
filename ="alice_1.txt"
try:
    with open(filename, encoding='utf-8') as f:
        contets = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exits.")



#Analyzing Text
print("\nAnalyzing Text, line 15, 18")
title = "Alice in wonderland"
print(title.split())

filename= "alice.txt"
try:
    with open(filename, encoding='utf-8') as f:
        contets = f.read()
except FileNotFoundError:
    print(f"Sorry the file {filename} does not exist.")
else:
    #Count the approximate number of words inthe file
    words = contets.split()
    num_words = len(words)
    print(f"\nThe file{filename} has about {num_words} words.")