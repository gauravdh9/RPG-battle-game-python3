import random
from .magic import Spell
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self,name,hp,mp,attk,df,magic,items):
        self.maxhp=hp
        self.hp=hp
        self.maxmp=mp
        self.mp=mp
        self.attkl=attk-10
        self.attkh=attk+10
        self.df=df
        self.actions=["Attack","Magic","Items"]
        self.magic=magic
        self.items=items
        self.name=name

    def generate_damage(self):
        return random.randrange(self.attkl,self.attkh)

    def take_damage(self,dmg):
        self.hp-=dmg
        if self.hp<0:
            self.hp=0
        return self.hp

    def heal(self,dmg):
        self.hp+=dmg
        if self.hp>self.maxhp:
            self.hp=self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self,cost):
        self.mp -= cost

    def choose_actions(self):
        i = 1
        print("\n"+"    "+bcolors.BOLD+self.name+bcolors.ENDC)
        print(bcolors.OKBLUE+bcolors.BOLD+"    ACTIONS:"+bcolors.ENDC)
        for item in self.actions:
            print("     "+str(i)+"."+item)
            i += 1

    def choose_magic(self):
        i=1
        print(bcolors.OKBLUE+bcolors.BOLD+"MAGIC:"+bcolors.ENDC)
        for spell in self.magic:
            print("     "+str(i)+".",spell.name,"(cost:",str(spell.cost)+ ")")
            i += 1
    def choose_item(self):
        i=1
        print(bcolors.OKBLUE+bcolors.BOLD+"ITEMS:"+bcolors.ENDC)
        for item in self.items:
            print("     "+str(i)+".",str(item["item"].name),":",str(item["item"].description),"quantity:"+str(item["quantity"]))
            i+=1
    def choose_target(self,enemies):
        i=1
        print(bcolors.FAIL + bcolors.BOLD + "TARGET:" + bcolors.ENDC)
        for enemy in enemies:
            if enemy.get_hp()!=0:
                print("     " + str(i) + ".", enemy.name)
                i+=1
        choice=int(input("Choose Enemy to attack:"))-1
        return choice
    def get_enemy_stats(self):
        enemyhp_ticks=(self.hp/self.maxhp)*50
        enemyhp_bar="█"*int(enemyhp_ticks)
        while len(enemyhp_bar)<50:
            enemyhp_bar+=" "
        enemyhp_string=str(self.hp)+"/"+str(self.maxhp)
        enemycurrent_hp=""
        if len(enemyhp_string)<11:
            decreased=11-len(enemyhp_string)
            enemycurrent_hp=" "*decreased
            enemycurrent_hp+=enemyhp_string
        else:
            enemycurrent_hp=enemyhp_string
        spaces=(20-len(self.name))*" "
        print("                                  __________________________________________________")
        print(bcolors.BOLD+self.name+":"+spaces+enemycurrent_hp+bcolors.FAIL+" |"+enemyhp_bar+"|        "+bcolors.ENDC+bcolors.BOLD+bcolors.ENDC)

    def get_stats(self):
        hp_ticks = (self.hp/self.maxhp)*25
        mp_ticks = (self.mp/self.maxmp)*10
        mp_bar = "█"*int(mp_ticks)
        hp_bar = "█"*int(hp_ticks)
        while len(hp_bar)<25:
            hp_bar+=" "
        while  len(mp_bar)<10:
            mp_bar+=" "
        hp_string=str(self.hp)+"/"+str(self.maxhp)
        current_hp=""
        if len(hp_string)<9:
            decreased=9-len(hp_string)
            current_hp=" "*decreased
            current_hp+=hp_string
        else:
            current_hp=hp_string
        mp_string=str(self.mp)+"/"+str(self.maxmp)
        current_mp=""
        if len(mp_string)<7:
            dec=7-len(mp_string)
            current_mp=" "*dec
            current_mp+=mp_string
        else:
            current_mp=mp_string
        spaces=(20-len(self.name))*" "
        print("                                _________________________                  __________")
        print(bcolors.BOLD+self.name+":"+spaces+current_hp+bcolors.OKGREEN+" |"+hp_bar+"|        "+bcolors.ENDC+bcolors.BOLD+current_mp+bcolors.OKBLUE+" |"+mp_bar+"|"+bcolors.ENDC)