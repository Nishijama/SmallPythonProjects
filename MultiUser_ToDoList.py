''' Multi-user to-do list '''
''' A simple study of handling json files and refactoring '''

import json

# check if json file containing all users exists, if not create one
def check_userbase():
    try:
        with open('users.json') as users_file:
            registered_users = json.load(users_file)

    except FileNotFoundError:
        with open('users.json', 'w') as users_file:
            registered_users = []
            json.dump(registered_users, users_file)


# get name from the user
def get_user_name():
    username = input("Username: ")
    return username


# if new user, add them to the userbase and create an empty json file for them
def create_user_data(username):
    user_data_file_name = username + "_data.json"
    user_data = []
    with open(user_data_file_name, 'w') as data_file:
        json.dump(user_data, data_file)
        return(user_data)


# if existing user, load their data from json file
def load_user_data(username):
    user_data_file_name = username + "_data.json"
    with open (user_data_file_name) as data_file:
        user_data = json.load(data_file)
        return(user_data)


# check if existing or new user
def load_user(username):
    with open('users.json') as users_file:
        registered_users = json.load(users_file)
        if username in registered_users:
            user_data = load_user_data(username)
            return user_data
        else:
            registered_users.append(username)
            with open('users.json', 'w') as users_file:
                json.dump(registered_users, users_file)
            user_data = create_user_data(username)
            return user_data


# display tasks to the user
def display_user_data(username, user_data):
    if user_data:
        print(f"Hello {username}! Here are your tasks: \n")
        for item in user_data:
            print(item)
    else:
        print(f"Hello {username}! You have no tasks yet")
    return 0


# allow user to add tasks to their list
def add_user_data(username, user_data):
    user_data_file_name = username + "_data.json"
    while True:
        new_item = input("Add task: ")
        print("'x' to cancel")
        if new_item == 'x':
            return False
        user_data.append(new_item)
        with open(user_data_file_name, 'w') as data_file:
            json.dump(user_data, data_file)

def main():
    registered_users = check_userbase()
    username = get_user_name()
    user_data = load_user(username)
    display_user_data(username, user_data)
    add_user_data(username, user_data)
    display_user_data(username, user_data)
    return 0

main()