from playsound3 import playsound
import random
import time

from win32con import MIIM_CHECKMARKS
entrancecount=0
firstbrute=False
wallcount=int(3)
global MapGame, lab ,tunnel, HP
MapGame = False

lab = [["w", "e", "e", "e", "e", "e", "e", "e", "w"],
       ["w", "f", "f", "f", "f", "f", "f", "f", "w"],
       ["w", "f", "f", "f", "f", "f", "f", "f", "w"],
       ["w", "f", "f", "f", "f", "f", "f", "f", "w"],
       ["w", "f", "f", "sh", "f", "f", "f", "f", "w"],
       ["w", "f", "f", "f", "f", "sh", "f", "f", "w"],
       ["w", "f", "f", "f", "sh", "f", "f", "sh", "w"],
       ["w", "sh", "f", "f", "f", "f", "f", "f", "w"],
       ["w", "w", "w", "l", "l", "l", "w", "w", "w"]]

tunnel = [["w", "e", "e", "e", "e", "e", "e", "e", "w"],
          ["w", "f", "f", "f", "f", "f", "f", "f", "w"],
          ["w", "f", "f", "f", "f", "f", "f", "f", "w"],
          ["w", "f", "f", "f", "f", "f", "f", "f", "w"],
          ["w", "f", "f", "sh", "f", "f", "f", "f", "w"],
          ["w", "f", "f", "f", "f", "sh", "f", "f", "w"],
          ["w", "f", "f", "f", "sh", "f", "f", "sh", "w"],
          ["w", "sh", "f", "f", "f", "f", "f", "f", "w"],
          ["e", "e", "e", "e", "e", "e", "e", "e", "e"]]
currentmap = lab
def line():
    print("----------------------")
line()
def yougot(gaineditem):
    gaineditem=str(gaineditem)
    gaineditem=gaineditem.upper()
    print(f"you got a {gaineditem}!") #says "you got(this item)" so i dont have to type this whole thing out over
#                                      and over when you get a new item from looting or killing mobs



wepstats={
    "stat_weapons": {"nothing":0 ,"wood bat": 3, "axe": 6, "knife": 10},
    "stat_armour":{"nothing":0 ,"leather vest":4, "metal sheets":7}
}

using={"weapons":"nothing","armour":"nothing"}

level = int(0)
MAXHP = 15
MAXHP = (level * 3) + MAXHP + wepstats["stat_armour"][using["armour"]]
HP = float(MAXHP)
kills=0
baseatk=3
atk = (level * 1.5) + baseatk + wepstats["stat_weapons"][using["weapons"]]
levscale = level * 1.2
inventory={"weapons":[],"armour":[],"foods":[], "level": level, "HP": HP, "MAXHP":MAXHP, "attack":atk, "kills":kills}

stats={"level":inventory["level"], "HP":inventory["HP"], "attack":inventory["attack"]}

