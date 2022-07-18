from pprint import pprint

tiesto = {
    "name": "Tiesto",
    "age": 55,
    "equipment": "Pioneer",
    "discography": 20,
    "salary": 30_000,
    "genre": "lite-house",
}
avicci = {
    "name": "Avicci",
    "age": 22,
    "equipment": "Pioneer",
    "discography": 40,
    "salary": 0,
    "genre": "adm",
}
anna = {
    "name": "Anna",
    "age": 24,
    "equipment": "Synth",
    "discography": 3,
    "salary": 3_000,
    "genre": "techno",
}


def verify(data):
    if len(data) != 6:
        print("The number of arguments is not correct!")
        return False

    if data[0].isdigit():
        print(f"{data[0]} is digit")
        return False

    for element in [data[1], data[3], data[4]]:
        index = data.index(element)
        if element.isdigit():
            data[index] = int(element)
        else:
            print(f"{element} is not a digit")
            return False

    if not data[5].isalnum():
        print(f"{data[5]} is not an alnum")
        return False

    return data


def add_new_dj(data):
    user_input = input("Enter new DJ's data: ").split(',')
    verify_user = verify(user_input)

    if verify_user is not False:
        new_dj_data = {
            "name": verify_user[0],
            "age": verify_user[1],
            "equipment": verify_user[2],
            "discography": verify_user[3],
            "salary": verify_user[4],
            "genre": verify_user[5],
        }
        data.append(new_dj_data)
        return new_dj_data


def delete(data):
    print([i['name'] for i in djs], 'Please choose DJ name to remove :', end="")
    name_to_del = input()
    for i in djs:
        if i["name"] == name_to_del:
            print(f'{i["name"]} was deleted')
            djs.remove(i)
    return data

def update(data):
    print([i['name'] for i in djs], 'Please choose DJ name to update : ', end="")
    name_to_update = input()
    for i in djs:
        if i["name"] == name_to_update:
            user_input = input("Enter new DJ's data: ").split(',')
            verify_user = verify(user_input)
            if verify_user is not False:
                i["name"] = verify_user[0]
                i["age"] = verify_user[1]
                i["equipment"] = verify_user[2]
                i["discography"] = verify_user[3]
                i["salary"] = verify_user[4]
                i["genre"] = verify_user[5]
                print(f'{name_to_update} update to {i["name"]}')
    return data

if __name__ == "__main__":
    djs = [tiesto, avicci, anna]
    allowed_options = "[add/list/names/delete/update/quit]"
    trigger = True

    while trigger:
        start = input(f"What should I do?{allowed_options}: ")
        if start == "add":
            print("DJ input format: name,age,equipment,discography,salary,genre")
            new_dj = add_new_dj(djs)
            if new_dj:
                print(f"DJ {new_dj['name']} is added!")
        elif start == 'delete':
            delete(djs)
        elif start == 'update':
            update(djs)
        elif start == "list":
            pprint(djs)
        elif start == "names":
            dj_list = [i["name"] for i in djs]
            pprint(dj_list)
        elif start == "quit":
            print("See you later...")
            trigger = False
        else:
            print(f"Please use allowed options! {allowed_options}")
