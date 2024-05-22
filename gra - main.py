from random import randint
mapa = []
addmove = 0
lista_potworow = []
lista_postaci = []
drewno = 50
kamien = 50
zloto = 1000
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
class Interactable(Tiles):
    def __init__(self, x, y,id):
        self.interakcja = True
        super().__init__(x, y,id)
class Generation(Tiles):
    def __init__(self, x, y,id):
        self.generation = True
        super().__init__(x, y,id)   


# =======================================     
class Plains(Tiles):
    def __init__(self, x, y,id):
        self.jaki_biom = "Plains"
        self.mozna_budowac = False
        self.generation = False
        self.mozna_chodzic = True
        self.trudny_teren = False
        super().__init__(x, y, id)
    def drukmapy(self):
            print("\033[1;32;40m _ ",end="")
    def zmianalinijkimapy(self):
            print(" _ ")
class Forest(Tiles):
    def __init__(self, x, y,id):
        self.jaki_biom = "Forest"
        self.mozna_budowac = True
        self.generation = False
        self.mozna_chodzic = True
        self.trudny_teren = True
        super().__init__(x, y,id)
    def drukmapy(self):
            print("\033[1;32;40m F ",end="")
    def zmianalinijkimapy(self):
            print(" F ")
class Mountains(Tiles):
    def __init__(self, x, y,id):
        self.jaki_biom = "Mountains"
        self.mozna_budowac = True
        self.generation = False
        self.mozna_chodzic = False

        super().__init__(x, y,id)
    def drukmapy(self):
            print("\033[1;37;40m A ",end="")
    def zmianalinijkimapy(self):
            print(" A ")
# =============================================================
class Bridge(Tiles):
    def __init__(self, x, y,id):
        self.jaki_biom = "Bridge"
        self.mozna_budowac = True
        self.mozna_chodzic = True
        self.generation = False
        self.trudny_teren = False
        super().__init__(x, y,id)
    def drukmapy(self):
            print("\033[1;33;40m H ",end="")
    def zmianalinijkimapy(self):
            print(" H ")
class KopalniaZlota(Generation):
    def __init__(self, x, y,id):
        self.jaki_biom = "Kopalnia_zlota"
        self.mozna_budowac = False
        self.mozna_chodzic = False
        self.trudny_teren = False
        super().__init__(x, y,id)
    def drukmapy(self):
            print("\033[1;35;40m Z ",end="")
    def zmianalinijkimapy(self):
            print(" Z ")
class KopalniaKamienia(Generation):
    def __init__(self, x, y,id):
        self.jaki_biom = "Kopalnia_kamienia"
        self.mozna_budowac = False
        self.mozna_chodzic = False
        self.trudny_teren = False
        super().__init__(x, y,id)
    def drukmapy(self):
            print("\033[1;35;40m K ",end="")
    def zmianalinijkimapy(self):
            print(" K ")
class Lumberjack(Generation):
    def __init__(self, x, y,id):
        self.jaki_biom = "Drwal"
        self.mozna_budowac = False
        self.mozna_chodzic = False
        self.trudny_teren = False
        super().__init__(x, y,id)
    def drukmapy(self):
            print("\033[1;35;40m D ",end="")
    def zmianalinijkimapy(self):
            print(" D ")
# ==========================================================
class Miasto(Interactable):
    def __init__(self, x, y,id):
        self.jaki_biom = "Miasto"
        self.mozna_budowac = False
        self.mozna_chodzic = False
        self.generation = False
        self.trudny_teren = False
        super().__init__(x, y,id)
    def drukmapy(self):
            print("\033[1;34;40m M ",end="")
    def zmianalinijkimapy(self):
            print(" M ")

class Skrzynia(Interactable):
    def __init__(self, x, y,id):
        self.jaki_biom = "Skrzynia"
        self.mozna_budowac = False
        self.mozna_chodzic = False
        self.generation = False
        self.trudny_teren = False
        super().__init__(x, y,id)
    def drukmapy(self):
            print("\033[1;33;40m C ",end="")
    def zmianalinijkimapy(self):
            print(" C ")

# ===============================================================
class Jednostka(Tiles):
     def __init__(self, x, y, id):
          self.ekwipunek = []
          super().__init__(x, y, id)
     def drukjednostki(self):
            print("\033[1;31;40m O ",end="")
     def replacex(self,x):
          self.koordynat_x = x
     def replacey(self,y):
          self.koordynat_y = y
