from klasy import *
from interakcje import *
from walka import *
from walka import atak_potwora
from generacja import zbieranie_surowce
from generacja import *
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
lista_kart1 = [Power_card("Power",2,"berserk",True,3,-1,False,0),Power_card("Power",1,"fortification",True,0,1,True,0),Power_card("Power",3,"corruption",True,3,3,False,0),Power_card("Power",2,"inner peace",True,-1,-1,False,1),Skill_card("Skill",1,False,False,0,0,5,False,False,"block")]
dodatkowa_lista_skill = [Skill_card("Skill",2,False,False,1,0,12,False,False,"barrier"),Skill_card("Skill",1,True,True,0,0,0,True,True,"curse"),Skill_card("Skill",0,False,False,0,2,0,False,False,"bloodletting"),Skill_card("Skill",1,False,False,3,0,0,False,False,"trance")]
dodatkowa_lista_skill2 = [Skill_card("Skill",1,True,False,0,2,6,False,False,"sentinel"),Skill_card("Skill",1,False,False,2,0,0,False,True,"spot weakness"),Skill_card("Skill",1,False,True,0,0,0,False,False,"double tap"),Skill_card("Skill",1,False,False,1,0,7,False,False,"sneak")]
dodatkowa_lista_attack = [Attack_card("Attack",1,False,10,False,False,"feed",5),Attack_card("Attack",2,False,21,False,False,"carnage",0),Attack_card("Attack",1,False,7,False,False,"bounce back",1),Attack_card("Attack",1,False,7,False,False,"strike",0)]
dodatkowa_lista_attack2 = [Attack_card("Attack",2,False,10,True,True,"uppercut",0),Attack_card("Attack",0,True,0,True,True,"scream",0),Attack_card("Attack",1,False,5,False,False,"rampage",0),Attack_card("Attack",1,False,18,False,False,"hemokinesis",5),Attack_card("Attack",1,False,15,False,False,"perfect strike",0)]

for i in dodatkowa_lista_skill:
     lista_kart1.append(i)
for i in dodatkowa_lista_skill2:
     lista_kart1.append(i)
for i in dodatkowa_lista_attack:
     lista_kart1.append(i)
for i in dodatkowa_lista_attack2:
     lista_kart1.append(i)
lista_kart = lista_kart1
def system_ruchu(day_counter,postac,lista_postaci,mapa,addmove,drewno,kamien,zloto):
     
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
                                zloto = interakcja(obj.koordynat_x,obj.koordynat_y,mapa,len(lista_postaci),lista_postaci,postac,lista_kart,zloto)
                                o +=1
                                i = False
                                movementpoints-=1  
                                break
                if wsad == "de":
                        for obj in mapa:
                            if obj.koordynat_x == postac.koordynat_x+1 and obj.koordynat_y == postac.koordynat_y and obj.interakcja == True:
                                zloto = interakcja(obj.koordynat_x,obj.koordynat_y,mapa,len(lista_postaci),lista_postaci,postac,lista_kart,zloto)
                                i = False
                                o +=1
                                movementpoints-=1  
                                break  
                if wsad == "se":
                        for obj in mapa:
                            if obj.koordynat_x == postac.koordynat_x and obj.koordynat_y == postac.koordynat_y+1 and obj.interakcja == True:
                                zloto = interakcja(obj.koordynat_x,obj.koordynat_y,mapa,len(lista_postaci),lista_postaci,postac,lista_kart,zloto)
                                i = False
                                o +=1
                                movementpoints-=1  
                                break
                if wsad == "we":
                        for obj in mapa:
                            if obj.koordynat_x == postac.koordynat_x and obj.koordynat_y == postac.koordynat_y-1 and obj.interakcja == True:
                                zloto = interakcja(obj.koordynat_x,obj.koordynat_y,mapa,len(lista_postaci),lista_postaci,postac,lista_kart,zloto)
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
        system_ruchu_potwora(lista_potworow,lista_postaci,mapa)
        generacjamapy(mapa,lista_postaci,lista_potworow)
     
        for potwor in lista_potworow:
               for postac in lista_postaci:
                    if potwor.koordynat_x == postac.koordynat_x and potwor.koordynat_y == postac.koordynat_y:
                         print(potwor.koordynat_x,postac.koordynat_x,potwor.koordynat_y,postac.koordynat_y)
                         atak_potwora(potwor,postac,lista_kart)
                         if postac.hp<=0:
                              lista_postaci.remove(postac)
                         elif potwor.hp <= 0:
                              lista_potworow.remove(potwor)
     return zloto,drewno,kamien,day_counter