def inv():
    global choice,inventory,using,atk,level,baseatk,HP,MAXHP
    inving=True
    atk = (level* 1.5) + baseatk + wepstats["stat_weapons"][using["weapons"]]
    inventory["attack"] = atk
    print(inventory)
    while inving == True:
        print("1. equip weapon  2.equip armour  3. eat something  4. exit")
        choice=input("->")
        if choice == "1":
            if not inventory["weapons"]:
                print("you have no weapons to equip.")
            else:
                findex = len((inventory["weapons"]))
                tnum = 0

                for i in range(int(findex)):
                    print(tnum, ".", inventory["weapons"][tnum])
                    tnum = tnum + 1
                    equing=True
                while equing==True:
                    equipping = (input("->"))
                    if equipping.isdigit():
                        try:
                            equipping = int(equipping)
                            using["weapons"] = inventory["weapons"][equipping]
                            atk = (level * 1.5) + baseatk + wepstats["stat_weapons"][using["weapons"]]
                            print(using["weapons"])
                            print("your attack is: ",atk)
                            break
                        except IndexError:
                            print("you input the wrong number mate")
                            break

        elif choice == "2":
            if not inventory["armour"]:
                print("you have no armour")
            else:
                findex = len(inventory["armour"])
                tnum = 0

                for i in range(int(findex)):
                    print(tnum, ".", inventory["armour"][tnum])
                    tnum = tnum + 1
                    equing = True
                while equing == True:
                    equipping = (input("->"))
                    if equipping.isdigit():
                        try:
                            equipping = int(equipping)
                            using["armour"] = inventory["armour"][equipping]
                            MAXHP = (level * 3) + MAXHP + wepstats["stat_armour"][using["armour"]]
                            inventory["MAXHP"]
                            print(using["armour"])
                            print("your MAXHP is: ", MAXHP)
                            break
                        except IndexError:
                            print("you input the wrong number mate")
                            break
                    else:
                        print("not a number")
                        break

        elif choice == "3":
            if not inventory["foods"]:
                print("you have no foods!?!?")
            else:
                findex = len((inventory["foods"]))
                tnum = 0

                for i in range(int(findex)):
                    print(tnum, ".", inventory["foods"][tnum])
                    tnum = tnum + 1
                while True:
                    eating = input("->")
                    if eating.isdigit():
                        try:
                            eating=int(eating)
                            if inventory["foods"][eating] == "SPRsoup":
                                if HP == MAXHP:
                                    print("you have max hp.")
                                    break
                                inventory["foods"].pop(eating)
                                print("you feel so souper!")
                                print("ATK and HP increase.")
                                HP = HP + 7
                                print("+7 HP")
                                if HP > MAXHP:
                                    HP = MAXHP
                                    print("HP was maxxed!")
                                inventory["HP"] = HP
                                baseatk = baseatk + 2

                                break

                            elif inventory["foods"][eating] == "CANbeans":
                                if HP == MAXHP:
                                    print("you have max hp.")
                                    break
                                inventory["foods"].pop(eating)
                                print("hienz beanz mmm")
                                HP = HP + 10
                                print("+10 HP")
                                if HP > MAXHP:
                                    HP = MAXHP

                                inventory["HP"] = HP
                                break
                        except IndexError:
                            print("not an option")
                            break
        if choice == "4":
            break

elist=["zombie","skelezombie","fatbie"]
elist2=["ZEBRUTE","zombie","skelezombie","fatbie"]
mobs = {
    "random guy": {"attack": 3, "HP":6, "ascii":"웃", "desc":"rando turned into a zombie!?"},
    "zombie": {"attack": 4 + levscale, "HP": 7 + levscale, "ascii":"\\(´ཀ`)/", "desc": "hes green and greedy and so green and green, did i mention hes green?"},
    "skelezombie": {"attack": 7 + levscale, "HP": 4 + levscale,"ascii":"𐂯-(´ཀ`)-𐂯", "desc": "his arms are stripped to the bone and weirdly sharp. owie! owie!"},
    "fatbie": {"attack": 2 + levscale, "HP": 12 + levscale,"ascii": "(っ҂ཀ•)っ", "desc": "VERY fat "},
    "ZEBRUTE":{"attack":10+ levscale, "HP": 20 + levscale,"desc":"a big boy!","ascii":"""
   ◞◞\\/◟◟
 ◜| ⚇  ◯ |◝
 ◟▕  ⯊メ▕ ◞
   ◟――◞
"""}
}

def battle():
    line()
    global atk,HP,level,MAXHP,kills,username
    if currentmap == lab:
        enemy=random.choice(elist)
    if introIs == True:
        enemy="random guy"
    if firstbrute == True:
        enemy="ZEBRUTE"
    ehp = mobs[enemy]["HP"]
    ehp=int(ehp)
    emaxhp = ehp

    print("your stats",stats)
    print(f"\na {enemy} approaches!")

    if introIs == True:
        print("press 1 and attack!!!")
        print("you can heal by eating food by pressing 2 which is found in shops.\nyou can run if you think you're outmatched but there is a chance that you can fail;\nwhen you fail, the enemy will be able to have their turn!")


    turn=True
    while True:
        if ehp > 0:
            if turn == True:
                print(f"{enemy} - HP: {ehp}/{emaxhp} ATK: {mobs[enemy]["attack"]}")
                print(mobs[enemy]["ascii"])
                print(mobs[enemy]["desc"])
                line()
                print("\n1. FIGHT  2.ACTION  3.RUN")
                batinput = input("\n->")
                if batinput == "1":
                    print("you did",atk,"damage")
                    ehp = ehp - atk
                    turn=False
                elif batinput == "2":
                    inv()
                    turn=False
                elif batinput == "3":

                    i=random.randint(0,100)
                    if introIs == True:
                        print("doc:GET BACK HERE")
                        print("the doctor dragged you back!")
                        turn = False
                    elif i < 70:
                        i=random.randint(1,2)
                        if i == 1:
                            print("you ran from the",enemy,"!")
                            break
                        elif i == 2:
                            print("you retreated strategically from the",enemy)
                            break
                    else:
                        print("it dragged you back into the fight!!")
                        turn = False
            elif turn == False:
                if firstbrute == True:
                    brutedia()

                    ehp=0

                else:
                    print("the",enemy,"attacked and did",mobs[enemy]["attack"],"damage.")
                    HP = HP - mobs[enemy]["attack"]
                    print("your HP is now:", HP, "/", MAXHP)
                    inventory["HP"]=HP
                    turn = True
        elif ehp <= 0:
            print("battle won woo hoo!")
            print("+1 kill")
            kills = kills+1
            print("+10 HP from winning.")
            HP = HP + 10
            if HP > MAXHP:
                HP = MAXHP
                print("MAX HP")
            inventory["HP"]=HP
            inventory["kills"]=kills
            if introIs == False:
                if kills == 3:
                    print("level up!")
                    level = level+1
                    inventory["level"]=level
                    inventory["MAXHP"]=MAXHP
                    print("you are now level",level)
                    kills = 0
                stealing(0,1)
                line()
                print(tilename)
            break
        if HP <= 0:
            print("you died bye")
            exit()

