from random import randint
mapa = []
lista_postaci = []
y = 1
x = 0
n = 0
day_counter = 0
movementpoints = 1000
class Tiles:
    def __init__(self,x,y,id):
        self.koordynat_x = x
        self.koordynat_y = y
        self.id = id
class Plains(Tiles):

    def __init__(self, x, y,id):
        self.jaki_biom = "Plains"
        self.mozna_budowac = True
        self.mozna_chodzic = True
        super().__init__(x, y, id)
    def drukmapy(self):
            print("\033[1;32;40m _ ",end="")
    def zmianalinijkimapy(self):
            print(" _ ")

class Mountains(Tiles):
    def __init__(self, x, y,id):
        self.jaki_biom = "Mountains"
        self.mozna_budowac = True
        self.mozna_chodzic = False
        super().__init__(x, y,id)
    def drukmapy(self):
            print("\033[1;37;40m A ",end="")
    def zmianalinijkimapy(self):
            print(" A ")

class Bridge(Tiles):
    def __init__(self, x, y,id):
        self.jaki_biom = "Bridge"
        self.mozna_budowac = True
        self.mozna_chodzic = True
        super().__init__(x, y,id)
    def drukmapy(self):
            print("\033[1;33;40m Z ",end="")
    def zmianalinijkimapy(self):
            print(" Z ")


class Jednostka(Tiles):
     def __init__(self, x, y, id):
          super().__init__(x, y, id)
     def drukjednostki(self):
            print("\033[1;31;40m O ",end="")
     def replacex(self,x):
          self.koordynat_x = x
     def replacey(self,y):
          self.koordynat_y = y

# =============================================================================
for i in range(2499):
    a = 0
    
    if x < 50:
        a = randint(1,100)
        if a == 1:
             tile = Mountains(x,y,i)
        elif a == 2:
             tile = Bridge(x,y,i)
        else:
            tile = Plains(x,y,i)

        mapa.append(tile)
        x+=1
    elif x >= 50:
        x -= 50
        y += 1

        tile = Plains(x,y,i)
 
        mapa.append(tile)

# =============================================================================
def generacja_gor(tile:object,mapa:list,n):

        if n>51 and n<2400:
            if mapa[n].jaki_biom == "Plains":

                
                if mapa[n+1].jaki_biom=="Mountains" or mapa[n+51].jaki_biom=="Mountains":
                    x = randint(1,3)
                    if x == 3:
                         return Mountains(mapa[n].koordynat_x,mapa[n].koordynat_y,mapa[n].id)
                    else: return tile
        return tile

def gen_postaci(mapa,n, lista_postaci):
    
    q = 0
    while q == 0:
        x = randint(2,49)
        y = randint(2,49)
        for i in mapa:
            if x == i.koordynat_x and y == i.koordynat_y and i.jaki_biom == "Plains":
                q+=1
                n+=1
                obj = Jednostka(x,y,n)
                lista_postaci.append(obj)
                return lista_postaci
            else:continue
         

for i in range(20):

     n = 0
     for obj in mapa:


        mapa[n] = generacja_gor(obj,mapa,n)

        n+=1

gen_postaci(mapa,n,lista_postaci)
gen_postaci(mapa,n,lista_postaci)
gen_postaci(mapa,n,lista_postaci)
def generowanie_postaci_na_mapie(lista_postaci,obj):

    for i in lista_postaci:
        if obj.koordynat_y == i.koordynat_y and obj.koordynat_x == i.koordynat_x:


             return True

def generacjamapy(mapa,lista_postaci):
    n = 1
    i = 0
    for obj in mapa:
        if generowanie_postaci_na_mapie(lista_postaci,obj):
                lista_postaci[i].drukjednostki()
                i+=1

                

        elif obj.koordynat_y == n:
                obj.drukmapy()
        elif obj.koordynat_y != n:
                obj.zmianalinijkimapy()
                n += 1


generacjamapy(mapa,lista_postaci)



