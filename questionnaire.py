while True:
    answer = input("Why do you like programming? Please answer here: ")
    if answer == 'exit':
        exit()

    filename = 'questionnaire.txt'

    with open(filename, 'a') as file_object:
        file_object.write(f"{answer}\n")
