import csv
import json
from pprint import pprint


class Dj:
    # This is a list of all djs
    djs = []
    djs_csv = []

    def __init__(self, name, age, equipment, discography, salary, genre, male):
        self.name = name
        self.age = age
        self.equipment = equipment
        self.discography = discography
        self.salary = salary
        self.genre = genre
        self.male = male

    @property
    def as_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "equipment": self.equipment,
            "discography": self.discography,
            "salary": self.salary,
            "genre": self.genre,
            "male": self.male,
        }

    @classmethod
    def add_csv(cls):
        print(
            "Update DJ's data by format: name,age,equipment,discography,salary,genre,male: "
        )
        user_input = input("Enter new DJ's data: ")
        dj_data = user_input.split(",")
        new_dj = cls.validate(dj_data)
        if new_dj is not None:
            Dj.djs_csv.append(new_dj.as_dict)
            return new_dj

    @classmethod
    def delete_csv(cls, name):
        for dj in cls.djs_csv:
            if dj["name"] == name:
                index = cls.djs_csv.index(dj)
                del cls.djs_csv[index]
                return True
        return False

    @classmethod
    def update_csv(cls, name):
        for dj in cls.djs_csv:
            if dj["name"] == name:
                print("Update DJ's data by format: name,age,equipment,discography,salary,genre,male: ")
                data_for_update = cls.validate(input("Enter new DJ's data: ").split(",")).as_dict
                dj["name"] = data_for_update["name"]
                dj["age"] = data_for_update["age"]
                dj["equipment"] = data_for_update["equipment"]
                dj["discography"] = data_for_update["discography"]
                dj["salary"] = data_for_update["salary"]
                dj["genre"] = data_for_update["genre"]
                dj["male"] = data_for_update["male"]
                return dj
    @classmethod
    def list_csv(cls):
        for dj in Dj.djs_csv:
            print(f'He is: {dj["name"]}, {dj["age"]} years old' if dj["male"] == "True"
                  else f'She is: {dj["name"]}, {dj["age"]} years old')
            # dj.show_short_details()

    @classmethod
    def names_csv(cls):
        print([dj["name"] for dj in Dj.djs_csv])

    @classmethod
    def validate(cls, data):
        if len(data) != 7:
            print("The number of arguments is not correct!")
            return None

        if data[0].isdigit():
            print(f"{data[0]} is digit")
            return None

        for element in [data[1], data[3], data[4]]:
            index = data.index(element)
            if element.isdigit():
                data[index] = int(element)
            else:
                print(f"{element} is not a digit")
                return None

        if not data[5].isalnum():
            print(f"{data[5]} is not an alnum")
            return None

        return cls(*data)

    @classmethod
    def read_from_file_csv(cls):
        FILENAME = "djs_old.csv"
        with open(FILENAME) as csv_file:
            reader = csv.DictReader(csv_file)
            djs_csv = [dj for dj in reader]
        return djs_csv

    @classmethod
    def update_file_csv(cls):
        FILENAME = "djs.csv"
        with open(FILENAME, "w", newline="") as file_csv:
            header = ["name", "age", "equipment", "discography", "salary", "genre", "male"]
            writer_dict = csv.DictWriter(file_csv, fieldnames=header)
            writer_dict.writeheader()
            writer_dict.writerows(Dj.djs_csv)


if __name__ == "__main__":
    # NOTE: Populate djs list
    extracted_djs_csv: list = Dj.read_from_file_csv()
    Dj.djs_csv = extracted_djs_csv

    allowed_options = "[add/list/names/delete/update/exit/]"

    while True:
        decision = input(f"What should I do?{allowed_options}: ")

        if decision == "list":
            Dj.list_csv()
        elif decision == "names":
            Dj.names_csv()
        elif decision == "add":
            print("DJ input format: name,age,equipment,discography,salary,genre,male")
            new_dj = Dj.add_csv()
            if new_dj:
                print(f"DJ {new_dj.name} is added!")
        elif decision == "update":
            print([dj["name"] for dj in Dj.djs_csv])
            name = input("Input DJ's name for update: ")
            updated_dj = Dj.update_csv(name)
            if updated_dj:
                print(f"DJ {name} updated to: {updated_dj['name']}")
        elif decision == "delete":
            delete_name = input("Input DJ's name for delete: ")
            deleted = Dj.delete_csv(delete_name)
            if deleted is True:
                print(f"DJ {delete_name} is deleted!")
        elif decision == "exit":
            print("♻︎ Updating the file...")
            Dj.update_file_csv()
            print("✅ File saved")
            print("Exiting...")
            break
        else:
            print(f"Please use allowed options! {allowed_options}")
