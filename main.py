# -*- coding: utf-8 -*-
from random import randint

__author__ = 'umt'

class YasamAlani():
    ALAN_X = ALAN_Y = 10
    alan = [[[] for l in range(ALAN_X)] for t in range(ALAN_Y)]

    @staticmethod
    def yerlestir(x=None, y=None, birey=None):
        if birey:
            # Birey oluşturuldu ise
            YasamAlani.alan[x-1][y-1].append(birey)
        else:
            # Birey oluşturulması ise
            x = x if x != None else randint(0, 9)
            y = y if y != None else randint(0, 9)
            isim = 'Birey ' + str(x) + str(y)

            YasamAlani.alan[x][y].append(Birey(isim, x, y))

    @staticmethod
    def goruntule():
        print '-' * 40
        for satir in YasamAlani.alan:
            for sutun in satir:
                print sutun,
            print ''
        print ''

    @staticmethod
    def konumlandir(ix, iy, birey, x, y):
        index = YasamAlani.alan[ix][iy].index(birey)
        if ix + x < YasamAlani.ALAN_X and iy + y < YasamAlani.ALAN_Y:
            if ix + x > -1 and iy + y > -1:
                YasamAlani.alan[ix+x][iy+x].append(YasamAlani.alan[ix][iy][index])
                YasamAlani.alan[ix][iy].remove(birey)
                return True
        else:
            return False

    @staticmethod
    def hucre(x, y):
        return YasamAlani.alan[x][y]


class Birey():
    def __init__(self, isim, x, y):
        self.isim = isim
        self.x = x
        self.y = y

    def hareket_et(self, x, y):
        if YasamAlani.konumlandir(self.x, self.y, self, x, y):
            print "%s konumunu (%d,%d)'den (%d,%d)'ye değişti" % (str(self), self.x, self.y, self.x+x, self.y+y)
            self.x += x
            self.y += y
        else:
            print str(self) + ' konum değiştiremedi'

    def __repr__(self):
        return self.isim


YasamAlani.yerlestir(2, 3)
YasamAlani.yerlestir()
YasamAlani.yerlestir()
YasamAlani.yerlestir()

YasamAlani.goruntule()

YasamAlani.hucre(2, 3)[0].hareket_et(-1, -1)
YasamAlani.goruntule()
# YasamAlani.hucre(3, 4)[0].hareket_et(1, 1)
# YasamAlani.goruntule()
# YasamAlani.hucre(4, 5)[0].hareket_et(2, 2)
# YasamAlani.goruntule()
# YasamAlani.hucre(6, 7)[0].hareket_et(4, 4)
# YasamAlani.goruntule()

