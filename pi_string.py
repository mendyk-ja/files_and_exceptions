filename = "pi_million_digits.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Give date  of your birth (ddmmyy format): ")
if birthday in pi_string:
    print("Date of your birth occur in the first million numbers of pi number.")
else:
    print("Date of your birth occur in the first million numbers of pi number.")

# Displaying only fist 52 number and 3 coma after that
# print(f"{pi_string[:52]}...")
# print(len(pi_string))
