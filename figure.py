from random import randint
from numpy import size


class Carre():
    def __init__(self, pos: tuple(), max_size: int, fill: bool=False, weight: int = 2) -> None:
        self.pos = pos
        self.x, self.y = self.pos
        self.size = randint(6, max_size)
        self.fill = fill
        if fill:
            self.weight = 2
        else:
            self.weight = weight
    
    def points(self) -> list:
        points = []
        demi = int(self.size / 2)
        first_point = (self.x + demi, self.y - demi)
        if first_point[0] != 0 and first_point[1] != 0:
            points.append(first_point)
        last_point = None
        for i in range(first_point[1] + 1, first_point[1] + self.size):
            points.append((first_point[0], i))
        last_point = points[-1]
        for i in range(first_point[0] + 1, first_point[0] + self.size):
            points.append((i, last_point[1]))
        last_point = points[-1]
        for i in range(last_point[1] - 1, first_point[1] - 1, -1):
            points.append((last_point[0], i))
        last_point = points[-1]
        for i in range(last_point[0] - 1, first_point[0], -1):
            points.append((i, last_point[1]))
        return points
carre = Carre(pos=(0,0), max_size=50)
print("attendu : " + str(carre.size - 1) + " x 4 = " + str((carre.size - 1) * 4))
print(len(carre.points()))