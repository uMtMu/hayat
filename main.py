# -*- coding: utf-8 -*-
from random import randint

__author__ = 'umt'

class YasamAlani():
    alan = [[[] for l in range(10)] for t in range(10)]

    @staticmethod
    def yerlestir(x=None, y=None, birey=None):
        if birey:
            # Birey oluşturuldu ise
            YasamAlani.alan[x+1][y+1].append(birey)
        else:
            # Birey oluşturulması ise
            x = x + 1 if x != None else randint(0, 9)
            y = y + 1 if y != None else randint(0, 9)

            isim = 'Birey ' + str(x) + str(y)
            YasamAlani.alan[x][y].append(Birey(isim, x, y))

    @staticmethod
    def goruntule():
        for satir in YasamAlani.alan:
            for sutun in satir:
                print sutun,
            print ''
        pass


class Birey():
    def __init__(self, isim, x, y):
        self.isim = isim
        self.x = x
        self.y = y

    def __repr__(self):
        return self.isim


YasamAlani.yerlestir(2, 3)
YasamAlani.yerlestir()
YasamAlani.yerlestir()
YasamAlani.yerlestir()

YasamAlani.goruntule()