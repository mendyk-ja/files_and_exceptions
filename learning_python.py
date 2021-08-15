# read input file
file_object = open("learning_python.txt", "rt")
# read file contents to string
data = file_object.read()
# replace all occurrences of the required string
data = data.replace('C', 'Python')
# close the input file
file_object.close()
# open the input file in write mode
file_object = open("learning_python.txt", "wt")
# overwrite the input file with the resulting data
file_object.write(data)
# close the file
print(data)
file_object.close()

file_name = 'learning_python.txt'

with open(file_name) as file_object:
    contents = file_object.read()
print(contents.rstrip())

with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())

with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
