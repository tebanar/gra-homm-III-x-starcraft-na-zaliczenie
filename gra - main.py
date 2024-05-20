from random import randint
mapa = []
addmove = 0
lista_postaci = []
y = 1
x = 0
n = 0
day_counter = 0
movementpoints = 10
class Tiles:
    def __init__(self,x,y,id):
        self.koordynat_x = x
        self.koordynat_y = y
        self.id = id
class Plains(Tiles):

    def __init__(self, x, y,id):
        self.jaki_biom = "Plains"
        self.mozna_budowac = False
        self.mozna_chodzic = True
        self.mozna_przeszukac = True
        self.rzadkosc_przeszukania = "common"
        self.trudny_teren = False
        super().__init__(x, y, id)
    def drukmapy(self):
            print("\033[1;32;40m _ ",end="")
    def zmianalinijkimapy(self):
            print(" _ ")

class Mountains(Tiles):
    def __init__(self, x, y,id):
        self.jaki_biom = "Mountains"
        self.mozna_budowac = True
        self.mozna_przeszukac = True
        self.rzadkosc_przeszukania = "rare"
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
        self.mozna_przeszukac = False
        self.trudny_teren = False
        super().__init__(x, y,id)
    def drukmapy(self):
            print("\033[1;33;40m H ",end="")
    def zmianalinijkimapy(self):
            print(" H ")
class KopalniaZlota(Tiles):
    def __init__(self, x, y,id):
        self.jaki_biom = "Kopalnia_zlota"
        self.mozna_budowac = True
        self.mozna_chodzic = True
        self.mozna_przeszukac = False
        self.trudny_teren = False
        super().__init__(x, y,id)
    def drukmapy(self):
            print("\033[1;35;40m Z ",end="")
    def zmianalinijkimapy(self):
            print(" Z ")
class KopalniaKamienia(Tiles):
    def __init__(self, x, y,id):
        self.jaki_biom = "Kopalnia_kamienia"
        self.mozna_budowac = False
        self.mozna_chodzic = False
        self.mozna_przeszukac = False
        self.trudny_teren = False
        super().__init__(x, y,id)
    def drukmapy(self):
            print("\033[1;35;40m K ",end="")
    def zmianalinijkimapy(self):
            print(" K ")
class Lumberjack(Tiles):
    def __init__(self, x, y,id):
        self.jaki_biom = "Drwal"
        self.mozna_budowac = False
        self.mozna_chodzic = False
        self.mozna_przeszukac = False
        self.trudny_teren = False
        super().__init__(x, y,id)
    def drukmapy(self):
            print("\033[1;35;40m D ",end="")
    def zmianalinijkimapy(self):
            print(" D ")
class Forest(Tiles):
    def __init__(self, x, y,id):
        self.jaki_biom = "Forest"
        self.mozna_budowac = True
        self.mozna_przeszukac = True
        self.mozna_chodzic = True
        self.rzadkosc_przeszukania = "epic"
        self.trudny_teren = True
        super().__init__(x, y,id)
    def drukmapy(self):
            print("\033[1;32;40m F ",end="")
    def zmianalinijkimapy(self):
            print(" F ")


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
        a = randint(1,1000)
        if a >= 1 and a <=10:
             tile = Mountains(x,y,i)
        elif a >= 11 and a <=20:
             tile = Forest(x,y,i)

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
def generacja_lasu(tile:object,mapa:list,n):

        if n>51 and n<2400:
            if mapa[n].jaki_biom == "Plains":

                
                if mapa[n+1].jaki_biom=="Forest" or mapa[n+51].jaki_biom=="Forest":
                    x = randint(1,3)
                    if x == 3:
                         return Forest(mapa[n].koordynat_x,mapa[n].koordynat_y,mapa[n].id)
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
for i in range(17):
     n=0
     for obj in mapa:
          mapa[n] = generacja_lasu(obj,mapa,n)
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

def jakabudowla(koordynat_x,koordynat_y,id,mapa):

     while True:
        print("a-most(pozwala łatwiej przejść przez trudny teren)(1 drewno)")
        print("b-kopalnia kamienia(daje 3 kamienia na dzien)(10 drewna,5 kamienia)")
        print("c-kopalnia zlota(daje 500 zlota na dzien)(20 drewna,20 kamienia)")
        print("d-drwal(daje 5 drewna na dzien)(15 drewna,10 kamienia)")
        wybor = input()
        for obj in mapa:

            if wybor == "a" and koordynat_x == obj.koordynat_x and koordynat_y == obj.koordynat_y and obj.mozna_budowac == True:

                    return Bridge(koordynat_x,koordynat_y,id)


            elif wybor == "b" and koordynat_x == obj.koordynat_x and koordynat_y == obj.koordynat_y and obj.jaki_biom == "Mountains":
                    return KopalniaKamienia(koordynat_x,koordynat_y,id)

            elif wybor == "c" and koordynat_x == obj.koordynat_x and koordynat_y == obj.koordynat_y and obj.jaki_biom == "Mountains":
                    return KopalniaZlota(koordynat_x,koordynat_y,id)

            elif wybor == "d" and koordynat_x == obj.koordynat_x and koordynat_y == obj.koordynat_y and obj.jaki_biom == "Forest":
                    return Lumberjack(koordynat_x,koordynat_y,id)