class Przeciwnik(Tiles):
     def __init__(self, x, y, id):
        self.jaki_biom = "Przeciwnik"
        self.mozna_budowac = False
        self.mozna_chodzic = False
        self.generation = False
        self.trudny_teren = False
        super().__init__(x, y, id)
     def drukjednostki(self):
            print("\033[1;36;40m P ",end="")
     def replacex(self,x):
          self.koordynat_x = x
     def replacey(self,y):
          self.koordynat_y = y
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

        for i in mapa:
            if i.jaki_biom == "Miasto":
                q+=1
                n+=1
                obj = Jednostka(i.koordynat_x,i.koordynat_y,n)
                lista_postaci.append(obj)
                return lista_postaci
            else:continue

def gen_potworow(mapa,n, lista_potworow):
    
    q = 0
    while q == 0:
        x = randint(2,48)
        y = randint(2,48)

        for i in mapa:
            if i.mozna_chodzic == True and x == i.koordynat_x and y == i.koordynat_y:
                q+=1
                n+=1
                print(i.koordynat_x,i.koordynat_y,n)
                obj = Przeciwnik(i.koordynat_x,i.koordynat_y,n)
                lista_potworow.append(obj)
                return lista_potworow
            else:continue






def generowanie_postaci_na_mapie(lista_postaci,obj):

    for i in lista_postaci:
        if obj.koordynat_y == i.koordynat_y and obj.koordynat_x == i.koordynat_x:


             return True
def generowanie_potworow_na_mapie(lista_potworow,obj):

    for i in lista_potworow:
        if obj.koordynat_y == i.koordynat_y and obj.koordynat_x == i.koordynat_x:


             return True
def zbieranie_surowce(drewno,zloto,kamien,mapa):
    for obj in mapa:
        if obj.generation == True:
             if obj.jaki_biom == "Drwal":
                  drewno+=3
             elif obj.jaki_biom == "Kopalnia_zlota":
                  zloto+=200
             elif obj.jaki_biom == "Kopalnia_kamienia":
                  kamien+=2
    return drewno,kamien,zloto
def generacjamapy(mapa,lista_postaci,lista_potworow):
    n = 1
    i = 0
    p = 0
    for obj in mapa:

        if generowanie_postaci_na_mapie(lista_postaci,obj):
                lista_postaci[i].drukjednostki()
                i+=1
        elif generowanie_potworow_na_mapie(lista_potworow,obj):
             lista_potworow[p].drukjednostki()
             p+=1

                

        elif obj.koordynat_y == n:
                obj.drukmapy()
        elif obj.koordynat_y != n:
                obj.zmianalinijkimapy()
                n += 1
# =============================================================================         
for i in range(2499):
    a = 0
    if i == 2250:
        tile = Miasto(x,y,i)
        x+=1
        mapa.append(tile)
    
    elif x < 50:
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




# ================================================================================
# ================================================================================
def miasto(mapa,n,lista_postaci):
     print("jestes w miescie")
     abc = input("jesli chcesz nowa postac napisz nowa postac - " )
     if abc == "nowa postac":
          gen_postaci(mapa,n,lista_postaci)
def skrzynia():
     print("wip")




def interakcja(koordynat_x,koordynat_y,mapa,n,lista_postaci,num):
     for obj in mapa:
          if koordynat_x == obj.koordynat_x and koordynat_y == obj.koordynat_y and obj.interakcja == True:
               if obj.jaki_biom == "Miasto":
                    miasto(mapa,n,lista_postaci)
               elif obj.jaki_biom == "Skrzynia":
                    skrzynia(lista_postaci,num)
# # ================================================================================
# ================================================================================
def jakabudowla(koordynat_x,koordynat_y,id,mapa,zloto,drewno,kamien):

     while True:
        print("(nazwa,co robi,koszt)")
        print("a-most(pozwala łatwiej przejść przez trudny teren)(2 drewno)")
        print("b-kopalnia kamienia(daje 2 kamienia na dzien)(10 drewna,5 kamienia ,300 zlota)")
        print("c-kopalnia zlota(daje 200 zlota na dzien)(20 drewna,20 kamienia 500 zlota)")
        print("d-drwal(daje 3 drewna na dzien)(15 drewna,10 kamienia,200 zlota)")
        print("q-wyjdz")
        wybor = input()
        for obj in mapa:

            if wybor == "a" and koordynat_x == obj.koordynat_x and koordynat_y == obj.koordynat_y and obj.mozna_budowac == True and drewno>=2:
                    drewno -= 2
                    return Bridge(koordynat_x,koordynat_y,id),drewno,kamien,zloto


            elif wybor == "b" and koordynat_x == obj.koordynat_x and koordynat_y == obj.koordynat_y and obj.jaki_biom == "Mountains" and drewno>=10 and kamien>=5 and zloto >= 300:
                    drewno-=10
                    kamien-=5
                    zloto -= 300
                    return KopalniaKamienia(koordynat_x,koordynat_y,id),drewno,kamien,zloto

            elif wybor == "c" and koordynat_x == obj.koordynat_x and koordynat_y == obj.koordynat_y and obj.jaki_biom == "Mountains" and drewno>=20 and kamien>=20 and zloto >= 500:
                    drewno-=20
                    kamien-=20
                    zloto -=500
                    return KopalniaZlota(koordynat_x,koordynat_y,id),drewno,kamien,zloto

            elif wybor == "d" and koordynat_x == obj.koordynat_x and koordynat_y == obj.koordynat_y and obj.jaki_biom == "Forest" and drewno>=15 and kamien>=10 and zloto >= 200:
                    drewno-=15
                    kamien-=10
                    zloto -=200
                    return Lumberjack(koordynat_x,koordynat_y,id),drewno,kamien,zloto
            elif wybor == "q" and koordynat_x == obj.koordynat_x and koordynat_y == obj.koordynat_y:
                    return obj,drewno,kamien,zloto

