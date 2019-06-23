import os
import json
import time
def clear():
    os.system('cls' if os.name ==  'nt' else 'clear')

x = 0
y = 0
inventory = []
guardAlive = True
userInput = 0
actionText = ''
deathList = []
deathNumber = -1
deathCount = 0

def typeAnything():
    print('')
    print('')
    print('')
    print(' -Type Anything to Continue- ')
    input('> ')
    clear()

def getInput():
    print('')
    print('')
    print('')
    print('')
    print('')
    global userInput
    userInput = input('> ')
    userInput = userInput.lower()
    userInput = userInput.strip()

def titleScreen():
    clear()
    print(
    '''
    ___________________________________________________________________________________________________________________
    |  __        ______  ______    ________   ________           ________    __    __   ______   ________  __________  |
    |  | |      |  ____| |  ___|   |__  ___| |  _____|          | ______ |   | |   | | |  ____| |  _____| |___    ___| |
    |  | |      | |__    | | ____     | |    | |_____           | |    | |   | |   | | | |__    | |_____      |  |     |
    |  | |      |  __|   | | |_  |    | |    |_____  |          | |    | |   | |   | | |  __|   |_____  |     |  |     |
    |  | |____  | |____  | |___| | ___| |__   _____| |          | |____| |   | |___| | | |____   _____| |     |  |     |
    |  |______| |______| |_______| |_______| |_______|          |________|__ |_______| |______| |_______|     |__|     |
    |                                                                    |__|                                          |
    |__________________________________________________________________________________________________________________|
    
    '''
    )
    typeAnything()

def firstScreen():
    print('Legis Quest')
    print('')
    print('You wake up in the middle of a field. You had stopped here to take a rest a litte while ago. You get up now in order to continue your quest.')
    typeAnything()
    print('Legis Quest')
    print('')
    print('For years on end you had been searching for it. The artifact to end all artifacts. The most desired, most valued object in the universe. You were convinced you would be the one to finally obtain it. To finally grasp...')
    typeAnything()
    print('Legis Quest')
    print('')
    print('THE LEGIS')
    typeAnything()

def printHeader():
    global x
    global y
    global inventory
    global actionText
    if x == 0 and y == 0:
        print('Field')
        print('')
    elif x == 0 and y == -1:
        print('Cavern')
        print('')
    elif x == 0 and y == 1:
        print('Sword Area')
        print('')
    elif x == 80 and y == 80:
        print('Legis')
        print('')
    else:
        print('Out Of Bounds')
        print('')
    if actionText != '':
        print(actionText)
        print('')

def save():
    global x
    global y
    global guardAlive
    global inventory
    saveX = json.dumps(x)
    saveY = json.dumps(y)
    saveGuardAlive = json.dumps(guardAlive)
    saveInventory = json.dumps(inventory)
    saveFile = open('Saves/Save.json', 'w')
    saveFile.write(saveX + '\n' + saveY + '\n' + saveGuardAlive + '\n' + saveInventory)
    saveFile.close()

def load():
    global x
    global y
    global guardAlive
    global inventory
    global actionText
    if os.path.isfile('Saves/Save.json'):
        saveFile = open('Saves/Save.json', 'r')
        x = saveFile.readline()
        y = saveFile.readline()
        guardAlive = saveFile.readline()
        inventory = saveFile.readline()
        saveFile.close()
        x = json.loads(x)
        y = json.loads(y)
        guardAlive = json.loads(guardAlive)
        inventory = json.loads(inventory)
        actionText = 'Game loaded.'
        loadDeath()
    else:
        actionText = 'You don\'t have a save file!'

def saveDeath():
    global deathList
    global deathCount
    saveDeathList = json.dumps(deathList)
    saveDeathCount = json.dumps(deathCount)
    deathFile = open('Saves/Deaths.json', 'w')
    deathFile.write(saveDeathList + '\n' + saveDeathCount)
    deathFile.close()

def loadDeath():
    global deathList
    global deathCount
    if os.path.isfile('Saves/Deaths.json'):
        deathFile = open('Saves/Deaths.json', 'r')
        deathList = deathFile.readline()
        deathCount = deathFile.readline()
        deathFile.close()
        deathList = json.loads(deathList)
        deathCount = json.loads(deathCount)

def gameOver():
    global deathList
    global deathNumber
    global deathCount
    if deathNumber not in deathList:
        deathList.append(deathNumber)
        deathCount = deathCount + 1
    saveDeath()
    print('')
    print('You are dead.')
    print('Game Over.')
    print('')

