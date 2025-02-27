from random import randint

def read_file(filename):
    lines = open(filename, encoding="utf8").read().splitlines()
    friend_list = [i.split() for i in lines]
    return friend_list

def extract_nickname_lists(friend_table):
    nickname_table = []
    for i in range(len(friend_table)):
        nickname_table.append(friend_table[i][3])
    return nickname_table

def extract_id_lists(friend_table):
    id_table = []
    for i in range(len(friend_table)):
        id_table.append(friend_table[i][0])
    return id_table

def read_nickname(member):
    list_nickname = []
    for i in range(member):
        list_nickname.append(input(f"Enter Nickname member{i + 1}: "))
    return list_nickname

def find_index(table, list_input):
    list_nickname_index = []
    for i in list_input:
        for j in table:
            if i.lower() == j.lower() and table.index(j) not in list_nickname_index:
                list_nickname_index.append(table.index(j))
                break
    return sorted(list_nickname_index)

def random_member(friend_table, list_nickname_index, member):
    random_time = int(input("How many people: "))
    random_member_index = []
    while random_time > 0:
        random_index = randint(0, member - 1)
        if random_index in random_member_index:
            pass
        else:
            random_member_index.append(random_index)
            random_time -= 1
    for i in range(len(random_member_index)):
        print(f"{i + 1}:", *friend_table[list_nickname_index[random_member_index[i]]])

def display_members(friend_table, list_nickname_index):
    for i in list_nickname_index:
        print(*friend_table[i])

def group_members(friend_table, nickname_table):
    member = int(input("How Many people in a Group: "))
    list_nickname = read_nickname(member)
    list_nickname_index = find_index(nickname_table, list_nickname)
    print("Group members")
    display_members(friend_table, list_nickname_index)
    if input("Random members? y/n: ").lower() == "y":
        random_member(friend_table, list_nickname_index, member)

def operate(friend_table, nickname_table, id_table):
    print("1. Group")
    print("2. Person")
    choice_1 = int(input("Enter choice: "))
    if choice_1 == 1:
        group_members(friend_table, nickname_table)
    elif choice_1 == 2:
        print("What do you have")
        print("1. Nickname")
        print("2. ID")
        choice_2 = int(input("Enter choice: "))
        if choice_2 == 1:
            nickname = [input("Enter Nickname: ")]
            display_members(friend_table, find_index(nickname_table, nickname))
        elif choice_2 == 2:
            id_student = [input("Enter ID: ")]
            display_members(friend_table, find_index(id_table, id_student))

def main():
    filename = "friend_list.txt"
    friend_table = read_file(filename)
    # print(friend_table)
    nickname_table = extract_nickname_lists(friend_table)
    id_table = extract_id_lists(friend_table)
    # print(nickname_table)
    # print(id_table)
    operate(friend_table, nickname_table, id_table)

if __name__ == '__main__':
    main()
