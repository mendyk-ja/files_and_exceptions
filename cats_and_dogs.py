
filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    try:
        with open(filename) as file_object:
            lines = file_object.readlines()
    except FileNotFoundError:
        print(f"Sorry, but {filename} file doesn't exist in this directory.")
    else:
        for line in lines:
            print(line.rstrip())

