
filename = 'crime_and_punishment.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

searched_word_all = 0
for line in lines:
    searched_word_line = line.lower().count(' the ')
    searched_word_all += searched_word_line

print(searched_word_all)