def printAreaDescription():
    global x
    global y
    global inventory
    global actionText
    global guardAlive
    if x == 0 and y == 0:
        print('You stand in the middle of a large, empty field. There is nothing of interest around you.')
        print('')
        print('The field extends for quite a while to both the EAST and the WEST, but there appear to be exits to the NORTH, the SOUTH and the LEGIS')
    elif x == 0 and y == -1:
        print('You are in a small cavern to the south of the field. You see that it somehow manages to contain an enormous pit with lava and very sharp looking spikes at the bottom. You would most likely not like to fall down it.')
        print('')
        print('You wonder how the lava manages to exist with the surrounding enviroment intact.')
    elif x == 0 and y == 1 and 'sword' not in inventory:
        print('You are standing next to a sword stuck in a rock in the middle of the field.')
    elif x == 0 and y == 1 and 'sword' in inventory:
        print('You are standing next to a rock in the middle of the field.')
    elif x == 80 and y == 80 and guardAlive == True:
        print('You are at the legis. It sits majestically on a pedestal and illumiates the room. Unfortunately for you, the legis is being guarded by some random dood.')
        print('You will probably have to fight him if you want the legis.')
        print('')
        print('Obvious exits are NOT LEGIS.')
    elif x == 80 and y == 80 and guardAlive == False:
        print('You are at the legis. A random dood with a massive chest wound lays on the floor.')
        print('The legis sits on its pedestal, ripe for the taking.')
        print('')
        print('Obvious exits are NOT LEGIS.')
    else:
        print('You\'re not supposed to be here. Stop hacking.')

