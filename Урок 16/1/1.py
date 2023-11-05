class kassa(object):
    
    def __init__(self, balans):
        self.balans = balans

    def top_up(self, x):
        self.balans += x

    def count_1000(self):
        print('В кассе', self.balans // 1000, 'тысяч')

    def take_away(self, y):
        if y <= self.balans:
            print(f'Вы забрали из кассы {y}')
            self.balans -= y
        else:
            print(f'В кассе недостаточно денег')

z = kassa(1236)
z.count_1000()
print(z.balans)
z.top_up(200)
print(z.balans)
z.take_away(600)
print(z.balans)
