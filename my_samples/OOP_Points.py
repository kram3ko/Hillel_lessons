from math import sqrt
class Point:
    points_sklad = []

    def __init__(self, name, cursor_x=0, cursor_y=0):

        self.name = name
        self.move_to(cursor_x,cursor_y)

        Point.points_sklad.append(self)
    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def start_pos(self):
        self.move_to(0,0)
    def print_point(self):
        print(f'Point with coord: ({self.x},{self.y})')
    def distace(self, another_point):
        if not isinstance(another_point, Point):
            raise ValueError(f'Not another point')
        return sqrt((self.x - another_point.x)**2) + ((self.y - another_point.y)**2)

if __name__ == "__main__":
    trigger = True
    allowed_options = "[add/list/names/delete/update/quit]"

    while trigger:
        descision = input(f"please choose opt: {allowed_options}")
        if descision == "add":
            add_point = Point(input('point name'),int(input('cord_x')),int(input('cord_y')))
        if descision == "list":
            for point in Point.points_sklad:
                print(f'Точки с именем:{point.name} and cord({point.x} {point.y})')