def system_ruchu_potwora(lista_potworow,lista_postaci,mapa):
     for i in lista_potworow:
          for obj in lista_postaci:
            if i.koordynat_x< 49 and i.koordynat_x> 5 and i.koordynat_x + 4>=obj.koordynat_x and i.koordynat_y< 49 and i.koordynat_y> 5 and i.koordynat_y + 4>=obj.koordynat_y and i.koordynat_y<= obj.koordynat_y and i.koordynat_x<= obj.koordynat_x:
                print("B")                
                for tile in mapa:
                    if obj.koordynat_x==i.koordynat_x and i.koordynat_y==obj.koordynat_y:
                      break
                    elif obj.koordynat_x-i.koordynat_x >= obj.koordynat_y-i.koordynat_y and tile.koordynat_x == i.koordynat_x+1 and tile.koordynat_y == i.koordynat_y and tile.mozna_chodzic == True:

                        i.replacex(i.koordynat_x+1)
                        break
                    elif obj.koordynat_x-i.koordynat_x <= obj.koordynat_y-i.koordynat_y and tile.koordynat_y == i.koordynat_y+1 and tile.koordynat_x == i.koordynat_x and tile.mozna_chodzic == True:

                        i.replacey(i.koordynat_y+1)
                        break

                break
            
            elif i.koordynat_x< 49 and i.koordynat_x> 5 and i.koordynat_x - 4 <=obj.koordynat_x and i.koordynat_y< 49 and i.koordynat_y> 5 and i.koordynat_y - 4<=obj.koordynat_y and i.koordynat_y>= obj.koordynat_y and i.koordynat_x>= obj.koordynat_x:
                print("a")
                for tile in mapa:
                 if obj.koordynat_x==i.koordynat_x and i.koordynat_y==obj.koordynat_y:
                      break
                 elif i.koordynat_x-obj.koordynat_x >= i.koordynat_y-obj.koordynat_y and tile.koordynat_x == i.koordynat_x-1 and tile.koordynat_y == i.koordynat_y and tile.mozna_chodzic == True:
                      

                      i.replacex(i.koordynat_x-1)
                      break
                 elif i.koordynat_x-obj.koordynat_x <= i.koordynat_y-obj.koordynat_y and tile.koordynat_y == i.koordynat_y-1 and tile.koordynat_x == i.koordynat_x and tile.mozna_chodzic == True:

                      i.replacey(i.koordynat_y-1)
                      break

                break
                 
            elif i.koordynat_x< 49 and i.koordynat_x> 5 and i.koordynat_x - 4<=obj.koordynat_x and i.koordynat_y< 49 and i.koordynat_y> 5 and i.koordynat_y + 4>=obj.koordynat_y and i.koordynat_y<= obj.koordynat_y and i.koordynat_x>= obj.koordynat_x:
                print("c")
                for tile in mapa:
                 if obj.koordynat_x==i.koordynat_x and i.koordynat_y==obj.koordynat_y:
                      break
                 elif i.koordynat_x-obj.koordynat_x >= obj.koordynat_y-i.koordynat_y and tile.koordynat_x == i.koordynat_x-1 and tile.koordynat_y == i.koordynat_y and tile.mozna_chodzic == True:

                      i.replacex(i.koordynat_x-1)
                      break
                 elif i.koordynat_x-obj.koordynat_x <= obj.koordynat_y-i.koordynat_y and tile.koordynat_y == i.koordynat_y+1 and tile.koordynat_x == i.koordynat_x and tile.mozna_chodzic == True:

                      i.replacey(i.koordynat_y+1)
                      break

                break
            elif i.koordynat_x< 49 and i.koordynat_x> 5 and i.koordynat_x + 4>=obj.koordynat_x and i.koordynat_y< 49 and i.koordynat_y> 5 and i.koordynat_y - 4<=obj.koordynat_y and i.koordynat_y>= obj.koordynat_y and i.koordynat_x<= obj.koordynat_x:
                print("d")
                for tile in mapa:
                 if obj.koordynat_x==i.koordynat_x and i.koordynat_y==obj.koordynat_y:
                      break
                 elif obj.koordynat_x-i.koordynat_x >= i.koordynat_y-obj.koordynat_y and tile.koordynat_x == i.koordynat_x+1 and tile.koordynat_y == i.koordynat_y and tile.mozna_chodzic == True:

                      i.replacex(i.koordynat_x+1)
                      break
                 elif obj.koordynat_x-i.koordynat_x <= i.koordynat_y-obj.koordynat_y and tile.koordynat_y == i.koordynat_y-1 and tile.koordynat_x == i.koordynat_x and tile.mozna_chodzic == True:

                      i.replacey(i.koordynat_y-1)
                      break

                break