# ================================================================================
# ================================================================================
def system_ruchu_potwora(lista_potworow,lista_postaci):
     for i in lista_potworow:
          for obj in lista_postaci:
            if i.koordynat_x< 45 and i.koordynat_x> 5 and i.koordynat_x + 4>=obj.koordynat_x and i.koordynat_y< 45 and i.koordynat_y> 5 and i.koordynat_y + 4>=obj.koordynat_y and i.koordynat_y<= obj.koordynat_y and i.koordynat_x<= obj.koordynat_x:

                 print(i.koordynat_x,i.koordynat_y)
                 print(obj.koordynat_x,obj.koordynat_y)

                 print("a")
                 break
            
            elif i.koordynat_x< 45 and i.koordynat_x> 5 and i.koordynat_x - 4 <=obj.koordynat_x and i.koordynat_y< 45 and i.koordynat_y> 5 and i.koordynat_y - 4<=obj.koordynat_y and i.koordynat_y>= obj.koordynat_y and i.koordynat_x>= obj.koordynat_x:
                 print(i.koordynat_x)
                 print(i.koordynat_y)
                 print(obj.koordynat_x)
                 print(obj.koordynat_y)
                 print("b")
                 break
                 
            elif i.koordynat_x< 45 and i.koordynat_x> 5 and i.koordynat_x - 4<=obj.koordynat_x and i.koordynat_y< 45 and i.koordynat_y> 5 and i.koordynat_y + 4>=obj.koordynat_y and i.koordynat_y<= obj.koordynat_y and i.koordynat_x>= obj.koordynat_x:
                 print(i.koordynat_x)
                 print(i.koordynat_y)
                 print(obj.koordynat_x)
                 print(obj.koordynat_y)
                 print("c")
                 break
            elif i.koordynat_x< 45 and i.koordynat_x> 5 and i.koordynat_x + 4>=obj.koordynat_x and i.koordynat_y< 45 and i.koordynat_y> 5 and i.koordynat_y - 4<=obj.koordynat_y and i.koordynat_y>= obj.koordynat_y and i.koordynat_x<= obj.koordynat_x:
                 print(i.koordynat_x)
                 print(i.koordynat_y)
                 print(obj.koordynat_x)
                 print(obj.koordynat_y)
                 print("d")
                 break








