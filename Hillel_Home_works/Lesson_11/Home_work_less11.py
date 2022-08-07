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
tiesto_data = {
    "name": "Tiesto",
    "age": 55,
    "equipment": "Pioneer",
    "discography": 20,
    "salary": 30_000,
    "genre": "lite-house",
    "male": True
}
avicci_data = {
    "name": "Avicci",
    "age": 22,
    "equipment": "Pioneer",
    "discography": 40,
    "salary": 0,
    "genre": "adm",
    "male": True
}


class Dj:
    # This is a list of all djs
    djs = []

    def __init__(self, name: str, age: int, equipment: str, discography: int, salary: float, genre: str, male: bool):
        self.validing(name, age, equipment, discography, salary, genre, male)
        self.name = name
        self.age = age
        self.equipment = equipment
        self.discography = discography
        self.salary = salary
        self.genre = genre
        self.male = male

    @staticmethod
    def validing(name, age, equipment, discography, salary, genre, male):
        assert isinstance(name, str), f'wrong type name: ({name}) --> might be str'
        assert isinstance(age, (int, float)), f'wrong type age: ({age}) int or float'
        assert isinstance(equipment, str), f'wrong type equipment: ({equipment}) string'
        assert isinstance(discography, int), f'wrong type discography: ({discography}) int'
        assert isinstance(salary, (int, float)), f'wrong type salary: ({salary}) int or float'
        assert isinstance(genre, str), f'wrong type genre: ({genre}) string'
        assert isinstance(male, bool), f'wrong type male: ({male}) bool'

    def upd(self,name_new, age_new, equipment_new, discography_new, salary_new, genre_new, male_new):
        self.validing(name_new, age_new, equipment_new, discography_new, salary_new, genre_new, male_new)
        self.name = name_new
        self.age = age_new
        self.equipment = equipment_new
        self.discography = discography_new
        self.salary = salary_new
        self.genre = genre_new
        self.male = male_new

    def show_full_details(self):
        if self.male is True:
            message = "He is"
        else:
            message = "She is"
        print(f"{message} {self.name}, {self.age}, {self.equipment}, {self.discography}, "
            f"{self.salary}, {self.genre}, {self.male} years old")

    @classmethod
    def add(cls):
        new_dj = Dj(input(f'Name: '), int(input(f'age: ')), input(f'equipment: '), int(input(f'discography: ')),
                        int(input(f'salary: ')), input(f'genre: '), bool(input(f'Male: True/False: ')))
        if new_dj:
            print(f'New Dj added {new_dj.name}')
            Dj.djs.append(new_dj)

    @classmethod
    def update(cls):
        for dj in Dj.djs:
            print(dj.name, end=' ')
        print()
        name_upd = input(f'Please choose DJ to update: ')
        for dj in Dj.djs:
            if dj.name == name_upd:
                dj.upd(input(f'Name: '), int(input(f'age: ')), input(f'equipment: '), int(input(f'discography: ')),
                        int(input(f'salary: ')), input(f'genre: '), bool(input(f'Male: True/False: ')))
        if name_upd:
            print(f'{name_upd} updated to {dj.name}')

    @classmethod
    def delete(cls, name):
        for dj in cls.djs:
            if dj.name == name:
                index = cls.djs.index(dj)
                del cls.djs[index]
                return True
        return False

    @classmethod
    def list(cls):
        for dj in Dj.djs:
            dj.show_full_details()

    @classmethod
    def names(cls):
        data = [dj.name for dj in Dj.djs]
        pprint(data)


if __name__ == "__main__":
    tiesto = Dj(**tiesto_data)
    avicci = Dj(**avicci_data)
    anna = Dj(**anna_data)

    # Populate djs list
    Dj.djs = [tiesto, avicci, anna]

    allowed_options = "[add/list/names/delete/update/exit/]"

    while True:
        desision = input(f"What should I do?{allowed_options}: ")

        if desision == "list":
            Dj.list()
        elif desision == "names":
            Dj.names()
        elif desision == "add":
           Dj.add()

        elif desision == "update":
            Dj.update()

        elif desision == "delete":
            delete_name = input("Input DJ's name for delete: ")
            deleted = Dj.delete(delete_name)
            if deleted is True:
                print(f'DJ {delete_name} is deleted!')
        elif desision == "exit":
            print("Exiting...")
            break
        else:
            print(f"Please use allowed options! {allowed_options}")
