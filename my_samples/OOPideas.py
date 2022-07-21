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
    def get_model(self):
        return self.model_name
    def change_colour(self):
        return self.colour
    def change_price(self):
        return self.price



tesla1 = Car(
    model_name="Tesla_p90",
    production=2001,
    company="Ilon_Mask",
    engine=0,
    colour="white",
    price=20_000,
)
bmw1 = Car(
    model_name="M5",
    production=2021,
    company="BMW",
    engine=4.5,
    colour="Red",
    price=90_000,
)
vw = Car(
    model_name="Polo_sedan",
    production=2022,
    company="Volkswagen",
    engine=1.5,
    colour="white",
    price=17_000,
)

class Book:
    def __init__(self, book_name, publication, publisher, genre, author, price):
        self.book_name = book_name
        self.publishing = publication
        self.production = publisher
        self.genre = genre
        self.engine = author
        self.price = price

harry = Book("Philosopher's Stone", 1997, "Bloomsbury", "fantasy","J.K.Rowling", 20000)
blade = Book("Blade",1973, "Marvel Comics", "comics","Erik Brus",1000)
toys = Book("Toys Story", 1995,"Buena Vista Pictures Distribution", "comedy", "Pixar Animation Studios",1000)


class Stadium:
    def __init__(self, stadium_name, date_open, country, city, place):
        self.stadium_name = stadium_name
        self.date_open = date_open
        self.country = country
        self.city = city
        self.place = place

stad1 = Stadium("Parken", 1992, "Denmark", "Copenhagen","Østerbro")
stad2 = Stadium("OSC Metalist", 1926, "Ukraine", "Kharkov", "gagarinplace")
stad3 = Stadium("New York City",2013,"Usa","New York","	The Bronx")


if __name__ == "__main__":
    car_list = [tesla1,bmw1,vw]
    book_list = [harry,blade,toys]
    stad_list = [stad1,stad2,stad3]
    allowed_options = "[qadd/add/listdict/list/names/delete/update/quit]"
    update_functions = "[colour/model/price]"

    while True:
        function_todo = input(f'What gonna do? {allowed_options}: ')
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
            update = input(f"choose what to do {update_functions}:")
            if update == "colour":
                vw.colour = input('Set colour: ')


        elif function_todo == "quit":
            print("see you later")
            break
