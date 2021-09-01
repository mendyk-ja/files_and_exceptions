import json


def get_stored_username():
    """Extracting a name from file, if  it exists."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Asking user to give his/her name and then saving it to a file."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """Greeting user using his name."""
    username = get_stored_username()
    if username:
        print(f"Welcome again, {username}!")
    else:
        username = get_new_username()
        print(f"Your name i saved now and will be used later, {username}.")


greet_user()


