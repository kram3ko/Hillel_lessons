from pprint import pprint

anna_data = {
    "name": "Anna",
    "age": 24,
    "equipment": "Synth",
    "discography": 3,
    "salary": 3_000,
    "genre": "techno",
    "male": False
}


class Dj:

    dj_list = []

    def __init__(self, name, age, equipment, discography, salary, genre, male):
        self.name = name
        self.age = age
        self.equipment = equipment
        self.discography = discography
        self.salary = salary
        self.genre = genre
        self.male = male
        Dj.dj_list.append(self)
    def names(self):
        print(f'Dj names are {self.name}')
    def show_short_details(self):
        if self.male is True:
            message = "He is"
        else:
            message = "She is"
        print(f"{message} {self.name}, {self.age} years old")
    def delete(self):
        for dj in Dj.dj_list:
            if dj.name == self.name:
                 Dj.dj_list.remove(dj)

tiesto = Dj(
    name="Tiesto",
    age=55,
    equipment="Pioneer",
    discography=20,
    salary=30_000,
    genre="lite-house",
    male=True
)

avicci = Dj(
    name="Avicci",
    age=22,
    equipment="Pioneer",
    discography=40,
    salary=0,
    genre="adm",
    male=True
)

anna = Dj(**anna_data)


if __name__ == "__main__":
    # djs = [tiesto, avicci, anna]
    allowed_options = "[add/list/names/delete/update/quit]"
    trigger = True

    while trigger:
        start = input(f"What should I do?{allowed_options}: ")
        if start == "add":
            djs.append(Dj(input(f"Enter name DJ: "),int(input(f"age: ")),input(f'equipment: '),int(input(f"discography: ")),
                    int(input(f"salary: ")),input(f'genre:'),input(f'male:')))

        elif start == 'delete':
            Dj.delete(input('dsds:'))
        elif start == 'update':
            print(Dj.dj_list)
        elif start == "shortlist":
            for dj in djs:
                dj.show_short_details()
        elif start == "list":
            for dj in djs:
                pprint(dj.__dict__)

        elif start == "names":
            for dj in djs:
                dj.names()
        elif start == "quit":
            print("See you later...")
            trigger = False
        else:
            print(f"Please use allowed options! {allowed_options}")