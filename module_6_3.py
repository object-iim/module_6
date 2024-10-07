class Horse:

    x_distance = 0
    sound = 'Frrr'

    def run(self, dx: int):
        self.x_distance += dx


class Eagle:

    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def fly(self,dy: int):
        self.y_distance += dy

class Pegasus(Eagle, Horse):

    def move(self, dx: int, dy: int):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
