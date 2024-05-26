from klasy import*
from ruch import *
from interakcje import *
from walka import *
from random import randint

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
                for i in range(5):
                    obj.deck.append(Attack_card("Attack",1,False,7,False,False,"strike",0))
                    obj.deck.append(Skill_card("Skill",1,False,False,0,0,7,False,False,"block"))

                for i in obj.deck:
                         print(i.nazwa)
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
def gen_boss(mapa,n, lista_potworow):
    
    q = 0
    while q == 0:
        x = randint(2,48)
        y = randint(2,48)

        for i in mapa:
            if i.mozna_chodzic == True and x == i.koordynat_x and y == i.koordynat_y:
                q+=1
                n+=1
                print(i.koordynat_x,i.koordynat_y,n)
                obj = Boss(i.koordynat_x,i.koordynat_y,n)
                lista_potworow.append(obj)
                return lista_potworow
            else:continue


def generowanie_postaci_na_mapie(lista_postaci,obj):

    for i in lista_postaci:
        if obj.koordynat_y == i.koordynat_y and obj.koordynat_x == i.koordynat_x and obj.koordynat_x>0:


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
    e = 0
    p = 0
    for obj in mapa:

        if generowanie_postaci_na_mapie(lista_postaci,obj):
             for i in lista_postaci:
                  if obj.koordynat_x == i.koordynat_x and obj.koordynat_y == i.koordynat_y:
                    i.drukjednostki()
             e+=1
        elif generowanie_potworow_na_mapie(lista_potworow,obj):
             for i in lista_potworow:
                  if obj.koordynat_x == i.koordynat_x and obj.koordynat_y == i.koordynat_y:
                    i.drukjednostki()
                       
             p+=1

                

        elif obj.koordynat_y == n:
                obj.drukmapy()
        elif obj.koordynat_y != n:
                obj.zmianalinijkimapy()
                n += 1