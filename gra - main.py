from random import randint

class Tiles:
    def __init__(self,x,y):
        self.koordynat_x = x
        self.koordynat_y = y
class Plains(Tiles):
    def __init__(self, x, y):
        self.jaki_biom = "plains"
        self.mozna_budowac = True
        super().__init__(x, y)
    def drukmapy(self):
            print(" _ ",end="")
    def zmianalinijkimapy(self):
            print(" R ")

class Mountains(Tiles):
    def __init__(self, x, y):
        self.jaki_biom = "Mountains"
        self.mozna_budowac = True
        super().__init__(x, y)
    def drukmapy(self):
            print(" A ",end="")
    def zmianalinijkimapy(self):
            print(" R ")
mapa = []
n = 1
a = 1
for i in range(2500):
    if a < 50:
        x = randint(1,5)
        if x != 1:
            tile = Plains(a,n)
        elif x == 1:
             tile = Mountains(a,n)    
        mapa.append(tile)
        a+=1
    elif a >= 50:
        a -= 50
        n += 1
        x = randint(1,5)
        if x != 1:
            tile = Plains(a,n)
        elif x == 1:
             tile = Mountains(a,n)    
        mapa.append(tile)

n = 1
for obj in mapa:
    if obj.koordynat_y == n:
        obj.drukmapy()
    elif obj.koordynat_y != n:
         obj.zmianalinijkimapy()
         n += 1


        