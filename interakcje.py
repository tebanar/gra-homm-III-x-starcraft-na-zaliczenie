from klasy import*

from generacja import *
from walka import *
from random import randint
def miasto(mapa,n,lista_postaci,zloto,num,lista_kart):
     while True:
          print("jestes w miescie")
          abc = input("gdzie chcesz pojsc?" )
          if abc == "karczma":
               czy_postac = input("czy chcesz nowa postac(500 zlota)?")
               if czy_postac == "tak" and zloto >= 500:
                    zloto-=500

                    gen_postaci(mapa,n,lista_postaci)
          elif abc == "wyjscie":
               break
          elif abc == "sklep"and zloto >= 500:
               czy_postac = input("czy chcesz nowa karte(500 zlota)?")
               if czy_postac == "tak":
                    skrzynia(num,lista_kart)
                    zloto-=500
               print("czy chcesz usunac karte(500 zlota)?")
               for i in num.deck:
                    print(i.nazwa)
               czy_postac = input()
               for i in num.deck:
                    if czy_postac == i.nazwa:
                         num.deck.remove(i)
                         zloto-=500
                         break
     return zloto

                       
     


def skrzynia(postac,lista_kart):
          karty_do_wybrania_rand = []
          karty_do_wybrania = []

          for i in range(3):
               karty_do_wybrania_rand.append(randint(0,len(lista_kart)-1))
          for i in karty_do_wybrania_rand:
               karty_do_wybrania.append(lista_kart[i])
          print(f"1 - {karty_do_wybrania[0].nazwa}")
          print(f"2 - {karty_do_wybrania[1].nazwa}")
          print(f"3 - {karty_do_wybrania[2].nazwa}")
          wybor_karty = input()
          for i in karty_do_wybrania:
               if wybor_karty == i.nazwa:
                    postac.deck.append(i)




def interakcja(koordynat_x,koordynat_y,mapa,n,lista_postaci,num,lista_kart,zloto):
     for obj in mapa:
          if koordynat_x == obj.koordynat_x and koordynat_y == obj.koordynat_y and obj.interakcja == True:
               if obj.jaki_biom == "Miasto":
                    zloto = miasto(mapa,n,lista_postaci,zloto,num,lista_kart)
               elif obj.jaki_biom == "Skrzynia":
                    skrzynia(num,lista_kart)
                    mapa[obj.id] = Plains(obj.koordynat_x,obj.koordynat_y,obj.id)
                    break
     return zloto
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