def gameLoop():
    global userInput
    global x
    global y
    global inventory
    global actionText
    global guardAlive
    global deathNumber
    while True:
        clear()
        print('Legis Quest')
        printHeader()
        printAreaDescription()
        getInput()
        if userInput == 'north' or userInput == 'n' or userInput == 'go north':
            if x == 0 and y == 0:
                y = 1
                actionText = ''
            elif x == 0 and y == 1:
                actionText = 'You attempt to go north, but an enormous tree grows out of nowhere and blocks your path.'
            elif x == 0 and y == -1:
                y = 0
                actionText = ''
        elif userInput == 'south' or userInput == 's' or userInput == 'go south':
            if x == 0 and y == 0:
                y = -1
                actionText = ''
            elif x == 0 and y == 1:
                y = 0
                actionText = ''
            elif x == 0 and y == -1:
                deathNumber = 0
                print('Really? Ok.')
                print('')
                print('You walk to the south, fall of the edge, into the pit, and die an excruciatingly painful death.')
                gameOver()
                break
        elif userInput == 'west' or userInput == 'w' or userInput == 'go west':
            if x == 0 and y == 0:
                actionText = 'You attempt to go west, but are teleported to back to the center for no apparent reason. \n \nYou mentally curse the programer of this game for being too lazy to program an accessible area to the west.'
            elif x == 0 and y == 1:
                deathNumber = 1
                print('You attempt to go west when a goat comes out of nowhere and kicks you in the face. You fall to the ground and bleed to death.')
                gameOver()
                break
            elif x == 0 and y == -1:
                actionText = 'You can\'t do that.'
        elif userInput == 'east' or userInput == 'e' or userInput == 'go east':
            if x == 0 and y == 0:
                actionText = 'You attempt to go east, but are teleported to back to the center for no apparent reason. \n \nYou mentally curse the programer of this game for being too lazy to program an accessible area to the east.'
            elif x == 0 and y == 1:
                actionText = 'You go to the east, but upon realizing that the area to the east of you hadn\'t actually been programed into the game, you return to the sword area.'
            elif x == 0 and y == -1:
                actionText = 'You can\'t do that.'
        elif userInput == 'legis' or userInput == 'l' or userInput == 'go legis':
            if x == 0 and y == 0:
                x = 80
                y = 80
                actionText = ''
            else:
                actionText = 'You can\'t do that, as much as you would like to.'
        elif userInput == 'not legis' or userInput == 'nl' or userInput == 'n l' or userInput == 'go not legis':
            if x == 80 and y == 80 and guardAlive == True:
                x = 0
                y = 0
                actionText = ''
            if x == 80 and y == 80 and guardAlive == False:
                deathNumber = 2
                print('Seriously?')
                time.sleep(1)
                print('Seriously?')
                time.sleep(1)
                print('')
                print('The legis is right there, ready to be taken, and you\'re just going to leave?')
                time.sleep(2)
                print('')
                print('')
                print('The programer of this game personaly comes into the game and kills you.')
                gameOver()
                break
            else:
                actionText = 'That is the exact opposite of where you are trying to go.'
        elif userInput == 'get sword' or userInput == 'pull sword' or userInput == 'pull on sword' or userInput == 'yank sword':
            if x == 0 and y == 1:
                actionText = 'You unceremoniously yank the sword out of the stone.'
                inventory.append('sword')
            else:
                actionText = 'I see no sword here.'
        elif userInput == 'stab' or userInput == 'stab dood' or userInput == 'stab guy' or userInput == 'stab person' or userInput == 'stab guard' or userInput == 'stab dude' or userInput == 'stab random dood' or userInput == 'stab random dude' or userInput == 'kill dood' or userInput == 'kill guy' or userInput == 'kill person' or userInput == 'kill guard' or userInput == 'kill dude' or userInput == 'kill random dood' or userInput == 'kill random dude' or userInput == 'fight' or userInput == 'fight dood' or userInput == 'fight guy' or userInput == 'fight person' or userInput == 'fight guard' or userInput == 'fight dude' or userInput == 'fight random dood' or userInput == 'fight random dude':
            if x == 80 and y == 80 and 'sword' in inventory:
                actionText = 'You walk up the guard and stab him the the chest. He falls over onto the ground.'
                guardAlive = False
            elif x == 80 and y == 80 and 'sword' not in inventory:
                deathNumber = 3
                print('You walk up the guard and attempt to stab him with your fist.')
                print('He pulls out an enormous axe and decapitates you.')
                gameOver()
                break
            else:
                actionText = 'There is nobody to attack here.'
        elif userInput == 'get legis' or userInput == 'grab legis':
            if x == 80 and y == 80 and guardAlive == False:
                actionText = ''
                clear()
                print('Legis Quest')
                printHeader()
                print('Stepping over the guard\'s dead body, you reach for the legis.')
                typeAnything()
                print('Legis Quest')
                printHeader()
                print('Your hands are trembling...')
                typeAnything()
                print('Legis Quest')
                printHeader()
                print('You grasp the legis...')
                typeAnything()
                print('Legis Quest')
                printHeader()
                print('You pull it from its pedestal...')
                typeAnything()
                print('Legis Quest')
                printHeader()
                print('You have finally obtained the legis!')
                print('')
                print('')
                print('You win!')
                print('')
                print('')
                if deathCount == 6:
                    print('You found all possible death messages!')
                    print('')
                    print('Congratulations!')
                elif deathCount == 0:
                    print('You never encountered a death message!')
                    print('')
                    print('...')
                    time.sleep(3)
                    print('')
                    print('')
                    print('You pathetic little excuse for a human being.')
                    time.sleep(2)
                    print('')
                    print('')
                    print('')
                    print('Get out of my sight.')
                else:
                    print('You found ' + str(deathCount) + ' out of 6 unique death messages!')
                print('')
                break
            elif x == 80 and y == 80 and guardAlive == True:
                deathNumber = 4
                print('You walk up the legis and try to grasp it.')
                print('The guy guarding the legis pulls out an enormous axe and decapitates you.')
                gameOver()
                break
            else:
                actionText = 'That is exactly what you are trying to do.'
        elif userInput == 'inventory' or userInput == 'inv':
            if inventory == []:
                actionText = 'You have no items.'
            else:
                actionText = 'You have:\n'
                if 'sword' in inventory:
                    actionText = actionText + 'A Sword\n'
        elif userInput == 'save':
            save()
            actionText = 'Game saved.'
        elif userInput == 'load':
            load()
        elif userInput == 'jump' or userInput == 'fall' or userInput == 'jump down' or userInput == 'fall down' or userInput == 'jump down it' or userInput == 'fall down it':
            if x == 0 and y == -1:
                deathNumber = 0
                print('Really? Ok.')
                print('')
                print('You fall of the edge, into the pit, and die an excruciatingly painful death.')
                gameOver()
                break
            else:
                actionText = 'Off of what?'
        elif userInput == 'quit':
            clear()
            break
        elif userInput == 'die' or userInput == 'suicide' or userInput == 'commit suicide' or userInput == 'commit die' or userInput == 'kill self' or userInput == 'kill myself':
            deathNumber = 5
            print('...')
            time.sleep(2)
            print('')
            print('Alright then!')
            time.sleep(0.5)
            print('You will your heart to stop beating.')
            gameOver()
            break
        elif userInput == 'get ye flask':
            actionText = 'You\'re not a dunegonman!'
        else:
            actionText = 'I have no idea what just asked me to do.'

titleScreen()
firstScreen()
loadDeath()
gameLoop()