def system_ruchu(day_counter,postac,lista_postaci,mapa,addmove,drewno,kamien,zloto,n,p):
     day_counter+=1
     drewno,kamien,zloto = zbieranie_surowce(drewno,zloto,kamien,mapa)
     o = 0
     movementpoints = 10 + addmove

     while movementpoints>0:
        i = True
        while i == True:

 

                wsad = input("\033[0m wasd - ")
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
                                if obj.trudny_teren == True:
                                     movementpoints-=2
                                else:
                                     movementpoints-=1  
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
                                mapa[obj.id],drewno,kamien,zloto = jakabudowla(obj.koordynat_x,obj.koordynat_y,obj.id,mapa,zloto,drewno,kamien)
                                o +=1
                                i = False
                                movementpoints-=1  
                                break
                if wsad == "db":
                        for obj in mapa:
                            if obj.koordynat_x == postac.koordynat_x+1 and obj.koordynat_y == postac.koordynat_y and obj.mozna_budowac == True:
                                mapa[obj.id],drewno,kamien,zloto = jakabudowla(obj.koordynat_x,obj.koordynat_y,obj.id,mapa,zloto,drewno,kamien)
                                i = False
                                o +=1
                                movementpoints-=1  
                                break  
                if wsad == "sb":
                        for obj in mapa:
                            if obj.koordynat_x == postac.koordynat_x and obj.koordynat_y == postac.koordynat_y+1 and obj.mozna_budowac == True:
                                mapa[obj.id],drewno,kamien,zloto = jakabudowla(obj.koordynat_x,obj.koordynat_y,obj.id,mapa,zloto,drewno,kamien)
                                i = False
                                o +=1
                                movementpoints-=1  
                                break
                if wsad == "wb":
                        for obj in mapa:
                            if obj.koordynat_x == postac.koordynat_x and obj.koordynat_y == postac.koordynat_y-1 and obj.mozna_budowac == True:
                                mapa[obj.id],drewno,kamien,zloto = jakabudowla(obj.koordynat_x,obj.koordynat_y,obj.id,mapa,zloto,drewno,kamien)
                                i = False
                                o +=1
                                movementpoints-=1  
                                break
                if wsad == "ae":
                        for obj in mapa:
                            if obj.koordynat_x == postac.koordynat_x-1 and obj.koordynat_y == postac.koordynat_y and obj.interakcja == True:
                                interakcja(obj.koordynat_x,obj.koordynat_y,mapa,len(lista_postaci),lista_postaci,n)
                                o +=1
                                i = False
                                movementpoints-=1  
                                break
                if wsad == "de":
                        for obj in mapa:
                            if obj.koordynat_x == postac.koordynat_x+1 and obj.koordynat_y == postac.koordynat_y and obj.interakcja == True:
                                interakcja(obj.koordynat_x,obj.koordynat_y,mapa,len(lista_postaci),lista_postaci,n)
                                i = False
                                o +=1
                                movementpoints-=1  
                                break  
                if wsad == "se":
                        for obj in mapa:
                            if obj.koordynat_x == postac.koordynat_x and obj.koordynat_y == postac.koordynat_y+1 and obj.interakcja == True:
                                interakcja(obj.koordynat_x,obj.koordynat_y,mapa,len(lista_postaci),lista_postaci,n)
                                i = False
                                o +=1
                                movementpoints-=1  
                                break
                if wsad == "we":
                        for obj in mapa:
                            if obj.koordynat_x == postac.koordynat_x and obj.koordynat_y == postac.koordynat_y-1 and obj.interakcja == True:
                                interakcja(obj.koordynat_x,obj.koordynat_y,mapa,len(lista_postaci),lista_postaci,n)
                                i = False
                                o +=1
                                movementpoints-=1  
                                break
        if movementpoints < 0:
             movementpoints = 0

        print(f"koordynaty - ({postac.koordynat_x,postac.koordynat_y})",f"cycle - {day_counter}",f"action points left - {movementpoints}")
        if day_counter>=1 and day_counter%2==0:
            print("night")
        else:
            print("day")
        print(f"kamien = {kamien}",f"drewno = {drewno}",f"zloto = {zloto}")
        generacjamapy(mapa,lista_postaci,lista_potworow)
        system_ruchu_potwora(lista_potworow,lista_postaci)
     
     
     gen_potworow(mapa,p, lista_potworow)
     return zloto,drewno,kamien,day_counter

# ================================================================================
# ================================================================================
print("mozesz sie poruszac uzywajac wasd")
print(30*"-")
print("w - do gory")
print("s - do dolu")
print("a - w lewo")
print("d - w prawo")
print(30*"-")
print("zeby budowac rzeczy, po napisaniu w ktora strone chcesz zbudowac napisz b (xb gdzie x to w,s,a lub d) ")
print("specyficzne rzeczy mozesz budowac tylko na specyficznym terenie")
print("mozesz rowniez uzywac/interaktowac z specyficznymi rzeczami(teraz tylko miasto) uzywajac podobnego sposobu jak z budowaniem tylko zamiast b uzywajac e")
print(30*"-")
print("(na mapie) A - gora, _ - polana, F - las, H - most, D - drwal, Z - kopalnia zlota, K - kopalnia kamienia, M - miasto, O - twoja postac")
print("(pozniej zrobie rzeczy z dniami i zasobami ale teraz sa bezuzyteczne)")
print("kazda postac ma 10 punktow akcji, przechodzenie przez normalny teren kosztuje 1 tak samo jak budowanie i interakcje, a przechodzenie przez trudny teren kosztuje 2")
print(30*"-")
input("zeby kontunuowac nacisnij enter  ")
print(30*"-")
p = 0

gen_postaci(mapa,n,lista_postaci)
generacjamapy(mapa,lista_postaci,lista_potworow)

while True:
        n=0

        for i in lista_postaci:

            print(f"\033[1;37;40m postac {n+1}")

            zloto,drewno,kamien,day_counter = system_ruchu(day_counter,lista_postaci[n],lista_postaci,mapa,addmove,drewno,kamien,zloto,n,p)
            n+=1
