#car1 = make_car(0,0)
#move_left(car1)
#(-1,0)
#>>car2 = make_car(2,2)
#move_right(car2)
#(2,3)
#move_right(car1)
#(0,0)
#move_right(car1)
#(1,0)
#move_right(car1)
#(2,0)
#move_up(car1)
#(2,1)
#move_up(car1)
#(2,2)
#move_up(car1)
#'Μηνυμα λαθους, δεν μπορει να ειναι στην ιδια θεση'
class Car:
    positions = []
    current = 0
    def __init__(self,x,y):
        self.index = Car.current
        Car.current = self.index + 1
        self.pos = [x,y]
        Car.positions.append(self.pos)
    def execute(self,new_pos):
        failed = False
        for i in range(0,len(Car.positions)):
            if Car.positions[i][0] == new_pos[0] and Car.positions[i][1] == new_pos[1]:
                failed = True
        if failed:
            return 'Μηνυμα λαθους, δεν μπορει να ειναι στην ιδια θεση'
        else:
            self.pos = new_pos
            Car.positions[self.index] = new_pos
            return f"({self.pos[0]}, {self.pos[1]})"
    def move(self,x,y):
        return self.execute([self.pos[0] + x,self.pos[1] + y])
def make_car(x,y):
    return Car(x,y)
def move_up(c):
    return c.move(0,1)
def move_right(c):
    return c.move(1,0)
def move_down(c):
    return c.move(0,-1)
def move_left(c):
    return c.move(-1,0)

car1 = make_car(0,0)
print(move_left(car1))
(-1,0)
car2 = make_car(2,2)
print(move_up(car2))
(2,3)
print(move_right(car1))
(0,0)
print(move_right(car1))
(1,0)
print(move_right(car1))
(2,0)
print(move_up(car1))
(2,1)
print(move_up(car1))
(2,2)
print(move_up(car1))
'Μηνυμα λαθους, δεν μπορει να ειναι στην ιδια θεση'