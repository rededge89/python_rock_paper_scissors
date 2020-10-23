import random


def generate_computer():
    computer_selection = random.choice(["rock", "paper", "scissors"])
    return computer_selection


def print_who_won(users_play, computer):
    win_conditions = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
    if users_play == '!rating':
        return 'rating'
    try:
        if users_play == computer:
            print(f"There is a draw ({users_play})")
            return "draw"
        elif win_conditions[users_play] == computer:
            print(f"Well done. The computer chose {computer} and failed")
            return "win"
        else:
            print(f"Sorry, but the computer chose {computer}")
            return "lose"
    except:
        print("Invalid input")


def find_player_info(name):
    user_list = open('rating.txt', mode='r')
    for user in user_list:
        name_and_score = user.split()
        if name_and_score[0] == name:
            user_list.close()
            return name_and_score
    user_list.close()
    name_and_score[0] = name
    name_and_score[1] = 0
    return name_and_score


def calculate_score(outcome):
    if outcome == 'win':
        pass
    elif outcome == 'draw':
        pass
    else:
        pass


def determine_what_weapons_win(weapons, user_choice):
    weapon_list = weapons.split(',')
    base_list = weapon_list[:]
    total_weapon_count = len(base_list)
    where_to_split_list = base_list.index(user_choice)
    list1 = base_list[:where_to_split_list]
    list2 = base_list[where_to_split_list:]
    list2.extend(list1)
    return list2[int(total_weapon_count / 2) + 1:]


def computer_selection_custom_game(weapons):
    weapon_list = weapons.split(',')
    index = random.randint(0, len(weapon_list)-1)
    return weapon_list[index]


username = input('Enter your name: ')
print('Hello, ' + username)
user_info = find_player_info(username)
weapon = input()
print("Okay, let's start")
if weapon == "":
    while (users_selection := input()) != "!exit":
        computer_selection = generate_computer()
        outcome = print_who_won(users_selection, computer_selection)
        if outcome == 'win':
            user_info[1] = int(user_info[1]) + 100
        elif outcome == 'draw':
            user_info[1] = int(user_info[1]) + 50
        elif outcome == 'rating':
            print(user_info[1])
    print("bye!")
else:
    while (users_selection := input()) != "!exit":
        if users_selection == '!rating':
            print(user_info[1])
        else:
            win_list = determine_what_weapons_win(weapon, users_selection)
            computer_selection = computer_selection_custom_game(weapon)
            if computer_selection in win_list:
                print(f"Well done. The computer chose {computer_selection} and failed")
                user_info[1] = int(user_info[1]) + 100
            elif computer_selection == users_selection:
                print(f"There is a draw ({computer_selection})")
                user_info[1] = int(user_info[1]) + 50
            else:
                print(f"Sorry, but the computer chose {computer_selection}")
