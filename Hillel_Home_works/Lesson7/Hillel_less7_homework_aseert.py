from pprint import pprint


# Car Class things
class Car:
    # class atribute
    engine_type = 'Electic'
    engine_power = 600

    # Class exaple init atribute

    def __init__(self, model_name: str, production: int, company: str, engine: float, colour: str, price: float):
        self.assertdata(model_name, production, company, engine, colour, price)
        self.model_name = model_name
        self.production = production
        self.company = company
        self.engine = engine
        self.colour = colour
        self.price = price

    def assertdata(self,model_name, production, company,engine , colour , price):
        assert isinstance(model_name, str), f'Not str value: ({model_name}) should be string'
        assert isinstance(production, int), f'Not int value: ({production}) should be int'
        assert isinstance(company, str), f'Not str value: ({company}) please write str'
        assert isinstance(engine, (float, int)), f'Not float value: ({engine}) please write float or int'
        assert isinstance(colour, str), f'Not str value: ({colour}) should be string'
        assert isinstance(price, (float, int)), f'Not float value: ({price}) please write float or int'


    def new_car_data(self, model_name_new, production_new, company_new, engine_new, colour_new, price_new):
        self.assertdata(model_name_new, production_new, company_new, engine_new, colour_new, price_new)
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
              f"Engine liters: {self.engine}, Colour: {self.colour}, Price sell: {self.price} "
              f"extra enginepower {self.engine_power} and {self.engine_type}")

    def get_model(self):
        return self.model_name

    def change_colour(self, colour):
        self.colour = colour

    def change_engine_type_power(self, engine_type, engine_power):
        self.engine_type = engine_type
        self.engine_power = engine_power
        if not isinstance(engine_power, (float, int)):
            raise ValueError(f" engine power Not float type")
        return print(f'Engine type now {self.engine_type},Power now {self.engine_power}, was changed')


# Cars initing by __init__ auto ways

testcar = Car("Tiguan", 2017, "VW", 4.5, "red", 25_000)

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
        self.publication = publication
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def model_bookname_show(self):
        print(f"books in list names: {self.book_name}  company {self.author}")

    def full_info(self):
        print(f" Book_name: {self.book_name}, publication: {self.publication}, publisher: {self.publisher}, "
              f"genre: {self.genre}, author: {self.author}, Price sell: {self.price}")

    def get_book_autor(self):
        return self.author

    def change_price(self, price):
        self.price = price

    def change_name_genre(self, book_name, genre):
        self.book_name = book_name
        self.genre = genre
        if not isinstance(book_name, str) and isinstance(genre, str):
            raise ValueError(f" Bookname,genre not str type")
        return print(f'Book name changed to {self.book_name},genre changed to {self.genre}')


harry = Book("Philosopher's Stone", 1997, "Bloomsbury", "fantasy", "J.K.Rowling", 20000)
blade = Book("Blade", 1973, "Marvel Comics", "comics", "Erik Brus", 1000)
toys = Book("Toys Story", 1995, "Buena Vista Pictures Distribution", "comedy", "Pixar Animation Studios", 1000)


class Stadium:
    def __init__(self, stadium_name, date_open, country, city, place):
        self.stadium_name = stadium_name
        self.date_open = date_open
        self.country = country
        self.city = city
        self.place = place

    def stadium_name_show(self):
        print(f"Stadium name: {self.stadium_name}  country {self.country}")

    def full_info(self):
        print(f" Stadion name: {self.stadium_name}, dateopen: {self.date_open}, country: {self.country}, "
              f"city: {self.city}, place: {self.place}")


stad1 = Stadium("Parken", 1992, "Denmark", "Copenhagen", "Østerbro")
stad2 = Stadium("OSC Metalist", 1926, "Ukraine", "Kharkov", "gagarinplace")
stad3 = Stadium("New York City", 2013, "Usa", "New York", "	The Bronx")

setattr(Car, "Hilel_home_work", 'Practice')
setattr(Book, "Hilel_home_work", 'Practice')
setattr(Stadium, "Hilel_home_work", 'Practice')

# UNCOMENT THINGS LATER and try! Works only with class CARS!!!


# if __name__ == "__main__":
#
#     car_list = [tesla1, bmw1, vw]
#     book_list = [harry, blade, toys]
#     stad_list = [stad1, stad2, stad3]
#
#     allowed_options = "[add/listdict/list/names/update/quit]"
#     update_functions = "[colour/model/price]"
#
#     while True:
#         function_todo = input(f'What gonna do? {allowed_options}: ')
#         if function_todo == "qadd":
#             print('work maybe later')
#             # new_qcar = Car(input(f'Model name :'))
#             # if new_qcar:
#             #     car_list.append(new_qcar)
#             #     print(f"New Model shorts {new_qcar.model_name}")
#         elif function_todo == "add":
#             new_car = Car(input(f"model_name: "), int(input(f"car_production: ")), input(f'company_name: '),
#                           float(input(f"engine: ")), input(f"colour: "), int(input(f'price: ')))
#             if new_car:
#                 print(f'New car data {new_car.model_name} is added')
#                 car_list.append(new_car)
#         elif function_todo == "listdict":
#             for cars in car_list:
#                 pprint(cars.__dict__)
#         elif function_todo == "list":
#             for cars in car_list:
#                 cars.full_info()
#         elif function_todo == "names":
#             for cars in car_list:
#                 cars.model_names_show()
#         elif function_todo == "update":
#             update = input(f"choose what to do {update_functions}:")
#             if update == "colour":
#                 vw.colour = input('Set colour: ')
#
#
#         elif function_todo == "quit":
#             print("see you later")
#             break
