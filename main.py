from random import randint
from klasy import *
from ruch import *
from generacja import *
from interakcje import *
from walka import *

# =============================================================================

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
        elif a >= 21 and a<= 22:
             tile = Skrzynia(x,y,i)

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
abc = 0
while True:
        n=0

        for i in lista_postaci:

            print(f"\033[1;37;40m postac {n+1}")

            zloto,drewno,kamien,day_counter = system_ruchu(day_counter,lista_postaci[n],lista_postaci,mapa,addmove,drewno,kamien,zloto)
            n+=1
            abc +=1
            gen_potworow(mapa,p, lista_potworow)
            if abc == 3:
             gen_boss(mapa,p, lista_potworow)
            for i in lista_potworow:
                print(i.jaki_biom)