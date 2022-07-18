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


def validate_dj_data(data):
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

def add_user(data):
    user_input = input("Enter new DJ's data: ")
    dj_data = user_input.split(",")
    validated_data = validate_dj_data(dj_data)

    if validated_data is not False:
        new_dj_data = {
            "name": validated_data[0],
            "age": validated_data[1],
            "equipment": validated_data[2],
            "discography": validated_data[3],
            "salary": validated_data[4],
            "genre": validated_data[5],
        }
        data.append(new_dj_data)
        return new_dj_data


def delete():
    print([i['name'] for i in djs], 'Please choose DJ name to remove :')
    name_to_del = input()
    for i in djs:
        if i["name"] == name_to_del:
            print(f'{i["name"]} was deleted')
            djs.remove(i)
def update():
    print([i['name'] for i in djs], 'Please choose DJ name to update :')
    name_to_update = input()
    for i in djs:
        if i["name"] == name_to_update:
            user_input = input("Enter new DJ's data: ").split(",")
            validated_data = validate_dj_data(user_input)
            if validated_data is not False:
               i["name"] = validated_data[0]
               i["age"] = validated_data[1]
               i["equipment"] = validated_data[2]
               i["discography"] = validated_data[3]
               i["salary"] = validated_data[4]
               i["genre"] = validated_data[5]


if __name__ == "__main__":
    djs = [tiesto, avicci, anna]
    allowed_options = "[add/list/names/delete/update/exit]"


    while True:
        desision = input(f"What should I do?{allowed_options}: ")
        if desision == "add":
            print("DJ input format: name,age,equipment,discography,salary,genre")
            new_dj = add_user(djs)
            if new_dj:
                print(f"DJ {new_dj['name']} is added!")
        elif desision == 'delete':
           delete()
        elif desision == 'update':
            update()
        elif desision == "list":
            pprint(djs)
        elif desision == "names":
            data = [dj["name"] for dj in djs]
            pprint(data)
        elif desision == "exit":
            print("Exiting...")
            break
        else:
            print(f"Please use allowed options! {allowed_options}")