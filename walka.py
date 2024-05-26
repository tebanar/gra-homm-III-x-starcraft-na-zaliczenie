from klasy import*
from ruch import *

from random import randint
def atak_potwora(potwor,postac,lista_kart):



     strength = 0
     energy_gain = 0
     dex = 0
     double = 1
     draw_pile = []
     for i in postac.deck:
          draw_pile.append(i)
     hand = []
     discard_pile = []
     postac_vulnerable = False
     postac_weakness = False
     barricade = False
     while potwor.hp>0 and postac.hp>0:
        barricade == False
        vulnerable = False
        weakness = False
        wybor_karty = ""
        energia = 3 + energy_gain
        print(f"gracz - {postac.hp}/{postac.max_hp}hp, {postac.obrona}tarczy"),print(f"potwor - {potwor.hp}/{potwor.max_hp}hp, {potwor.obrona}tarczy")
        for i in range(6):
             if len(draw_pile)-1 == 0:
                  for i in discard_pile:
                       draw_pile.append(i)
                  discard_pile = []     
             karta = randint(0,len(draw_pile)-1) 
             hand.append(draw_pile[karta])
             draw_pile.pop(karta)
        akcja_potwora = randint(1,2)
        if akcja_potwora == 1:
             print("potwor cie atakuje")
             jaki_atak = randint(1,3)
             if jaki_atak == 1:
                  print(f"potwor cie atakuje za {potwor.atak_potwora/2}x2")
             if jaki_atak == 2:
                  print(f"potwor cie atakuje za {potwor.atak_potwora}")
             elif jaki_atak == 3:
                  print(f"potwor cie atakuje za {potwor.atak_potwora*1.5}")

        elif akcja_potwora == 2:
             print("potwor broni sie")
        while wybor_karty!="koniec tury":
          print(f"gracz - {postac.hp}/{postac.max_hp}hp, {postac.obrona}tarczy"),print(f"potwor - {potwor.hp}/{potwor.max_hp}hp, {potwor.obrona}tarczy")
          print("twoja reka to:")
          for i in hand:
                    print(i.nazwa)
          print(f"energia = {energia}")
          wybor_karty = input("jaką karte chcesz uzyc ")
          for karta in hand:
                 if karta.nazwa == wybor_karty and karta.koszt <= energia:
                      if karta.exhaust == True:
                           hand.remove(karta)
                      elif karta.exhaust == False:
                         discard_pile.append(karta)
                         hand.remove(karta)
                      energia -= karta.koszt
                      if karta.jaki_typ == "Attack":
                       for i in range(double):
                       


                         print("atakujesz potwora")
                         if vulnerable == True and postac_weakness == True:
                              potwor.atack_na_tarcze(karta.damage + strength * 1.2)
                         elif vulnerable == True:
                              potwor.atack_na_tarcze(karta.damage + strength * 1.5)
                         elif postac_weakness == True:
                              potwor.atack_na_tarcze(karta.damage + strength * 0.75)
                         else: 
                              potwor.atack_na_tarcze(karta.damage + strength)

                         if potwor.obrona<0:
                              potwor.take_damage(-potwor.obrona)       

                         if karta.debuff_weak == True:
                              weakness = True
                         if karta.debuff_vuln == True:
                              vulnerable = True
                         if karta.nazwa == "rampage":
                              karta.zmiana_ataku(3)
                         if karta.specjalny != 0:
                              if karta.nazwa == "feed":
                                   if potwor.hp <= 0:
                                        postac.max_hp += karta.specjalny
                                        postac.hp += karta.specjalny
                              if karta.nazwa == "bounce back":
                                   for i in range(karta.specjalny):
                                        if len(draw_pile)-1 == 0:
                                             for i in discard_pile:
                                                  draw_pile.append(i)
                                             discard_pile = []     
                                        nowa_karta = randint(0,len(draw_pile)-1) 
                                        hand.append(draw_pile[nowa_karta])
                                        draw_pile.pop(nowa_karta)  
                              if karta.nazwa == "hemokinesis":
                                   postac.take_damage(karta.specjalny)
                         if double != 1:
                                        double -= 1   
                      elif karta.jaki_typ == "Skill":
                           print("uzywasz skilla")
                           postac.bronienie(karta.block+dex)
                           if karta.nazwa == "spot weakness":
                                strength += karta.draw
                           else:
                                for i in range(karta.draw):
                                   if len(draw_pile)-1 == 0:
                                        for i in discard_pile:
                                             draw_pile.append(i)
                                        discard_pile = []     
                                   nowa_karta = randint(0,len(draw_pile)-1) 
                                   hand.append(draw_pile[nowa_karta])
                                   draw_pile.pop(nowa_karta)    
                           energia += karta.energy_gain  
                           if karta.cure == True:
                                if karta.nazwa == "double tap":
                                     double +=1      
                                else:
                                     postac_vulnerable == False      
                                     postac_weakness == False  
                           if karta.nazwa == "blood letting":
                                postac.take_damage(karta.specjalny)
                      elif karta.jaki_typ == "Power":
                           energy_gain += karta.energy_gain
                           strength+= karta.energy_gain
                           dex+=karta.add_dex
                           if karta.barricade == True:
                              barricade == True

                      

                              


                      break
          if wybor_karty == "draw pile":
               for i in draw_pile:
                    print(i.nazwa)
          if wybor_karty == "discard pile":
               for i in discard_pile:
                    print(i.nazwa)
          if potwor.obrona < 0 :
               potwor.reset_obrony()
        potwor.reset_obrony()


        if akcja_potwora == 1:
             print("potwor cie atakuje")
             if jaki_atak == 1 and weakness == True:
                  print(f"potwor cie atakuje za {potwor.atak_potwora/2*0.8}x2 i uwrazliwia cie(?)")
                  postac.atack_na_tarcze(potwor.atak_potwora*0.8)
                  postac_vulnerable == True
             elif jaki_atak == 2 and weakness == True:
                  print(f"potwor cie atakuje za {potwor.atak_potwora*0.8} i oslabia cie")
                  postac.atack_na_tarcze(potwor.atak_potwora*0.8)
                  postac_weakness = True
             elif jaki_atak == 3 and weakness == True:
                  print(f"potwor cie atakuje za {potwor.atak_potwora*1.5*0.8}")
                  postac.atack_na_tarcze(potwor.atak_potwora*1.5*0.8)
             elif jaki_atak == 1:
                  print(f"potwor cie atakuje za {potwor.atak_potwora/2}x2 i uwrazliwia cie")
                  postac.atack_na_tarcze(potwor.atak_potwora)
                  postac_vulnerable == True
             elif jaki_atak == 2 :
                  print(f"potwor cie atakuje za {potwor.atak_potwora} i oslabia cie")
                  postac.atack_na_tarcze(potwor.atak_potwora)
                  postac_weakness = True
             elif jaki_atak == 3 :
                  print(f"potwor cie atakuje za {potwor.atak_potwora*1.5}")
                  postac.atack_na_tarcze(potwor.atak_potwora*1.5)
             if postac.obrona<0:
                  postac.take_damage(-postac.obrona)
        elif akcja_potwora == 2:
             print("potwor broni sie")
             potwor.bronienie(randint(8,13))
          






        if barricade == True:
             continue
        elif barricade == False:
             postac.reset_obrony()

        for i in hand:
             discard_pile.append(i)


        hand = []
        for i in discard_pile:
          print(i.nazwa)
     if postac.hp>0:
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