def system_ruchu(wsadczyxy,day_counter,postac,lista_postaci,mapa):
     day_counter+=1
     o = 0
     i = True
     while i == True:

        if wsadczyxy == "koordynaty":
            x = int(input("x = "))
            y = int(input("y = "))

            for obj in mapa:
                if  x  + y < movementpoints + postac.koordynat_y + postac.koordynat_x: 
                    if obj.koordynat_x == x and obj.koordynat_y == y and obj.mozna_budowac == True:
                        postac.replacex(x)
                        postac.replacey(y)
                        i = False
                        break
                else: 
                    print("nie")
                    break
        elif wsadczyxy == "wasd":
             wsad = input("wasd - ")
             if wsad == "a":
                    for obj in mapa:
                        if obj.koordynat_x == postac.koordynat_x-1 and obj.koordynat_y == postac.koordynat_y and obj.mozna_chodzic == True:
                            postac.replacex(postac.koordynat_x-1)
                            i = False
                            break
             if wsad == "d":
                    for obj in mapa:
                        if obj.koordynat_x == postac.koordynat_x+1 and obj.koordynat_y == postac.koordynat_y and obj.mozna_chodzic == True:
                            postac.replacex(postac.koordynat_x+1)
                            i = False  
                            break  
             if wsad == "s":
                    for obj in mapa:
                        if obj.koordynat_x == postac.koordynat_x and obj.koordynat_y == postac.koordynat_y+1 and obj.mozna_chodzic == True:
                            postac.replacey(postac.koordynat_y+1)
                            i = False
                            break
             if wsad == "w":
                    for obj in mapa:
                        if obj.koordynat_x == postac.koordynat_x and obj.koordynat_y == postac.koordynat_y-1 and obj.mozna_chodzic == True:
                            postac.replacey(postac.koordynat_y-1)
                            i = False
                            break


             if wsad == "ab":
                    for obj in mapa:
                        if obj.koordynat_x == postac.koordynat_x-1 and obj.koordynat_y == postac.koordynat_y and obj.mozna_budowac == True:
                            mapa[o] = Bridge(obj.koordynat_x-1,obj.koordynat_y,obj.id)
                            o +=1
                            i = False
                            break
             if wsad == "db":
                    for obj in mapa:
                        if obj.koordynat_x == postac.koordynat_x+1 and obj.koordynat_y == postac.koordynat_y and obj.mozna_budowac == True:
                            mapa[o] = Bridge(obj.koordynat_x+1,obj.koordynat_y,obj.id)
                            i = False
                            o +=1
                            break  
             if wsad == "sb":
                    for obj in mapa:
                        if obj.koordynat_x == postac.koordynat_x and obj.koordynat_y == postac.koordynat_y+1 and obj.mozna_budowac == True:
                            mapa[o] = Bridge(obj.koordynat_x,obj.koordynat_y+1,obj.id)
                            i = False
                            o +=1
                            break
             if wsad == "wb":
                    for obj in mapa:
                        if obj.koordynat_x == postac.koordynat_x and obj.koordynat_y == postac.koordynat_y-1 and obj.mozna_budowac == True:
                            mapa[o] = Bridge(obj.koordynat_x,obj.koordynat_y-1,obj.id)
                            i = False
                            o +=1
                            break

     print(postac.koordynat_x,postac.koordynat_y)
     generacjamapy(mapa,lista_postaci)


print("\033[1;37;40m koordynaty czy wasd?")
wsadczyxy = input()
while True:
    print("\033[1;37;40m postac 1")
    system_ruchu(wsadczyxy,day_counter,lista_postaci[0],lista_postaci,mapa)
    print("\033[1;37;40m postac 2")
    system_ruchu(wsadczyxy,day_counter,lista_postaci[1],lista_postaci,mapa)
    print("\033[1;37;40m postac 3")
    system_ruchu(wsadczyxy,day_counter,lista_postaci[2],lista_postaci,mapa)
