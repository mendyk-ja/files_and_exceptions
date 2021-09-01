import json


filename = 'number.json'
try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    print(f"File {filename} doesn't exist!")
else:
    print(f"Your  favourite n umber is {number}!")


