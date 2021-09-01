import json

number = input("What is your favourite number? ")
filename = 'number.json'
with open(filename, 'w') as f:
    json.dump(number, f)
