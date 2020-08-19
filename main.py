from battle.classes.game import Person,bcolors
from battle.classes.magic import Spell
from battle.classes.inventory import Item
import random
from time import sleep
#Create black magic
fire=Spell("Fire",15,200,"black")
thunder=Spell("Thunder",20,250,"black")
blizzard=Spell("Blizzard",10,120,"black")
meteor=Spell("Meteor",13,150,"black")
quake=Spell("Quake",10,140,"black")


#Create White Magic

cure=Spell("Cure",12,120,"white")
cura=Spell("Cura",10,100,"black")

#Create Some items
potion=Item("Potion","potion","Heals 50 HP",50)
hipotion=Item("Hipotion","potion","Heals 100 HP",100)
superpotion=Item("Super Potion","potion","Heals 500 HP",500)
elixir=Item("Elixir","elixir","Fully restores HP/MP of one party's member",9999)
hiElixir=Item("MegaElixir","elixir","Fully restores party's HP/MP",9999)

grenade=Item("Grenade","attack","Deals 500 damage",500)

#instantiate person and enemy with magic
player_spells=[fire,thunder,blizzard,meteor,quake,cure,cura]
enemy_spells=[fire,meteor,blizzard,cure]
player_items=[{"item":potion,"quantity":5},{"item":hipotion,"quantity":15}
       ,{"item":superpotion,"quantity":5},{"item":elixir,"quantity":10},{"item":hiElixir,"quantity":10}
       ,{"item":grenade,"quantity":5}]
player1=Person("Gaurav",3460,160,200,35,player_spells,player_items)
player2=Person("Gaurav",4460,130,300,35,player_spells,player_items)
player3=Person("Gaurav",2460,140,400,35,player_spells,player_items)
#enemies
enemy1=Person("Thanos",11500,65,250,25,enemy_spells,[])
enemy2=Person("Ego",11500,65,450,25,enemy_spells,[])
enemy3=Person("Ronan",11500,65,350,25,enemy_spells,[])
enemy4=Person("Ronan",11500,65,350,25,enemy_spells,[])

players=[player1,player2,player3]
enemies=[enemy1,enemy2,enemy3,enemy4]
running=True
i=0

print(bcolors.FAIL+bcolors.BOLD+"***************************Welcome to My RPG GAME********************************"+bcolors.ENDC)

