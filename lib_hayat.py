#! /usr/bin/python
# -*- coding: utf-8 -*-
from random import randint
import uuid

__author__ = 'umt'

class YasamAlani():
    ALAN_X = ALAN_Y = 10
    alan = [[[] for l in range(ALAN_X)] for t in range(ALAN_Y)]

    varliklar = []

    @staticmethod
    def yerlestir(x=None, y=None, varlik=None):
        if varlik:
            # varlik oluşturuldu ise
            YasamAlani.alan[x-1][y-1].append(varlik)
        else:
            # varlik oluşturulması ise
            x = x if x != None else randint(0, YasamAlani.ALAN_X - 1)
            y = y if y != None else randint(0, YasamAlani.ALAN_Y - 1)
            isim = 'B' + str(x) + str(y)

            varlik = Birey(isim, x, y)
            YasamAlani.alan[x][y].append(varlik)

        YasamAlani.varliklar.append(varlik)
        return varlik

    @staticmethod
    def goruntule():
        print '-' * 40
        for satir in YasamAlani.alan:
            for sutun in satir:
                print sutun,
                print "\t",
            print ''
        print ''

    @staticmethod
    def konumlandir(ix, iy, varlik, x, y):
        index = YasamAlani.alan[ix][iy].index(varlik)
        if ix + x < YasamAlani.ALAN_X and iy + y < YasamAlani.ALAN_Y:
            if ix + x > -1 and iy + y > -1:
                YasamAlani.alan[ix+x][iy+y].append(YasamAlani.alan[ix][iy][index])
                YasamAlani.alan[ix][iy].remove(varlik)
                return True
        else:
            return False

    @staticmethod
    def hucre(x, y):
        return YasamAlani.alan[x][y]

    @staticmethod
    def varlik_listele():
        for varlik in YasamAlani.varliklar:
           print varlik 

    @staticmethod
    def canlan():
        pass
        

class Varlik:
    def __init__(self, isim, x, y):
        self.isim = isim
        self.x = x
        self.y = y
        self.uid = uuid.uuid4()

    def __repr__(self):
        return self.isim

    def detay_ver(self):
        return "İsim: %s\nID: %s" % (self.isim, self.uid)

class Hareketli:
    def hareket_et(self, x, y):
        if YasamAlani.konumlandir(self.x, self.y, self, x, y):
            print "%s konumunu (%d,%d)'den (%d,%d)'ye değişti" % (str(self), self.x, self.y, self.x+x, self.y+y)
            self.x += x
            self.y += y
        else:
            print str(self) + ' konum değiştiremedi'

    def saga_git(self):
        self.hareket_et(0, 1)

    def sola_git(self):
        self.hareket_et(0, -1)

    def asagi_git(self):
        self.hareket_et(1, 0)

    def yukari_git(self):
        self.hareket_et(-1, 0)


class Birey(Varlik, Hareketli):
    def __init__(self, isim, x, y):
        Varlik.__init__(self, isim, x, y)