def intro():        #the intro which will lead into the first battle of the game
    print("DIALOGUE")
    line()
    print("...")
    input()
    print("???: do you hear me?... soldier?..")
    input()
    print("???:what is your name?\n")
    while True:
        username = input("->")
        if username == "":
            print("hi no gimme a name")
        else:
            break
    print("\n???:ah yes", username)
    print("???:that checks out.")
    input()
    print("???:are you even conscious...")
    input()
    print("???:WAKEUP DAMN!")
    playsound("sounds/spray.wav")
    playsound("sounds/scream.wav")
    print("*your nostrils burn.*")
    print("???:nothing like some skatole and ammonium sulfide (fart spray.), am i right!?")
    input()
    print("???:no?... okay........")
    input()
    print("???:you're probably confused...")
    input()
    print("well to start off, my name is...")
    playsound("sounds/drumroll.mp3")
    print("???:THE DOCTOR!!")
    input()
    print("doc:why are you looking at me like that.")
    input()
    print("doc:well so basically like")
    input()
    print("doc:well errr so bascially whats happening is that..")
    input()
    print("doc:so its kkindaaa baaaadd-")
    print("???:THERES A ZOMBIE APOCALYPSE AND YOU'RE THE WORLDS LAST HOPE.")
    input()
    print("doc:...")
    input()
    print("doc:who are you.(╭ರ_•́)")
    input()
    print("1.'im the worlds last hope?'\n2.'who are you... who is this kid? whats he gonna do?'\n3.'oooh pooo..'")
    while True:
        dc = input("->")
        if dc == "1":
            print("doc:*cough* yeah pretty much...")
            input()
            break
        elif dc == "2":
            print("???:oh am i talking to loud.")
            input()
            print("doc:yes obviously bro.")
            input()
            break
        elif dc == "3":
            print("doc:no i didntpoo.....")
            break
    dc=0
    print("doc:how did you get in here anyway rando???")
    input()
    print("ultra evil guy:my name is actually ultra evil guy im here to stop you from saving the world grgrllgGRAHHH!")
    print("*he turns into a zombie on the spot?!*")
    input()
    print("doc:holy crap save me my dear soldier",username)
    MapGame
    battle()
    print("doc:omg you saved mee!!")
    input()
    print("doc:YOU have to save the world so we should probably be leaving soon.")
    input()
    input("doc:its time for your...")
    input()

introIs = True #to skip the intro
while introIs == True:
    print("'->' means you have to input something to continue ")
    print("when you see 'DIALOGUE' you must press ENTER to continue the dialogue.")
    introchoice = input("do you want the intro y/n\n->")
    line()
    if introchoice == "y":
        intro()
        introIs = False
    elif introchoice == "n":
        while True:
            username = input("your name:\n->")
            if username == "":
                print("hi no gimme a name")
            else:
                break
        introIs=False

