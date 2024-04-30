from random import randint
mapa = []
y = 1
x = 0
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
        self.mozna_budowac = True
        super().__init__(x, y, id)
    def drukmapy(self):
            print(" _ ",end="")
    def zmianalinijkimapy(self):
            print(" _ ")

class Mountains(Tiles):
    def __init__(self, x, y,id):
        self.jaki_biom = "Mountains"
        self.mozna_budowac = False
        super().__init__(x, y,id)
    def drukmapy(self):
            print(" A ",end="")
    def zmianalinijkimapy(self):
            print(" A ")
class Jednostka(Tiles):
     def __init__(self, x, y, id):
          super().__init__(x, y, id)
     def drukjednostki(self):
            print(" O ",end="")
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

def gen_postaci(mapa):
    q = 0
    while q == 0:
        c = randint(2,49)
        b = randint(2,49)
        for i in mapa:
            if c == i.koordynat_x and b == i.koordynat_y and i.jaki_biom == "Plains":
                q+=1
                return c,b
            else:continue
         
c,b = gen_postaci(mapa)        
         
obj1 = Jednostka(c,b  ,1)
c,b = gen_postaci(mapa)  
obj2 = Jednostka(c,b  ,1)
lista_postaci = [obj1,obj2]
for i in range(20):

     n = 0
     for obj in mapa:


        mapa[n] = generacja_gor(obj,mapa,n)

        n+=1



def generacjamapy(mapa,lista_postaci):
    n = 1
    for obj in mapa:
        for i in lista_postaci:
            if obj.koordynat_y == i.koordynat_y and obj.koordynat_x == i.koordynat_x:
                i.drukjednostki()
                
        if obj.koordynat_y == i.koordynat_y and obj.koordynat_x == i.koordynat_x:
             continue
        elif obj.koordynat_y == n:
                obj.drukmapy()
        elif obj.koordynat_y != n:
                obj.zmianalinijkimapy()
                n += 1


generacjamapy(mapa,lista_postaci)



def system_ruchu(wsadczyxy,day_counter,postac,lista_postaci):
     day_counter+=1
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
                        if obj.koordynat_x == postac.koordynat_x-1 and obj.koordynat_y == postac.koordynat_y and obj.mozna_budowac == True:
                            postac.replacex(postac.koordynat_x-1)
                            i = False
                            break
             if wsad == "d":
                    for obj in mapa:
                        if obj.koordynat_x == postac.koordynat_x+1 and obj.koordynat_y == postac.koordynat_y and obj.mozna_budowac == True:
                            postac.replacex(postac.koordynat_x+1)
                            i = False  
                            break  
             if wsad == "s":
                    for obj in mapa:
                        if obj.koordynat_x == postac.koordynat_x and obj.koordynat_y == postac.koordynat_y+1 and obj.mozna_budowac == True:
                            postac.replacey(postac.koordynat_y+1)
                            i = False
                            break
             if wsad == "w":
                    for obj in mapa:
                        if obj.koordynat_x == postac.koordynat_x and obj.koordynat_y == postac.koordynat_y-1 and obj.mozna_budowac == True:
                            postac.replacey(postac.koordynat_y-1)
                            i = False
                            break

     print(postac.koordynat_x,postac.koordynat_y)
     generacjamapy(mapa,lista_postaci)
print("wybierz koordynaty x i y")

print("koordynaty czy wasd?")
wsadczyxy = input()
while True:
    print("postac 1")
    system_ruchu(wsadczyxy,day_counter,obj1,lista_postaci)
    print("postac 2")
    system_ruchu(wsadczyxy,day_counter,obj2,lista_postaci)