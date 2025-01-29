class Car:
    cars = []
    def __init__(self,x,y):
        self.x_coord = x
        self.y_coord = y
    def __eq__(self, value):
        return (self.x_coord == value.x_coord) and (self.y_coord == value.y_coord)
    def __repr__(self):
        return f"({self.x_coord},{self.y_coord})"

def move(car:Car,dx,dy):
    if Car(car.x_coord + dx, car.y_coord + dy) not in Car.cars:
        car.x_coord += dx
        car.y_coord += dy
        print(car)
    else:
        print("Μηνυμα λαθους, δεν μπορει να ειναι στην ιδια θεση")

def make_car(x,y):
    if Car(x,y) not in Car.cars:
        car = Car(x,y)
        Car.cars.append(car)
        print(f"make{car}")
        return car
    else:
        print("Μηνυμα λαθους, δεν μπορει να ειναι στην ιδια θεση")

def move_up(car: Car):
    move(car,0,1)

def move_down(car: Car):
    move(car,0,-1)

def move_right(car: Car):
    move(car,1,0)

def move_left(car: Car):
    move(car,-1,0)

car1 = make_car(0,0)
move_left(car1)
(-1,0)
car2 = make_car(2,2)
(2,2)
move_up(car2)
(2,3)
move_right(car1)
(0,0)
move_right(car1)
(1,0)
move_right(car1)
(2,0)
move_up(car1)
(2,1)
move_up(car1)
(2,2)
move_up(car1)