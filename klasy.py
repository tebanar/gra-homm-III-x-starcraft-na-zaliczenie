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
          self.deck = []
          self.max_hp = 100
          self.hp = self.max_hp
          self.obrona = 0
          super().__init__(x, y, id)
     def drukjednostki(self):
            print("\033[1;31;40m O ",end="")
     def replacex(self,x):
          self.koordynat_x = x
     def replacey(self,y):
          self.koordynat_y = y
     def take_damage(self,damage):
          self.hp -= damage
     def bronienie(self,shield):
          self.obrona += shield
     def atack_na_tarcze(self,atak):
          self.obrona -= atak
     def reset_obrony(self):
          self.obrona = 0
class Przeciwnik(Tiles):
     def __init__(self, x, y, id):
        self.jaki_biom = "Przeciwnik"
        self.mozna_budowac = False
        self.mozna_chodzic = False
        self.generation = False
        self.trudny_teren = False
        self.max_hp = 100
        self.hp = self.max_hp
        self.obrona = 0
        self.atak_potwora = 10
        super().__init__(x, y, id)
     def drukjednostki(self):
            print("\033[1;36;40m P ",end="")
     def replacex(self,x):
          self.koordynat_x = x
     def replacey(self,y):
          self.koordynat_y = y
     def take_damage(self,damage):
          self.hp -= damage
     def bronienie(self,shield):
          self.obrona += shield
     def atack_na_tarcze(self,atak):
          self.obrona -= atak
     def reset_obrony(self):
          self.obrona = 0
class Boss(Tiles):
     def __init__(self, x, y, id):
        self.jaki_biom = "Boss"
        self.mozna_budowac = False
        self.mozna_chodzic = False
        self.generation = False
        self.trudny_teren = False
        self.max_hp = 300
        self.hp = self.max_hp
        self.obrona = 0
        self.atak_potwora = 20
        super().__init__(x, y, id)
     def drukjednostki(self):
            print("\033[1;31;40m B ",end="")
     def replacex(self,x):
          self.koordynat_x = x
     def replacey(self,y):
          self.koordynat_y = y
     def take_damage(self,damage):
          self.hp -= damage
     def bronienie(self,shield):
          self.obrona += shield
     def atack_na_tarcze(self,atak):
          self.obrona -= atak
     def reset_obrony(self):
          self.obrona = 5
class Karta():
     def __init__(self,typ,koszt,exhaustion,nazwa) -> None:
          self.jaki_typ = typ
          self.koszt = koszt
          self.exhaust = exhaustion
          self.nazwa = nazwa

class Attack_card(Karta):
     def __init__(self, typ, koszt, exhaustion,damage,weakness,vulnerable,nazwa,specjalny_stat) -> None:
          self.damage = damage
          self.debuff_weak = weakness
          self.debuff_vuln = vulnerable
          self.specjalny = specjalny_stat

          super().__init__(typ, koszt, exhaustion,nazwa)
     def zmiana_ataku(self,damage):
          self.damage += damage
class Skill_card(Karta):
     def __init__(self, typ, koszt, exhaustion,cure, draw,energy,block,weakness,vulnerable,nazwa) -> None:
          self.cure = cure
          self.draw = draw
          self.energy_gain = energy
          self.block = block
          self.debuff_weak = weakness
          self.debuff_vuln = vulnerable


          super().__init__(typ, koszt, exhaustion,nazwa)



class Power_card(Karta):
     def __init__(self, typ,koszt, nazwa,exhaustion,strength,dexterity,barricade,energy) -> None:
          self.add_strength = strength
          self.add_dex = dexterity
          self.barricade = barricade

          self.energy_gain = energy



     
          super().__init__(typ,koszt,exhaustion,nazwa)
