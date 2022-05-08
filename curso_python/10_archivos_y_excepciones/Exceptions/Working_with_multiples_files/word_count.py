#working with multiples files
print("Working with multiples files, .line 3")
def count_words(filename):
    """count the approcimate number of words in a file"""
    try:
        with open(filename, encoding= "utf-8") as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry the file {filename} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"\nThe file has {num_words} words.")


filename = 'alice.txt'
count_words(filename)


#-------------------------------------------------------------------------------------------------------
print("\nOpen miultiples files, line 22")
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)

#------------------------------------------------------------------------------------------------------

print("\nFailing Silently with PASS errores silenciosos, line 29")
def count_words(filename):
    """count the approcimate number of words in a file"""
    try:
        with open(filename, encoding="utf-8") as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"\nThe file has {num_words} words.")


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
