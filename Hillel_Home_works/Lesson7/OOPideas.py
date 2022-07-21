from pprint import pprint

class Car:
    def __init__(self, model_name=None, production=None, company=None, engine=None, colour=None, price=None):
        self.new_car_data(model_name,production,company,engine,colour,price)

    def new_car_data(self, model_name_new, production_new, company_new, engine_new, colour_new, price_new):
        self.model_name = model_name_new
        self.production = production_new
        self.company = company_new
        self.engine = engine_new
        self.colour = colour_new
        self.price = price_new
    def model_names_show(self):
        print(f"Cars in list Model: {self.model_name}  company {self.company}")
    def full_info(self):
        print(f" Model: {self.model_name}, year product: {self.production}, Who made: {self.company}, "
              f"Engine liters: {self.engine}, Colour: {self.colour}, Price sell: {self.price}")



class Book:
    def __init__(self, book_name, production, publishing, genre, author, price):
        self.book_name = book_name
        self.publishing = production
        self.production = publishing
        self.genre = genre
        self.engine = author
        self.price = price


class Stadium:
    def __init__(self, stadium_name, date_open, country, city, place):
        self.stadium_name = stadium_name
        self.date_open = date_open
        self.country = country
        self.city = city
        self.place = place


if __name__ == "__main__":
    car_list = []
    book_list = []
    stad_list = []
    allowed_options = "[qadd/add/listdict/list/names/del/update/quit]"

    while True:
        function_todo = input(f'What gonna do? {allowed_options}')
        if function_todo == "qadd":
            new_qcar = Car(input(f'Model name :'))
            if new_qcar:
                car_list.append(new_qcar)
                print(f"New Model shorts {new_qcar.model_name}")
        elif function_todo == "add":
            new_car = Car(input(f"model_name: "),int(input(f"car_production: ")),input(f'company_name: '),
                          float(input(f"engine: ")),input(f"colour: "),int(input(f'price: ')))
            if new_car:
                print(f'New car data {new_car.model_name} is added')
                car_list.append(new_car)
        elif function_todo == "listdict":
            for cars in car_list:
                pprint(cars.__dict__)
        elif function_todo == "list":
            for cars in car_list:
                cars.full_info()
        elif function_todo == "names":
            for cars in car_list:
                cars.model_names_show()
        elif function_todo == "update":
           car_to_update = input()
           if car_to_update in car_list:
               print('yes')