while running:
       print("*************************************Battle**************************************")
       print("\n")
       for i in range(1,len(enemies)+1):

              print(bcolors.BOLD+bcolors.OKBLUE+"---------------------------------------Round",i,"---------------------------------------"+bcolors.ENDC)
              print("Name:                                      HP                                  MP")

              for player in players:
                     player.get_stats()
              print("\n")
              for enemy in enemies:
                     enemy.get_enemy_stats()
              for player in players:
                     player.choose_actions()
                     choice=input("Choose Action:")
                     index=int(choice)-1

                     if index==0:
                            dmg=player.generate_damage()
                            enemy=player.choose_target(enemies)
                            enemies[enemy].take_damage(dmg)
                            print("\n")
                            print("You Attacked "+enemies[enemy].name,"for", dmg,"points of damage")
                            if enemies[enemy].get_hp()==0:
                                   print(enemies[enemy].name+"has died")
                                   del enemies[enemy]
                     elif index==1:
                            player.choose_magic()
                            magic_choice=int(input("Choose Magic:"))-1
                            if magic_choice==-1:
                                   continue
                            spell=player.magic[magic_choice]
                            magic_dmg=spell.generate_spell_damage()
                            current_mp=player.get_mp()

                            if spell.cost>current_mp:
                                   print(bcolors.FAIL+"\nNOT ENOUGH MP\n"+bcolors.ENDC)
                                   continue
                            player.reduce_mp(spell.cost)
                            if spell.type=="white":
                                   player.heal(magic_dmg)
                                   print(bcolors.OKBLUE+"\n"+spell.name+"heals for",str(magic_dmg),"HP."+bcolors.ENDC)
                            elif spell.type=="black":
                                   enemy = player.choose_target(enemies)
                                   enemies[enemy].take_damage(magic_dmg)
                                   print(bcolors.OKBLUE+"\n"+spell.name,"deals",str(magic_dmg),"points of damage to",enemies[enemy].name+bcolors.ENDC)
                                   if enemies[enemy].get_hp() == 0:
                                          print(enemies[enemy].name + "has died")
                                          del enemies[enemy]

                     elif index==2:
                            player.choose_item()
                            item_choice=int(input("Choose item:"))-1
                            item=player.items[item_choice]
                            if item["quantity"]==0:
                                   print(bcolors.FAIL+"\n"+"None...Left"+bcolors.ENDC)
                                   continue
                            item["quantity"]-=1
                            if item_choice==-1:
                                   continue

                            if item["item"].type=="potion":
                                   player.heal(item["item"].prop)
                                   print(bcolors.OKGREEN+"\n"+item["item"].name,"heals for",str(item["item"].prop),"HP"+bcolors.ENDC)
                            elif item["item"].type=="elixir":
                                   if item["item"].name=="MegaElixir":
                                          for i in players:
                                                 i.hp=i.maxhp
                                                 i.mp=i.maxmp
                                   else:
                                          player.hp=player.maxhp
                                          player.mp=player.maxmp
                                   print(bcolors.OKBLUE+"\n"+item["item"].name+" fully restored HP/MP"+bcolors.ENDC)
                            elif item["item"].type=="attack":
                                   enemy = player.choose_target(enemies)
                                   enemies[enemy].take_damage(item["item"].prop)
                                   print(bcolors.FAIL+"\n"+"💣💣💣💣💣"+item["item"].name,"deals",str(item["item"].prop),"point of damage to",enemies[enemy].name,"💣💣💣💣💣"+bcolors.ENDC)
                                   if enemies[enemy].get_hp() == 0:
                                          print("\n")
                                          print(enemies[enemy].name ,"has died")
                                          del enemies[enemy]

              defeated_enemies=0
              defeated_players=0
              for enemy in enemies:
                     if enemy.get_hp()==0:
                            defeated_enemies+=1
              for player in players:
                     if player.get_hp()==0:
                            defeated_players+=1

              if defeated_enemies==2:
                     print(bcolors.OKGREEN+"****Your Team won!****"+bcolors.ENDC)
                     running=False
              elif defeated_players==2:
                     print(bcolors.FAIL+"****Your Enemies have defated you****"+bcolors.ENDC)
                     running=False

              for enemy in enemies:
                     enemy_Choice=random.randrange(0,2)
                     enemy_damage = enemy.generate_damage()
                     target = random.randrange(0, 3)
                     if enemy_Choice==0:

                            players[target].take_damage(enemy_damage)
                            print("\n")
                            print(enemy.name,"Attcks",players[target].name," for ",enemy_damage)
                     elif enemy_Choice==1:
                            spellchoice=random.randrange(0,len(enemy_spells))
                            spell = enemy.magic[spellchoice]
                            magic_dmg = spell.generate_spell_damage()
                            current_mp = enemy.get_mp()
                            if spell.cost > current_mp:
                                   print(bcolors.FAIL +enemy.name +"\nNOT HAVE ENOUGH MP\n" + bcolors.ENDC)
                                   continue
                            enemy.reduce_mp(spell.cost)
                            if spell.type == "white":
                                   enemy.heal(magic_dmg)
                                   print(bcolors.OKBLUE + "\n" + spell.name , "heals",enemy.name ,"for", str(magic_dmg),
                                         "HP." + bcolors.ENDC)
                            elif spell.type == "black":
                                   target = random.randrange(0, 3)
                                   players[target].take_damage(magic_dmg)
                                   print(bcolors.OKBLUE + "\n" + spell.name , "deals", str(magic_dmg),
                                         "points of damage to " + players[target].name + bcolors.ENDC)
                                   if players[target].get_hp() == 0:
                                          print(players[target].name , "has died")
                                          del players[target]

              print("Next Round will start in couple of Seconds, Get Ready")
              sleep(5)