def brutedia():
    global firstbrute,HP
    print("the brute attack and did",HP-1,"damage!")
    HP -= HP -1
    print("your HP is now:", HP, "/", MAXHP)
    print("you are crippled!\n you will miss one turn.")
    line()
    print("DIALOGUE")
    input()
    print("doc:ARE YOU OKAY", username, "?!")
    input()
    print("doc:oh god this is it then... your mission is over...")
    input()
    print("???:HEY!")
    line()
    print(
        "1. its so over were getting jumped ONTOP of this thing that just almost one shot me.\n2.yay were getting saved!!!\n")
    dc = input("->")
    if dc == "1":
        print("???:NONO WE WANNA HELP STOP DONT MOVE A MUSCLE!!")
    elif dc == "2":
        print("???:YESYES NOW DONT MOVE!")
    input()
    print("???:the brute has CRIPPLED you!\n???:if you try to act or attack or run you WILL die.")
    input()
    print("doc:what do we do then??")
    input()
    global fbruteend
    fbruteend = True
    firstbrute = False

def menu(): #the menu you can access while ingame!!
    global MapGame
    print("______ _____  ___ ______   _    _  ___   _      _   __")
    print("|  _  \\  ___|/ _ \\|  _  \\ | |  | |/ _ \\ | |    | | / / ")
    print("| | | | |__ / /_\\ \\ | | | | |  | / /_\\ \\| |    | |/ /")
    print("| | | |  __||  _  | | | | | |/\\| |  _  || |    |    \\ ")
    print("| |/ /| |___| | | | |/ /  \\  /\\  / | | || |____| |\\  \\ ")
    print("|___/ \\____/\\_| |_/___/    \\/  \\/\\_| |_/\\_____/\\_| \\_/")

    print("[¬º-°]¬\n")
    print("----------------------")
    print("# 1 --> play")
    print("# 2 --> controls(recommended)")
    print("# 3 --> quit")
    print("----------------------")
    while True:
        print("what is your choice?:")
        menuchoice = input("->")
        if menuchoice == "1":
            MapGame = True
            break
        if menuchoice == "2":
            print("")
            line()
            print("WASD to move\n[E] to interact with buildings and on map items\n[I] to access your inventory\n[M] to come back to this menu")
            print("-> means input")
            line()
            print("BATTLE CONTROLS\nbattles are played with the numbers corresponding to what thing you would like to select.\n1.ATTACK 2.IEM 3.RUN\nyou would enter 1 2 or 3 depending on your choice,\nthis applies for every time you see numbers and a period")
            line()
            print("1 to play now ok go play press 1 thanks okay bye")
        if menuchoice == "3":
            print("okay bye")
            break

menu()
def tunneldia():
    global firstbrute
    print("DIALOGUE")
    print("doc:holycrap the tunnel closed in on us")
    input()
    print("yo it stank in here.")
    print("1.sorry i farded lol!\n2.i think the fart spray was worse mate.\n3.oooh poopoo...")

    while True:
        dc = input("->")
        if dc == "1":
            print("doc:no you didnt i just realised theres a billion zombies in here!! -(°ﾛ°)- ")
            break
        elif dc == "2":
            print("doc:it COULDNT have been that bad")
            break
        elif dc == "3":
            print("doc:how did you know i pooped myself (ᵕ—ᴗ—)")
            break
    dc=0
    input()
    print("doc:HOLY CRAP LOOK AT HOW BIG HE IS ITS SO OVER HES APPROACHING AAAAA")
    firstbrute=True
    battle()

