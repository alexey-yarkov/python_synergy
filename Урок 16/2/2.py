class cherepashka(object):

    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s == 1:
            print('Шаг не может быть меньше еденицы')
        else:
            self.s -= 1
            
    def count_moves(self, x2, y2):
        k = 0
        ks1 = 0
        ks2 = 0
        d = self.s
        if abs(self.x - x2) % self.s == 0:
            k = abs(self.x - x2) // self.s
        else:
            k = abs(self.x - x2) // self.s
            ks1 = abs(self.x - x2) % self.s
        if abs(self.y - y2) % self.s == 0:
            k = k + abs(self.y - y2) // self.s
        else:
            k = k + abs(self.y - y2) // self.s
            ks2 = abs(self.y - y2) % self.s
        if ks2 == ks1:
            while d >= ks1:
                d -= 1
                k += 1
            k += 1
        else:
            ks1, ks2 = ks2, ks1
            while d >= ks1:
                d -= 1
                k += 1
            while d >= ks2:
                d -= 1
                k += 1
            
        return k

X = int(input('Веедите кординату x = '))
Y = int(input('Веедите кординату y = '))
S = int(input('Веедите шаг s = '))
a = cherepashka(X, Y, S)
print(a.x, a.y, a.s)
print(a.count_moves(20, 20))
