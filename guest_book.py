while True:
    name = input('Please, insert here your name: ')
    if name == 'exit':
        exit()
    print(f"Welcome, {name}. Happy to see you!")

    filename = 'guest_book.txt'

    with open(filename, 'a') as file_object:
        file_object.write(f"{name}\n")