def system_ruchu(day_counter,postac,lista_postaci,mapa,addmove):
     day_counter+=1
     o = 0
     movementpoints = 10 + addmove

     while movementpoints>0:
        i = True
        while i == True:

 

                wsad = input("wasd - ")
                if wsad == "a":
                        for obj in mapa:
                            if obj.koordynat_x == postac.koordynat_x-1 and obj.koordynat_y == postac.koordynat_y and obj.mozna_chodzic == True:
                                postac.replacex(postac.koordynat_x-1)
                                i = False
                                if obj.trudny_teren == True:
                                     movementpoints-=2
                                else:
                                     movementpoints-=1

                                break
                if wsad == "d":
                        for obj in mapa:
                            if obj.koordynat_x == postac.koordynat_x+1 and obj.koordynat_y == postac.koordynat_y and obj.mozna_chodzic == True:
                                postac.replacex(postac.koordynat_x+1)
                                i = False  
                                if obj.trudny_teren == True:
                                     movementpoints-=2
                                else:
                                     movementpoints-=1                                
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
                                if obj.trudny_teren == True:
                                     movementpoints-=2
                                else:
                                     movementpoints-=1                                
                                break


                if wsad == "ab":
                        for obj in mapa:
                            if obj.koordynat_x == postac.koordynat_x-1 and obj.koordynat_y == postac.koordynat_y and obj.mozna_budowac == True:
                                mapa[obj.id] = jakabudowla(obj.koordynat_x,obj.koordynat_y,obj.id,mapa)
                                o +=1
                                i = False
                                movementpoints-=1  
                                break
                if wsad == "db":
                        for obj in mapa:
                            if obj.koordynat_x == postac.koordynat_x+1 and obj.koordynat_y == postac.koordynat_y and obj.mozna_budowac == True:
                                mapa[obj.id] = jakabudowla(obj.koordynat_x,obj.koordynat_y,obj.id,mapa)
                                i = False
                                o +=1
                                movementpoints-=1  
                                break  
                if wsad == "sb":
                        for obj in mapa:
                            if obj.koordynat_x == postac.koordynat_x and obj.koordynat_y == postac.koordynat_y+1 and obj.mozna_budowac == True:
                                mapa[obj.id] = jakabudowla(obj.koordynat_x,obj.koordynat_y,obj.id,mapa)
                                i = False
                                o +=1
                                movementpoints-=1  
                                break
                if wsad == "wb":
                        for obj in mapa:
                            if obj.koordynat_x == postac.koordynat_x and obj.koordynat_y == postac.koordynat_y-1 and obj.mozna_budowac == True:
                                mapa[obj.id] = jakabudowla(obj.koordynat_x,obj.koordynat_y,obj.id,mapa)
                                i = False
                                o +=1
                                movementpoints-=1  
                                break
                # if wsad == "ap":
                #         for obj in mapa:
                #             if obj.koordynat_x == postac.koordynat_x-1 and obj.koordynat_y == postac.koordynat_y and obj.mozna_budowac == True:
                #                 mapa[obj.id] = Bridge(obj.koordynat_x,obj.koordynat_y,obj.id)
                #                 o +=1
                #                 i = False
                #                 movementpoints-=1  
                #                 break
                # if wsad == "dp":
                #         for obj in mapa:
                #             if obj.koordynat_x == postac.koordynat_x+1 and obj.koordynat_y == postac.koordynat_y and obj.mozna_budowac == True:
                #                 mapa[obj.id] = Bridge(obj.koordynat_x,obj.koordynat_y,obj.id)
                #                 i = False
                #                 o +=1
                #                 movementpoints-=1  
                #                 break  
                # if wsad == "sp":
                #         for obj in mapa:
                #             if obj.koordynat_x == postac.koordynat_x and obj.koordynat_y == postac.koordynat_y+1 and obj.mozna_budowac == True:
                #                 mapa[obj.id] = Bridge(obj.koordynat_x,obj.koordynat_y,obj.id)
                #                 i = False
                #                 o +=1
                #                 movementpoints-=1  
                #                 break
                # if wsad == "wp":
                #         for obj in mapa:
                #             if obj.koordynat_x == postac.koordynat_x and obj.koordynat_y == postac.koordynat_y-1 and obj.mozna_budowac == True:
                #                 mapa[obj.id] = Bridge(obj.koordynat_x,obj.koordynat_y,obj.id)
                #                 i = False
                #                 o +=1
                #                 movementpoints-=1  
                #                 break
        if movementpoints < 0:
             movementpoints = 0

        print(postac.koordynat_x,postac.koordynat_y,"day - ",day_counter,"action points left - ",movementpoints)
        if day_counter>=1 and day_counter%2==0:
            print("night")
        else:
            print("day")
        generacjamapy(mapa,lista_postaci)



while True:
        print("\033[1;37;40m postac 1")

        system_ruchu(day_counter,lista_postaci[0],lista_postaci,mapa,addmove)
        print("\033[1;37;40m postac 2")

        system_ruchu(day_counter,lista_postaci[1],lista_postaci,mapa,addmove)
        print("\033[1;37;40m postac 3")

        system_ruchu(day_counter,lista_postaci[2],lista_postaci,mapa,addmove)