while MapGame == True:
    y = 8
    x = 4

    currentmap = lab
    y_len = len(currentmap) - 1
    x_len = len(currentmap[0]) - 1

    biom = {
        "w": {"t": "wall", "en": True},
        "e": {"t": "entrance", "en": False},
        "f": {"t": "floor", "en": True},
        "sh": {"t": "shop", "en": False},
        "l": {"t": "lab", "en": False},
        "rsh": {"t": "a looted shop.", "en": False}# naming the tiles on the map
    }

    current_tile = currentmap[y][x]
    tilename = biom[current_tile]["t"]
    entile = biom[current_tile]["en"]

    play = True
    print("you've left the lab with the doctor.")
    print("doc:go explore, you can move in all directions.")

    labcount = 0
    encounter = 0
    encounternum = 0


    while play:
        interacts=["e","i","m"]#interactions
        mapinputs = ["w","a","s","d","e","i","m"]# the inputs the player is allowed to do
        walks = ["w","a","s","d"]#walk inputs

        current_tile = currentmap[y][x]

        choice = input("-> ").lower()
        if not any(char in choice for char in mapinputs):
            print("INVALID")
            playsound("sounds/invalid input.wav")  # if the input the player gives is invalid it tells them and makes a sound

        if choice == "w":
            if y > 0:
                y -= 1
        elif choice == "d":
            if x < x_len:
                x += 1
        elif choice == "s":
            if y < y_len:
                y += 1
        elif choice == "a":
            if x > 0:
                x -= 1  # movement with built-in boundaries


        def icheck(itemtocheck, whatclassitem):
            if itemtocheck in inventory["weapons"] or itemtocheck in inventory["armour"]:
                print("but you already have one.")
            else:
                inventory[whatclassitem].append(itemtocheck)

        def stealing(a,b):
            for i in range(a,b):
                whatclass = random.randint(1, 4)
                if whatclass == 1:
                    robc = random.randint(1, 100)

                    if robc >= 80:
                        yougot("knife")
                        icheck("knife", "weapons")
                    elif robc >= 60:
                        yougot("axe")
                        icheck("axe", "weapons")
                    elif robc >= 1:
                        yougot("wood bat")
                        icheck("wood bat", "weapons")
                elif whatclass == 2:
                    robc = random.randint(1, 100)

                    if robc <= 60:
                        yougot("leather vest")
                        icheck("leather vest","armour")
                    elif robc <= 100:
                        yougot("metal sheets??")
                        icheck("metal sheets","armour")
                elif whatclass == 3:
                    robc = random.randint(1, 100)

                    if robc <= 40:
                        yougot("canned beans")
                        inventory["foods"].append("CANbeans")
                    elif robc <= 100:
                        yougot("super soup!")
                        inventory["foods"].append("SPRsoup")
                elif whatclass == 4:
                    print("you got nothing")

        current_tile = currentmap[y][x]  # ]
        tilename = biom[current_tile]["t"]  # ] finds out what tile the player is standing on
        entile = biom[current_tile]["en"]  # ]


        print(tilename)

        if choice == "i":
            inv()
        if choice == "m":
            menu()
        if choice == "e":
            if current_tile == "sh":
                print("oo you stealin, heres what you got!:")
                stealing(0,3)
                currentmap[y][x] = "rsh"
                current_tile = currentmap[y][x]
            elif current_tile == "e":
                if level == 3:
                    if currentmap == lab:
                        currentmap = tunnel
                        print("you went into the tunnel.")
                        y = y + 8
                        print("the entrance closed behind you!")
                        tunneldia()
                else:
                    print("you are not high enough level!")
                    entrancecount=+1
                    if entrancecount==1:
                        print("DIALOGUE")
                        print("doc:try to get to to level three, maybe that will help!")
                if currentmap == tunnel:
                    "you cant go back"
            elif current_tile == "l":
                print("the lab, you're too busy to go back there")

            elif current_tile == "w":
                if wallcount==0:
                    print("its a wall, bland and concrete, designed to protect the town. doesnt seem like it did much of a job.")
                    wallcount=1
                elif wallcount!=0:
                    print("the wall that failed.")
        elif current_tile == "sh":
            print("there is a shop here, loot it? [E]")
        elif current_tile == "f":
            print("nothing here.")

        elif current_tile == "w":
            if y == 0 and x == 0 or x == 8 and y == 0 or y == 8 and x == 0 or x == 8 and y == 8:
                print("you're in a corner.")
            elif y == 0:
                print("there is a wall above you.")
            elif x == 0:
                print("there is a wall to your left.")
            elif x == 8:
                print("there is a wall to your right")
            elif y == 8:
                print("there is a wall below you.")         #built in borders for movement

            rollmoss = random.randint(1, 10)
            if rollmoss == 1:
                mosstime = True
                while mosstime == True:
                    eatmoss = input("there is moss here. eat it? Y/N\n")
                    if eatmoss.lower() == "y":
                        print("you ate the moss.\n you feel great!")
                        print("+5 HP")
                        hp = hp + 5
                        if HP>MAXHP:
                            HP=MAXHP
                        mosstime = False
                    elif eatmoss.lower() == "n":
                        print("loser.")
                        mosstime = False  # an Easter egg referencing deltarune

        elif current_tile == "l":
            labcount = labcount + 1
            if labcount == 3:
                print("okay try pressing w bro, get AWAY from the lab, please.")
            else:
                print("there is a lab here")

        if entile == True:
            if currentmap == lab:
                encounter = random.randint(1, 10)
                if encounter == 1:
                    battle()
            elif currentmap == tunnel:
                encounter = random.randint(1, 5)
        if any(char in choice for char in walks):
            playsound("sounds/walk.wav")
        elif any(char in choice for char in interacts):
            playsound("sounds/bell.mp3")
