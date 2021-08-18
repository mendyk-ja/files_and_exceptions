
while True:
    try:
        first_number = int(input("Please, insert first_number: "))
    except ValueError:
        print("Inserted data is  not a number! please, try again.")
    else:
        while True:
            try:
                second_number = int(input("Please, insert second number: "))
            except ValueError:
                print("Inserted data is  not a number! please, try again.")
            else:
                break
        break
