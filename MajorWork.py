import pygame
import random
pygame.init()

#Functional Test, Score and High Score display and are updated properly, High Score is stored separately

Screen = pygame.display.set_mode((520,520))
pygame.display.set_caption("SDD Assignment 2")
startGameImage = pygame.image.load('Home Screen.jpg')
playGameImage = pygame.image.load('Game Screen.jpg')
font_1 = pygame.font.SysFont("Verdana",20)
font_2 = pygame.font.SysFont("Verdana",30)
font_3 = pygame.font.SysFont("Verdana",11)
text_colour_1 = (255,255,255)
text_colour_2 = (255,23,15)
obstacle = pygame.image.load("platform1.png")
obstacle2 = pygame.image.load("platform2.png")
dropdown = pygame.image.load("Dropdown.png")
menu = pygame.image.load("Menu.png")
menu_over = pygame.image.load("Menu_Over.png")
button = pygame.image.load("Button.png")
button_over = pygame.image.load("Button_over.png")

playerWidth = (pygame.image.load('Charactere_Idle_Left_0.png')).get_width()*4
playerHeight = (pygame.image.load('Charactere_Idle_Left_0.png')).get_height()*4
walkRight = [pygame.image.load('Charater_Walk_Right_0.png'), pygame.image.load('Charater_Walk_Right_1.png'), pygame.image.load('Charater_Walk_Right_2.png'), pygame.image.load('Charater_Walk_Right_3.png'), pygame.image.load('Charater_Walk_Right_4.png'), pygame.image.load('Charater_Walk_Right_5.png'), pygame.image.load('Charater_Walk_Right_6.png'), pygame.image.load('Charater_Walk_Right_7.png')]
walkLeft = [pygame.image.load('Character_Walk_Left_0.png'), pygame.image.load('Character_Walk_Left_1.png'), pygame.image.load('Character_Walk_Left_2.png'), pygame.image.load('Character_Walk_Left_3.png'), pygame.image.load('Character_Walk_Left_4.png'), pygame.image.load('Character_Walk_Left_5.png'), pygame.image.load('Character_Walk_Left_6.png'), pygame.image.load('Character_Walk_Left_7.png')]
jumpRight = [pygame.image.load('Character_Jump_Right_0.png'), pygame.image.load('Character_Jump_Right_1.png'), pygame.image.load('Character_Jump_Right_2.png')]
jumpLeft = [pygame.image.load('Character_Jump_Left_0.png'), pygame.image.load('Character_Jump_Left_1.png'), pygame.image.load('Character_Jump_Left_2.png')]
ObstacleImage1Width = obstacle.get_width()/8
ObstacleImage1Height = obstacle.get_height()/8
ObstacleImage2Width = obstacle2.get_height()/8
ObstacleImage2Height = obstacle2.get_height()/8
DropdownImageHeight = dropdown.get_height()/8
DropdownImageWidth = dropdown.get_width()/8
MenuImageWidth = menu.get_width()/8
MenuImageHeight = menu.get_height()/8
MenuOverImageWidth = menu_over.get_width()/8
MenuOverImageHeight = menu_over.get_height()/8
ButtonImageWidth = button.get_width()/6
ButtonImageHeight = button.get_height()/6
ButtonOverImageWidth = button_over.get_width()/6
ButtonOverImageHeight = button_over.get_height()/6
ObstacleImage1 = pygame.transform.scale(obstacle, (ObstacleImage1Width, ObstacleImage1Height))
ObstacleImage2 = pygame.transform.scale(obstacle2, (ObstacleImage2Width, ObstacleImage2Height))
DropdownImage = pygame.transform.scale(dropdown,(DropdownImageWidth,DropdownImageHeight))
MenuImage = pygame.transform.scale(menu,(MenuImageWidth,MenuImageHeight))
MenuOverImage = pygame.transform.scale(menu_over,(MenuOverImageWidth,MenuOverImageHeight))
ButtonImage = pygame.transform.scale(button,(ButtonImageWidth,ButtonImageHeight))
ButtonOverImage = pygame.transform.scale(button_over,(ButtonOverImageWidth,ButtonOverImageHeight))

class obstacle(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def drawObstacle1(self, win):
        if not game_over:
            win.blit(ObstacleImage1, (self.x,self.y))
    def drawObstacle2(self,win):
        if not game_over:
            win.blit(ObstacleImage2, (self.x,self.y))

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, win):
        if self.walkCount + 1 >= 24:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
man = player(200, 410, playerWidth,playerHeight)

class button:
    def __init__(self, width, height, colour, over_colour, text):
        self.width = width
        self.height = height
        self.colour = colour
        self.over_colour = over_colour
        self.text = text

startButton = button(125,50, (0,68,185), (30,30,30), font_1.render("Start Game", True, text_colour_1))
helpButton = button(125,50, (0,68,185), (30,30,30), font_1.render("Help", True, text_colour_1))
quitButton = button(125,50, (0,68,185), (30,30,30), font_1.render("Quit", True, text_colour_1))
gameName = font_1.render("SDD Major Work", True, text_colour_1)

helpBoxOuterWidth = 75
helpBoxOuterHeight = 75

class box:
    def __init__(self, width, height, colour):
        self.width = width
        self.height = height
        self.colour = colour

Screen1box1 = box(40,40,(218,118,159))
Screen1box2 = box(80,165,(184,39,86))
Screen1box3 = box(75,63,(64,75,49))
Screen1box4 = box(20,54,(89,54,64))

Screen2box1 = box(84,34,(7,8,78))
Screen2box2 = box(46,54,(48,74,47))
Screen2box3 = box(74,92,(56,53,28))
Screen2box4 = box(57,86,(57,35,56))

Screen3box1 = box(48,65,(98,49,87))
Screen3box2 = box(86,67,(84,49,35))
Screen3box3 = box(74,76,(39,38,34))
Screen3box4 = box(98,85,(84,209,183))

Screen4box1 = box(42,94,(82,138,183))
Screen4box2 = box(29,24,(43,89,39))
Screen4box3 = box(98,28,(25,35,39))
Screen4box4 = box(84,38,(39,75,38))

Screen1pos1 = 99
Screen1pos2 = 280
Screen1pos3 = 497
Screen1pos4 = 750

Screen1pos1y = 400
Screen1pos2y = 360
Screen1pos3y = 300
Screen1pos4y = 350

Screen2pos1 = 34
Screen2pos2 = 246
Screen2pos3 = 487
Screen2pos4 = 684

Screen2pos1y = 300
Screen2pos2y = 340
Screen2pos3y = 420
Screen2pos4y = 350

Screen3pos1 = 38
Screen3pos2 = 235
Screen3pos3 = 498
Screen3pos4 = 725

Screen3pos1y = 360
Screen3pos2y = 410
Screen3pos3y = 450
Screen3pos4y = 470

Screen4pos1 = 34
Screen4pos2 = 259
Screen4pos3 = 485
Screen4pos4 = 708

Screen1 = False
Screen2 = False
Screen3 = False
Screen4 = False

helpBoxOuter = box(460,460,(218,118,159))
helpBoxMiddle = box(450,450,(255,162,157))
helpBoxInner = box(430,430,(255,219,208))

returnButton = button(125,50, (0,68,185), (30,30,30), font_1.render("Return", True, text_colour_1))

helpName = font_2.render("Help", True, text_colour_2)
helpText1 = font_3.render("To play, click on the button marked 'Start'",True, text_colour_1)
helpText2 = font_3.render("To return to home, click on the button marked 'Home'",True, text_colour_1)
helpText3 = font_3.render("To return to the dropdown menu, click on the",True, text_colour_1)
helpText4 = font_3.render("button marked 'Return'", True, text_colour_1)
helpText5 = font_3.render("To open or close the dropdown menu, click on the",True, text_colour_1)
helpText6 = font_3.render("blue button at the top right-hand corner of the screen",True, text_colour_1)
helpText7 = font_3.render("To restart the game after you have died, click on",True, text_colour_1)
helpText8 = font_3.render("the button marked 'Restart'",True, text_colour_1)
helpText9 = font_3.render("To quit, click on the button marked 'Quit'",True, text_colour_1)
helpText10 = font_3.render("Right Arrow key to move right",True, text_colour_1)
helpText11 = font_3.render("Left Arrow key to move left",True, text_colour_1)
helpText12 = font_3.render("Up Arrow key to jump",True,text_colour_1)

game_over = False
mainGame = False
Home = True
Help = False
Menu = False
Died = False

#----------------------1 Home Screen Menu ----------------------

def startGame():
    x, y = (0, 0)
    global game_over
    global mainGame
    global Home
    global Help
    while not game_over and not mainGame and not Help:
        Screen.blit(startGameImage,(0,0))
        Screen.blit(ButtonImage, ((Screen.get_width()-ButtonImageWidth)/2+10,(Screen.get_height()-ButtonImageHeight)/2+50))
        Screen.blit(ButtonImage,
                    ((Screen.get_width() - ButtonImageWidth) / 2+10, (Screen.get_height() - ButtonImageHeight) / 2 -10))
        Screen.blit(ButtonImage,
                    ((Screen.get_width() - ButtonImageWidth) / 2+10, (Screen.get_height() - ButtonImageHeight) / 2 + 110))

        #---------------------1.1 Detect and respond to events-------------------

        for event in pygame.event.get():

            #-------------------1.1.1 Quit ---------------------

            if event.type==pygame.QUIT:
                game_over = True

            #--------------------1.1.2 Mousebuttonup-----------------

            if event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                if ((Screen.get_width() - ButtonImageWidth) / 2 + 10 <= x <= (Screen.get_width() - ButtonImageWidth) / 2 + 10 + ButtonImageWidth and (Screen.get_height() - ButtonImageHeight) / 2 + 110 <= y <=
                (Screen.get_height() - ButtonImageHeight) / 2 + 110+ButtonImageHeight):
                    game_over = True
                if ((Screen.get_width() - ButtonImageWidth) / 2 + 10 <= x <= (Screen.get_width() - ButtonImageWidth) / 2 + 10+ButtonImageWidth and (Screen.get_height() - ButtonImageHeight) / 2 + 50 <= y <= (Screen.get_height() - ButtonImageHeight) / 2 + 50+ButtonImageHeight):
                    Home = False
                    mainGame = True

                if ((Screen.get_width() - ButtonImageWidth) / 2 + 10 <= x <= (Screen.get_width() - ButtonImageWidth) / 2 + 10 +ButtonImageWidth and (Screen.get_height() - ButtonImageHeight) / 2 -10 <= y <=
                (Screen.get_height() - ButtonImageHeight) / 2 - 10 +ButtonImageHeight):
                    Home = False
                    Help = True

            #-------------------1.1.3 Mousemotion--------------------

            if event.type==pygame.MOUSEMOTION:
                x,y = event.pos
        if ((Screen.get_width() - ButtonImageWidth) / 2 + 10 <= x <= (Screen.get_width() - ButtonImageWidth) / 2 + 10+ButtonImageWidth and (Screen.get_height() - ButtonImageHeight) / 2 + 50 <= y <= (Screen.get_height() - ButtonImageHeight) / 2 + 50+ButtonImageHeight):
            Screen.blit(ButtonOverImage, ((Screen.get_width() - ButtonImageWidth) / 2 + 10, (Screen.get_height() - ButtonImageHeight) / 2 + 50))
            Screen.blit(ButtonImage,
                        ((Screen.get_width() - ButtonImageWidth) / 2 + 10,
                         (Screen.get_height() - ButtonImageHeight) / 2 - 10))
            Screen.blit(ButtonImage,
                        ((Screen.get_width() - ButtonImageWidth) / 2 + 10,
                         (Screen.get_height() - ButtonImageHeight) / 2 + 110))


        if ((Screen.get_width() - ButtonImageWidth) / 2 + 10 <= x <= (Screen.get_width() - ButtonImageWidth) / 2 + 10 + ButtonImageWidth and (Screen.get_height() - ButtonImageHeight) / 2 + 110 <= y <=
                (Screen.get_height() - ButtonImageHeight) / 2 + 110+ButtonImageHeight):
            Screen.blit(ButtonImage, (
            (Screen.get_width() - ButtonImageWidth) / 2 + 10, (Screen.get_height() - ButtonImageHeight) / 2 + 50))
            Screen.blit(ButtonImage,
                        ((Screen.get_width() - ButtonImageWidth) / 2 + 10,
                         (Screen.get_height() - ButtonImageHeight) / 2 - 10))
            Screen.blit(ButtonOverImage,
                        ((Screen.get_width() - ButtonImageWidth) / 2 + 10,
                         (Screen.get_height() - ButtonImageHeight) / 2 + 110))

        if ((Screen.get_width() - ButtonImageWidth) / 2 + 10 <= x <= (Screen.get_width() - ButtonImageWidth) / 2 + 10 +ButtonImageWidth and (Screen.get_height() - ButtonImageHeight) / 2 -10 <= y <=
                (Screen.get_height() - ButtonImageHeight) / 2 - 10 +ButtonImageHeight):
            Screen.blit(ButtonImage, (
            (Screen.get_width() - ButtonImageWidth) / 2 + 10, (Screen.get_height() - ButtonImageHeight) / 2 + 50))
            Screen.blit(ButtonOverImage,
                        ((Screen.get_width() - ButtonImageWidth) / 2 + 10,
                         (Screen.get_height() - ButtonImageHeight) / 2 - 10))
            Screen.blit(ButtonImage,
                        ((Screen.get_width() - ButtonImageWidth) / 2 + 10,
                         (Screen.get_height() - ButtonImageHeight) / 2 + 110))


        Screen.blit(startButton.text, ((Screen.get_width() - ButtonImageWidth) / 2 + (ButtonImageWidth - startButton.text.get_width()) / 2,
                                       (Screen.get_height() - ButtonImageHeight) / 2 + 50 + (ButtonImageHeight- startButton.text.get_height()) / 2))
        Screen.blit(helpButton.text, (
        (Screen.get_width() - ButtonImageWidth) / 2 + (ButtonImageWidth - helpButton.text.get_width()) / 2,
        (Screen.get_height() - ButtonImageHeight) / 2 -10 + (ButtonImageHeight - helpButton.text.get_height()) / 2))

        Screen.blit(quitButton.text, (
            (Screen.get_width() - ButtonImageWidth) / 2 + (ButtonImageWidth - quitButton.text.get_width()) / 2,
            (Screen.get_height() - ButtonImageHeight) / 2 +110 + (
                        ButtonImageHeight - quitButton.text.get_height()) / 2))
        Screen.blit(gameName, ((Screen.get_width() - gameName.get_width())/2, (Screen.get_height()-gameName.get_height())/2-70))


        pygame.display.update()

#-------------------------2 Help Screen-----------------------

def help():
    (x,y) = (0,0)
    global game_over
    global mainGame
    global Help
    global Home
    while not game_over and not mainGame and not Home:
        Screen.blit(startGameImage, (0, 0))
        Screen.blit(DropdownImage, (
        (Screen.get_width() - DropdownImageWidth) / 2, (Screen.get_height() - DropdownImageHeight) / 2 - 60))
        Screen.blit(ButtonImage,((Screen.get_width()-ButtonImageWidth)/2+10,390))
        Screen.blit(helpName, ((Screen.get_width() - helpName.get_width()) / 2,
                               0 + (Screen.get_height() - helpName.get_height()) / 2-100))
        Screen.blit(helpText1, ((Screen.get_width() - helpText1.get_width()) / 2 + 10,
                               0 + (Screen.get_height() - helpText1.get_height()) / 2-60))
        Screen.blit(helpText2, ((Screen.get_width() - helpText2.get_width()) / 2 + 10,
                                0 + (Screen.get_height() - helpText2.get_height()) / 2 - 45))
        Screen.blit(helpText3, ((Screen.get_width() - helpText3.get_width()) / 2 + 10,
                                0 + (Screen.get_height() - helpText3.get_height()) / 2 -30))
        Screen.blit(helpText4, ((Screen.get_width() - helpText4.get_width()) / 2 + 10,
                                0 + (Screen.get_height() - helpText4.get_height()) / 2 - 15))
        Screen.blit(helpText5, ((Screen.get_width() - helpText5.get_width()) / 2 + 10,
                                0 + (Screen.get_height() - helpText5.get_height()) / 2))
        Screen.blit(helpText6, ((Screen.get_width() - helpText6.get_width()) / 2 + 10,
                                0 + (Screen.get_height() - helpText6.get_height()) / 2 + 15))
        Screen.blit(helpText7, ((Screen.get_width() - helpText7.get_width()) / 2 + 10,
                                0 + (Screen.get_height() - helpText7.get_height()) / 2 + 30))
        Screen.blit(helpText8, ((Screen.get_width() - helpText8.get_width()) / 2 + 10,
                                0 + (Screen.get_height() - helpText8.get_height()) / 2 + 45))
        Screen.blit(helpText9, ((Screen.get_width() - helpText9.get_width()) / 2 + 10,
                                0 + (Screen.get_height() - helpText9.get_height()) / 2 + 60))
        Screen.blit(helpText10, ((Screen.get_width() - helpText10.get_width()) / 2 + 10,
                                0 + (Screen.get_height() - helpText10.get_height()) / 2 + 75))
        Screen.blit(helpText11, ((Screen.get_width() - helpText11.get_width()) / 2 + 10,
                                0 + (Screen.get_height() - helpText11.get_height()) / 2 + 90))
        Screen.blit(helpText12, ((Screen.get_width() - helpText12.get_width()) / 2 + 10,
                                0 + (Screen.get_height() - helpText12.get_height()) / 2 + 105))

        #--------------------2.1 Detect and respond to events-------------------------

        for event in pygame.event.get():

            #---------------------2.1.1 Quit--------------------

            if event.type == pygame.QUIT:
                game_over = True

            #---------------------2.1.2 Mousebuttonup-------------------------

            if event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                if ((Screen.get_width() - ButtonImageWidth) / 2 + 10 <= x <= (Screen.get_width() - ButtonImageWidth) / 2 + 10 + ButtonImageWidth and 390 <= y <= 390+ButtonImageHeight):
                    Home = True
                    Help = False
            #--------------------2.1.2 Mousemotion---------------------------

            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
        if ((Screen.get_width() - ButtonImageWidth) / 2 + 10 <= x <= (Screen.get_width() - ButtonImageWidth) / 2 + 10 + ButtonImageWidth and 390 <= y <= 390+ButtonImageHeight):
            Screen.blit(ButtonOverImage,((Screen.get_width()-ButtonImageWidth)/2+10,390))


        Screen.blit(returnButton.text, ((Screen.get_width()-ButtonImageWidth)/2 + (ButtonImageWidth - returnButton.text.get_width()) / 2,
                                        390 + (ButtonImageHeight / 2 - returnButton.text.get_height() / 2)))

        pygame.display.update()


MenuHelp = False
platform1 = False
platform2 = False
platform3 = False
Screen1obstacle1 = False
Screen1obstacle2 = False
Screen1obstacle3 = False
Screen1obstacle4 = False
Screen2obstacle1 = False
Screen2obstacle2 = False
Screen2obstacle3 = False
Screen2obstacle4 = False
Screen3obstacle1 = False
Screen3obstacle2 = False
Screen3obstacle3 = False
Screen3obstacle4 = False
Screen4obstacle1 = False
Screen4obstacle2 = False
Screen4obstacle3 = False
Screen4obstacle4 = False

Screens = 0

#---------------------3 Main Game Screen---------------------------

def Game():
    Clock = pygame.time.Clock()
    obstacle1x = 520
    obstacle2x = 520
    obstacle3x = 520
    obstacley = 0
    background1x = 0
    background2x = 1920
    variable = 0
    counter = 1
    Screen1run = False
    Screen2run = False
    Screen3run = False
    global Screens
    global pos1, pos2, pos3, pos4
    global Screen1, Screen2, Screen3, Screen4
    global Screen1obstacle1, Screen1obstacle2, Screen1obstacle3, Screen1obstacle4, Screen2obstacle1, Screen2obstacle2, Screen2obstacle3, Screen2obstacle4, Screen3obstacle1, Screen3obstacle2, Screen3obstacle3, Screen3obstacle4, Screen4obstacle1, Screen4obstacle2, Screen4obstacle3, Screen4obstacle4
    (x, y) = (0, 0)
    Screeny = 0
    youDiedy = -200
    vel = 10
    man.x = 100
    man.y = 520-playerHeight
    over1 = False
    over2 = False
    over3 = False
    Begin = False
    modifier = 1
    menuButton = button(25, 25, (0, 68, 185), (30, 30, 30), font_1.render("||", True, text_colour_1))
    homeButton = button(125, 50, (0, 68, 185), (30, 30, 30), font_1.render("Home", True, text_colour_1))
    menu_button_rect = [(Screen.get_width() - menuButton.width) - 20, 20, menuButton.width,
                        menuButton.height]
    youDied = box(400, 200, (99, 91, 215))
    restartButton = button(125, 50, (0, 68, 185), (30, 30, 30), font_1.render("Restart", True, text_colour_1))
    menuName = font_2.render("Menu", True, text_colour_2)
    diedName = font_2.render("You Died", True, text_colour_2)
    score = 0
    with open("score.txt",'r') as file:
        storedscore = file.read()
        if int(storedscore) > 0:
            highScore = int(storedscore)
        elif file.read() == "":
            highScore = 0
    global MenuHelp, game_over, mainGame, Help, Home, Menu, platform1,platform2,platform3,Died
    while not game_over and not Help and not Home:

        #--------------3.1 Start displaying first group of obstacles------------------

        if Screens==0:
            Screen1 = True
            Screen1run = True
            Screens += 1

        #-------------3.2 Continue to run Game----------------

        while Screens >= 1 and not game_over and not Home:
            scoreCountText = font_1.render(score.__str__(), True, text_colour_1)
            highScoreCountText = font_1.render(highScore.__str__(), True, text_colour_1)
            scoreText = font_1.render(("Score:"), True, text_colour_1)
            highScoreText = font_1.render(("High Score:"), True, text_colour_1)

            #--------------3.2.1 Detect Keyboard inputs-----------------

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] and not Menu and not Died:
                man.x -= vel
                man.left = True
                man.right = False
                man.standing = False
            elif keys[pygame.K_RIGHT] and not Menu and not Died:
                man.x += vel
                man.right = True
                man.left = False
                man.standing = False
            else:
                man.standing = True
                man.walkCount = 0


            if not (man.isJump):

                if keys[pygame.K_UP] and not Menu and not Died:
                    man.isJump = True
                    man.right = False
                    man.left = False
                    man.walkCount = 0

            else:

                if man.jumpCount >= -10 and not Menu and not Died:
                    neg = 1
                    if man.jumpCount < 0:
                        neg = -1
                    man.y -= (man.jumpCount ** 2) * 0.5 * neg
                    man.jumpCount -= 1

                elif Menu or Died:
                    man.jumpCount -= 0
                elif man.y+playerHeight<=520:
                    modifier = 1
                    man.isJump = False
                    man.jumpCount = 10

            #----------------3.2.2 Randomly assign a collection of platforms------------------------

            while Screens == 1:
                n = random.randint(0, 2)
                if n == 0 and not(Screen1):
                    Screen1 = True
                    Screen1run = True
                    if counter == 2:
                        obstacle1x = obstacle2x + 780
                    if counter == 3:
                        obstacle1x = obstacle3x + 820
                    counter = 1
                    Screens += 1
                if n == 1 and not(Screen2):
                    Screen2 = True
                    Screen2run = True
                    if counter == 1:
                        obstacle2x = obstacle1x + 880
                    if counter == 3:
                        obstacle2x = obstacle3x + 780
                    counter = 2
                    Screens += 1

                if n == 2 and not(Screen3):
                    Screen3 = True
                    Screen3run = True
                    if counter == 1:
                        obstacle3x = obstacle1x + 880
                    if counter == 2:
                        obstacle3x = obstacle2x + 820
                    counter = 3
                    Screens += 1

            you_died_rect = [(Screen.get_width() - youDied.width) / 2, youDiedy - youDied.height,
                             youDied.width, youDied.height]

            #----------------3.2.3 Fall if not on a platform--------------------

            if not platform1 and not platform2 and not platform3 and not man.isJump and man.y + playerHeight < 520:
                man.y -= ((10 - modifier) ** 2) * 0.5 * -1
                modifier += 1

            #---------------3.2.4 Move platforms across the screen and the player if on a platform--------------
            if obstacley % (15 + variable) == 0 and not Menu and not Died:
                if Screen1:
                    obstacle1x -= 20
                if Screen2:
                    obstacle2x -= 20
                if Screen3:
                    obstacle3x -= 20
                if (platform1 or platform2 or platform3) and not man.isJump:
                    man.x -= 20
            #--------------3.2.5 Character Animation----------------------

            for r in range(len(walkRight)):
                walkRight[r] = pygame.transform.scale(walkRight[r], (playerWidth, playerHeight))
            for r in range(len(walkLeft)):
                walkLeft[r] = pygame.transform.scale(walkLeft[r], (playerWidth, playerHeight))

            #-------------3.2.6 Control first group of platforms------------------

            if Screen1 and not game_over:
                Clock.tick(24)

                #-------------------3.2.6.1 Detect when Screen 1 is beyond the right side of the screen-----------------

                if Screen1pos4+obstacle1x <= 520 and Screen1run:
                    Screens -= 1
                    Screen1run = False

                #------------------3.2.6.2 Detect that the player is over a platform-----------------

                if man.isJump:
                    if (Screen1pos1 + obstacle1x + ObstacleImage1.get_width() > man.x > Screen1pos1 + obstacle1x and man.y+playerHeight>Screen1pos1y+15):
                        over1 = True
                    elif (Screen1pos2 + obstacle1x + ObstacleImage2.get_width() > man.x > Screen1pos2 + obstacle1x and man.y+playerHeight>Screen1pos2y+15):
                        over1 = True
                    elif (Screen1pos3 + obstacle1x + ObstacleImage2.get_width() > man.x > Screen1pos3 + obstacle1x and man.y+playerHeight>Screen1pos3y+15):
                        over1 = True
                    elif (Screen1pos4 + obstacle1x + ObstacleImage1.get_width() > man.x > Screen1pos4 + obstacle1x and man.y+playerHeight>Screen1pos4y+15):
                        over1 = True

                #------------------3.2.6.3 If player has moved from above a platform to below, move to on the platform------------------

                if over1 and man.y + playerHeight > Screen1pos1y+15 and Screen1pos1 + obstacle1x + ObstacleImage1.get_width() > man.x > Screen1pos1 + obstacle1x:
                    man.y = Screen1pos1y+15 - playerHeight

                elif over1 and man.y + playerHeight > Screen1pos2y+15 and Screen1pos2 + obstacle1x + ObstacleImage2.get_width() > man.x > Screen1pos2 + obstacle1x:
                    man.y = Screen1pos2y+15 - playerHeight

                elif over1 and man.y + playerHeight > Screen1pos3y+15 and Screen1pos3 + obstacle1x + ObstacleImage2.get_width() > man.x > Screen1pos3 + obstacle1x:
                    man.y = Screen1pos3y+15 - playerHeight

                elif over1 and man.y + playerHeight > Screen1pos4y+15 and Screen1pos4 + obstacle1x + ObstacleImage1.get_width() > man.x > Screen1pos4 + obstacle1x:
                    man.y = Screen1pos4y+15 - playerHeight

                if not man.isJump:
                    over1 = False

                #--------------------------3.2.6.4 If the player has moved into the object horizontally, move them next to the object-------------------

                if man.x+playerWidth>Screen1pos1+obstacle1x:
                    if man.y+playerHeight>Screen1pos1y+15 and man.y < Screen1pos1y+15 + ObstacleImage1Height:
                        if man.x<Screen1pos1+obstacle1x:
                            man.x = Screen1pos1 + obstacle1x - playerWidth+1
                if man.x<Screen1pos1+obstacle1x+ObstacleImage1.get_width():
                    if man.y+playerHeight>Screen1pos1y+15 and man.y < Screen1pos1y+15 + ObstacleImage1Height:
                        if man.x>Screen1pos1+obstacle1x:
                            man.x = Screen1pos1+obstacle1x+ObstacleImage1.get_width()

                if man.x + playerWidth > Screen1pos2 + obstacle1x:
                    if man.y + playerHeight > Screen1pos2y+15 and man.y < Screen1pos2y+15 + ObstacleImage2Height:
                        if man.x < Screen1pos2 + obstacle1x:
                            man.x = Screen1pos2 + obstacle1x - playerWidth + 1
                if man.x < Screen1pos2 + obstacle1x + ObstacleImage2.get_width():
                    if man.y + playerHeight > Screen1pos2y+15 and man.y < Screen1pos2y+15 + ObstacleImage2Height:
                        if man.x > Screen1pos2 + obstacle1x:
                            man.x = Screen1pos2 + obstacle1x + ObstacleImage2.get_width()

                if man.x + playerWidth > Screen1pos3 + obstacle1x:
                    if man.y + playerHeight > Screen1pos3y+15 and man.y < Screen1pos3y+15 + ObstacleImage2Height:
                        if man.x < Screen1pos3 + obstacle1x:
                            man.x = Screen1pos3 + obstacle1x - playerWidth + 1
                if man.x < Screen1pos3 + obstacle1x + ObstacleImage2.get_width():
                    if man.y + playerHeight > Screen1pos3y+15 and man.y < Screen1pos3y+15 + ObstacleImage2Height:
                        if man.x > Screen1pos3 + obstacle1x:
                            man.x = Screen1pos3 + obstacle1x + ObstacleImage2.get_width()

                if man.x + playerWidth > Screen1pos4 + obstacle1x:
                    if man.y + playerHeight > Screen1pos4y+15 and man.y < Screen1pos4y+15 + ObstacleImage1Height:
                        if man.x < Screen1pos4 + obstacle1x:
                            man.x = Screen1pos4 + obstacle1x - playerWidth + 1
                if man.x < Screen1pos4 + obstacle1x + ObstacleImage1.get_width():
                    if man.y + playerHeight > Screen1pos4y+15 and man.y < Screen1pos4y+15 + ObstacleImage1Height:
                        if man.x > Screen1pos4 + obstacle1x:
                            man.x = Screen1pos4 + obstacle1x + ObstacleImage1.get_width()

                #---------------------3.2.6.5 Detects if the player is on a platform, and determines which platform-------------------

                if not man.isJump:
                    if Screen1pos1 + obstacle1x + ObstacleImage1.get_width() > man.x > Screen1pos1 + obstacle1x or Screen1pos1 + obstacle1x + ObstacleImage1.get_width() > man.x + playerWidth > Screen1pos1 + obstacle1x:
                        if man.y + playerHeight == Screen1pos1y+15:
                            Screen1obstacle1 = True
                            platform1 = True
                    if Screen1pos2 + obstacle1x + ObstacleImage2.get_width() > man.x > Screen1pos2 + obstacle1x or Screen1pos2 + obstacle1x + ObstacleImage2.get_width() > man.x + playerWidth > Screen1pos2 + obstacle1x:
                        if man.y + playerHeight == Screen1pos2y+15:
                            Screen1obstacle2 = True
                            platform1 = True
                    if Screen1pos3 + obstacle1x + ObstacleImage2.get_width() > man.x > Screen1pos3 + obstacle1x or Screen1pos3 + obstacle1x + ObstacleImage2.get_width() > man.x + playerWidth > Screen1pos3 + obstacle1x:
                        if man.y + playerHeight == Screen1pos3y+15:
                            Screen1obstacle3 = True
                            platform1 = True
                    if Screen1pos4 + obstacle1x + ObstacleImage1.get_width() > man.x > Screen1pos4 + obstacle1x or Screen1pos4 + obstacle1x + ObstacleImage1.get_width() > man.x + playerWidth > Screen1pos4 + obstacle1x:
                        if man.y + playerHeight == Screen1pos4y+15:
                            Screen1obstacle4 = True
                            platform1 = True

                #-------------------3.2.6.6 Detects when the player has moved of a platform------------------

                if Screen1obstacle1 and not Screen1pos1 + obstacle1x + ObstacleImage1.get_width() > man.x > Screen1pos1 + obstacle1x and not Screen1pos1 + obstacle1x + ObstacleImage1.get_width() > man.x + playerWidth > Screen1pos1 + obstacle1x:
                    neg = -1
                    man.y -= (man.jumpCount ** 2) * 0.5 * neg
                    man.jumpCount -= 1
                    platform1 = False
                    Screen1obstacle1 = False

                elif Screen1obstacle2 and not Screen1pos2 + obstacle1x + ObstacleImage2.get_width() > man.x > Screen1pos2 + obstacle1x and not Screen1pos2 + obstacle1x + ObstacleImage2.get_width() > man.x + playerWidth > Screen1pos2 + obstacle1x:
                    neg = -1
                    man.y -= (man.jumpCount ** 2) * 0.5 * neg
                    man.jumpCount -= 1
                    platform1 = False
                    Screen1obstacle2 = False

                elif Screen1obstacle3 and not Screen1pos3 + obstacle1x + ObstacleImage2.get_width() > man.x > Screen1pos3 + obstacle1x and not Screen1pos3 + obstacle1x + ObstacleImage2.get_width() > man.x + playerWidth > Screen1pos3 + obstacle1x:
                    neg = -1
                    man.y -= (man.jumpCount ** 2) * 0.5 * neg
                    man.jumpCount -= 1
                    platform1 = False
                    Screen1obstacle3 = False

                elif Screen1obstacle4 and not Screen1pos4 + obstacle1x + ObstacleImage1.get_width() > man.x > Screen1pos4 + obstacle1x and not Screen1pos4 + obstacle1x + ObstacleImage1.get_width() > man.x + playerWidth > Screen1pos4 + obstacle1x:
                    neg = -1
                    man.y -= (man.jumpCount ** 2) * 0.5 * neg
                    man.jumpCount -= 1
                    platform1 = False
                    Screen1obstacle4 = False


                Screen.blit(playGameImage, (0, 0))

                if obstacle1x <= -750:
                    Screen1 = False
                    obstacle1x = 520

                if obstacley % 1000 == 0:
                    variable -= 1
                if variable < 1:
                    variable = 1

            # -------------3.2.7 Control second group of platforms------------------

            if Screen2 and not game_over:
                Clock.tick(24)

                # -------------------3.2.7.1 Detect when Screen 1 is beyond the right side of the screen-----------------

                if Screen2pos4+obstacle2x <= 520 and Screen2run:
                    Screens -= 1
                    Screen2run = False

                # ------------------3.2.7.2 Detect that the player is over a platform-----------------

                if man.isJump:
                    if (Screen2pos1 + obstacle2x + ObstacleImage2.get_width() > man.x > Screen2pos1 + obstacle2x and man.y+playerHeight>Screen2pos1y+15):
                        over2 = True
                    elif (Screen2pos2 + obstacle2x + ObstacleImage1.get_width() > man.x > Screen2pos2 + obstacle2x and man.y+playerHeight>Screen2pos2y+15):
                        over2 = True
                    elif (Screen2pos3 + obstacle2x + ObstacleImage2.get_width() > man.x > Screen2pos3 + obstacle2x and man.y+playerHeight>Screen2pos3y+15):
                        over2 = True
                    elif (Screen2pos4 + obstacle2x + ObstacleImage1.get_width() > man.x > Screen2pos4 + obstacle2x and man.y+playerHeight>Screen2pos4y+15):
                        over2 = True

                # ------------------3.2.7.3 If player has moved from above a platform to below, move to on the platform------------------

                if over2 and man.y + playerHeight > Screen2pos1y+15 and Screen2pos1 + obstacle2x + ObstacleImage2.get_width() > man.x > Screen2pos1 + obstacle2x:
                    man.y = Screen2pos1y+15 - playerHeight

                elif over2 and man.y + playerHeight > Screen2pos2y+15 and Screen2pos2 + obstacle2x + ObstacleImage1.get_width() > man.x > Screen2pos2 + obstacle2x:
                    man.y = Screen2pos2y+15 - playerHeight

                elif over2 and man.y + playerHeight > Screen2pos3y+15 and Screen2pos3 + obstacle2x + ObstacleImage2.get_width() > man.x > Screen2pos3 + obstacle2x:
                    man.y = Screen2pos3y+15 - playerHeight

                elif over2 and man.y + playerHeight > Screen2pos4y+15 and Screen2pos4 + obstacle2x + ObstacleImage1.get_width() > man.x > Screen2pos4 + obstacle2x:
                    man.y = Screen2pos4y+15 - playerHeight

                if not man.isJump:
                    over2 = False

                # --------------------------3.2.7.4 If the player has moved into the object horizontally, move them next to the object-------------------

                if man.x+playerWidth>Screen2pos1+obstacle2x:
                    if man.y+playerHeight>Screen2pos1y+15 and man.y < Screen2pos1y+15 + ObstacleImage2Height:
                        if man.x<Screen2pos1+obstacle2x:
                            man.x = Screen2pos1 + obstacle2x - playerWidth+1
                if man.x<Screen2pos1+obstacle2x+ObstacleImage2.get_width():
                    if man.y+playerHeight>Screen2pos1y+15 and man.y < Screen2pos1y+15 + ObstacleImage2Height:
                        if man.x>Screen2pos1+obstacle2x:
                            man.x = Screen2pos1+obstacle2x+ObstacleImage2.get_width()

                if man.x + playerWidth > Screen2pos2 + obstacle2x:
                    if man.y + playerHeight > Screen2pos2y+15 and man.y < Screen2pos2y+15 + ObstacleImage1Height:
                        if man.x < Screen2pos2 + obstacle2x:
                            man.x = Screen2pos2 + obstacle2x - playerWidth + 1
                if man.x < Screen2pos2 + obstacle2x + ObstacleImage1.get_width():
                    if man.y + playerHeight > Screen2pos2y+15 and man.y < Screen2pos2y+15 + ObstacleImage1Height:
                        if man.x > Screen2pos2 + obstacle2x:
                            man.x = Screen2pos2 + obstacle2x + ObstacleImage1.get_width()

                if man.x + playerWidth > Screen2pos3 + obstacle2x:
                    if man.y + playerHeight > Screen2pos3y+15 and man.y < Screen2pos3y+15 + ObstacleImage2Height:
                        if man.x < Screen2pos3 + obstacle2x:
                            man.x = Screen2pos3 + obstacle2x - playerWidth + 1
                if man.x < Screen2pos3 + obstacle2x + ObstacleImage2.get_width():
                    if man.y + playerHeight > Screen2pos3y+15 and man.y < Screen2pos3y+15 + ObstacleImage2Height:
                        if man.x > Screen2pos3 + obstacle2x:
                            man.x = Screen2pos3 + obstacle2x + ObstacleImage2.get_width()

                if man.x + playerWidth > Screen2pos4 + obstacle2x:
                    if man.y + playerHeight > Screen2pos4y+15 and man.y < Screen2pos4y+15 + ObstacleImage1Height:
                        if man.x < Screen2pos4 + obstacle2x:
                            man.x = Screen2pos4 + obstacle2x - playerWidth + 1
                if man.x < Screen2pos4 + obstacle2x + ObstacleImage1.get_width():
                    if man.y + playerHeight > Screen2pos4y+15 and man.y < Screen2pos4y+15 + ObstacleImage1Height:
                        if man.x > Screen2pos4 + obstacle2x:
                            man.x = Screen2pos4 + obstacle2x + ObstacleImage1.get_width()

                # ---------------------3.2.7.5 Detects if the player is on a platform, and determines which platform-------------------

                if not man.isJump:
                    if Screen2pos1 + obstacle2x + ObstacleImage2.get_width() > man.x > Screen2pos1 + obstacle2x or Screen2pos1 + obstacle2x + ObstacleImage2.get_width() > man.x + playerWidth > Screen2pos1 + obstacle2x:
                        if man.y + playerHeight == Screen2pos1y+15:
                            Screen2obstacle1 = True
                            platform2 = True
                    if Screen2pos2 + obstacle2x + ObstacleImage1.get_width() > man.x > Screen2pos2 + obstacle2x or Screen2pos2 + obstacle2x + ObstacleImage1.get_width() > man.x + playerWidth > Screen2pos2 + obstacle2x:
                        if man.y + playerHeight == Screen2pos2y+15:
                            Screen2obstacle2 = True
                            platform2 = True
                    if Screen2pos3 + obstacle2x + ObstacleImage2.get_width() > man.x > Screen2pos3 + obstacle2x or Screen2pos3 + obstacle2x + ObstacleImage2.get_width() > man.x + playerWidth > Screen2pos3 + obstacle2x:
                        if man.y + playerHeight == Screen2pos3y+15:
                            Screen2obstacle3 = True
                            platform2 = True
                    if Screen2pos4 + obstacle2x + ObstacleImage1.get_width() > man.x > Screen2pos4 + obstacle2x or Screen2pos4 + obstacle2x + ObstacleImage1.get_width() > man.x + playerWidth > Screen2pos4 + obstacle2x:
                        if man.y + playerHeight == Screen2pos4y+15:
                            Screen2obstacle4 = True
                            platform2 = True

                # -------------------3.2.7.6 Detects when the player has moved of a platform------------------

                if Screen2obstacle1 and not Screen2pos1 + obstacle2x + ObstacleImage2.get_width() > man.x > Screen2pos1 + obstacle2x and not Screen2pos1 + obstacle2x + ObstacleImage2.get_width() > man.x + playerWidth > Screen2pos1 + obstacle2x:
                    neg = -1
                    man.y -= (man.jumpCount ** 2) * 0.5 * neg
                    man.jumpCount -= 1
                    platform2 = False
                    Screen2obstacle1 = False

                elif Screen2obstacle2 and not Screen2pos2 + obstacle2x + ObstacleImage1.get_width() > man.x > Screen2pos2 + obstacle2x and not Screen2pos2 + obstacle2x + ObstacleImage1.get_width() > man.x + playerWidth > Screen2pos2 + obstacle2x:
                    neg = -1
                    man.y -= (man.jumpCount ** 2) * 0.5 * neg
                    man.jumpCount -= 1
                    platform2 = False
                    Screen2obstacle2 = False

                elif Screen2obstacle3 and not Screen2pos3 + obstacle2x + ObstacleImage2.get_width() > man.x > Screen2pos3 + obstacle2x and not Screen2pos3 + obstacle2x + ObstacleImage2.get_width() > man.x + playerWidth > Screen2pos3 + obstacle2x:
                    neg = -1
                    man.y -= (man.jumpCount ** 2) * 0.5 * neg
                    man.jumpCount -= 1
                    platform2 = False
                    Screen2obstacle3 = False

                elif Screen2obstacle4 and not Screen2pos4 + obstacle2x + ObstacleImage1.get_width() > man.x > Screen2pos4 + obstacle2x and not Screen2pos4 + obstacle2x + ObstacleImage1.get_width() > man.x + playerWidth > Screen2pos4 + obstacle2x:
                    neg = -1
                    man.y -= (man.jumpCount ** 2) * 0.5 * neg
                    man.jumpCount -= 1
                    platform2 = False
                    Screen2obstacle4 = False

                Screen.blit(playGameImage, (0, 0))

                if obstacle2x <= -750:
                    Screen2 = False
                    obstacle2x = 520

                if obstacley % 1000 == 0:
                    variable -= 1
                if variable < 1:
                    variable = 1

            # -------------3.2.8 Control third group of platforms------------------

            if Screen3 and not game_over:
                Clock.tick(24)

                # -------------------3.2.8.1 Detect when Screen 1 is beyond the right side of the screen-----------------

                if Screen3pos4+obstacle3x <= 520 and Screen3run:
                    Screens -= 1
                    Screen3run = False

                # ------------------3.2.8.2 Detect that the player is over a platform-----------------

                if man.isJump:
                    if (Screen3pos1 + obstacle3x + ObstacleImage2.get_width() > man.x > Screen3pos1 + obstacle3x and man.y+playerHeight>Screen3pos1y+15):
                        over3 = True
                    elif (Screen3pos2 + obstacle3x + ObstacleImage1.get_width() > man.x > Screen3pos2 + obstacle3x and man.y+playerHeight>Screen3pos2y+15):
                        over3 = True
                    elif (Screen3pos3 + obstacle3x + ObstacleImage1.get_width() > man.x > Screen3pos3 + obstacle3x and man.y+playerHeight>Screen3pos3y+15):
                        over3 = True
                    elif (Screen3pos4 + obstacle3x + ObstacleImage2.get_width() > man.x > Screen3pos4 + obstacle3x and man.y+playerHeight>Screen3pos4y+15):
                        over3 = True

                # ------------------3.2.8.3 If player has moved from above a platform to below, move to on the platform------------------

                if over3 and man.y + playerHeight > Screen3pos1y+15 and Screen3pos1 + obstacle3x + ObstacleImage2.get_width() > man.x > Screen3pos1 + obstacle3x:
                    man.y = Screen3pos1y+15 - playerHeight

                elif over3 and man.y + playerHeight > Screen3pos2y+15 and Screen3pos2 + obstacle3x + ObstacleImage1.get_width() > man.x > Screen3pos2 + obstacle3x:
                    man.y = Screen3pos2y+15 - playerHeight

                elif over3 and man.y + playerHeight > Screen3pos3y+15 and Screen3pos3 + obstacle3x + ObstacleImage1.get_width() > man.x > Screen3pos3 + obstacle3x:
                    man.y = Screen3pos3y+15 - playerHeight

                elif over3 and man.y + playerHeight > Screen3pos4y+15 and Screen3pos4 + obstacle3x + ObstacleImage2.get_width() > man.x > Screen3pos4 + obstacle3x:
                    man.y = Screen3pos4y+15 - playerHeight

                if not man.isJump:
                    over3 = False

                # --------------------------3.2.8.4 If the player has moved into the object horizontally, move them next to the object-------------------

                if man.x+playerWidth>Screen3pos1+obstacle3x:
                    if man.y+playerHeight>Screen3pos1y+15 and man.y < Screen3pos1y+15 + ObstacleImage2Height:
                        if man.x<Screen3pos1+obstacle3x:
                            man.x = Screen3pos1 + obstacle3x - playerWidth+1
                if man.x<Screen3pos1+obstacle3x+ObstacleImage2.get_width():
                    if man.y+playerHeight>Screen3pos1y+15 and man.y < Screen3pos1y+15 + ObstacleImage2Height:
                        if man.x>Screen3pos1+obstacle3x:
                            man.x = Screen3pos1+obstacle3x+ObstacleImage2.get_width()

                if man.x + playerWidth > Screen3pos2 + obstacle3x:
                    if man.y + playerHeight > Screen3pos2y+15 and man.y < Screen3pos2y+15 + ObstacleImage1Height:
                        if man.x < Screen3pos2 + obstacle3x:
                            man.x = Screen3pos2 + obstacle3x - playerWidth + 1
                if man.x < Screen3pos2 + obstacle3x + ObstacleImage1.get_width():
                    if man.y + playerHeight > Screen3pos2y+15 and man.y < Screen3pos2y+15 + ObstacleImage1Height:
                        if man.x > Screen3pos2 + obstacle3x:
                            man.x = Screen3pos2 + obstacle3x + ObstacleImage1.get_width()

                if man.x + playerWidth > Screen3pos3 + obstacle3x:
                    if man.y + playerHeight > Screen3pos3y+15 and man.y < Screen3pos3y+15 + ObstacleImage1Height:
                        if man.x < Screen3pos3 + obstacle3x:
                            man.x = Screen3pos3 + obstacle3x - playerWidth + 1
                if man.x < Screen3pos3 + obstacle3x + ObstacleImage1.get_width():
                    if man.y + playerHeight > Screen3pos3y+15 and man.y < Screen3pos3y+15 + ObstacleImage1Height:
                        if man.x > Screen3pos3 + obstacle3x:
                            man.x = Screen3pos3 + obstacle3x + ObstacleImage1.get_width()

                if man.x + playerWidth > Screen3pos4 + obstacle3x:
                    if man.y + playerHeight > Screen3pos4y+15 and man.y < Screen3pos4y+15 + ObstacleImage2Height:
                        if man.x < Screen3pos4 + obstacle3x:
                            man.x = Screen3pos4 + obstacle3x - playerWidth + 1
                if man.x < Screen3pos4 + obstacle3x + ObstacleImage2.get_width():
                    if man.y + playerHeight > Screen3pos4y+15 and man.y < Screen3pos4y+15 + ObstacleImage2Height:
                        if man.x > Screen3pos4 + obstacle3x:
                            man.x = Screen3pos4 + obstacle3x + ObstacleImage2.get_width()

                # ---------------------3.2.8.5 Detects if the player is on a platform, and determines which platform-------------------

                if not man.isJump:
                    if Screen3pos1 + obstacle3x + ObstacleImage2.get_width() > man.x > Screen3pos1 + obstacle3x or Screen3pos1 + obstacle3x + ObstacleImage2.get_width() > man.x + playerWidth > Screen3pos1 + obstacle3x:
                        if man.y + playerHeight == Screen3pos1y+15:
                            Screen3obstacle1 = True
                            platform3 = True
                    if Screen3pos2 + obstacle3x + ObstacleImage1.get_width() > man.x > Screen3pos2 + obstacle3x or Screen3pos2 + obstacle3x + ObstacleImage1.get_width() > man.x + playerWidth > Screen3pos2 + obstacle3x:
                        if man.y + playerHeight == Screen3pos2y+15:
                            Screen3obstacle2 = True
                            platform3 = True
                    if Screen3pos3 + obstacle3x + ObstacleImage1.get_width() > man.x > Screen3pos3 + obstacle3x or Screen3pos3 + obstacle3x + ObstacleImage1.get_width() > man.x + playerWidth > Screen3pos3 + obstacle3x:
                        if man.y + playerHeight == Screen3pos3y+15:
                            Screen3obstacle3 = True
                            platform3 = True
                    if Screen3pos4 + obstacle3x + ObstacleImage2.get_width() > man.x > Screen3pos4 + obstacle3x or Screen3pos4 + obstacle3x + ObstacleImage2.get_width() > man.x + playerWidth > Screen3pos4 + obstacle3x:
                        if man.y + playerHeight == Screen3pos4y+15:
                            Screen3obstacle4 = True
                            platform3 = True

                # -------------------3.2.8.6 Detects when the player has moved of a platform------------------

                if Screen3obstacle1 and not Screen3pos1 + obstacle3x + ObstacleImage2.get_width() > man.x > Screen3pos1 + obstacle3x and not Screen3pos1 + obstacle3x + ObstacleImage2.get_width() > man.x + playerWidth > Screen3pos1 + obstacle3x:
                    neg = -1
                    man.y -= (man.jumpCount ** 2) * 0.5 * neg
                    man.jumpCount -= 1
                    platform3 = False
                    Screen3obstacle1 = False

                elif Screen3obstacle2 and not Screen3pos2 + obstacle3x + ObstacleImage1.get_width() > man.x > Screen3pos2 + obstacle3x and not Screen3pos2 + obstacle3x + ObstacleImage1.get_width() > man.x + playerWidth > Screen3pos2 + obstacle3x:
                    neg = -1
                    man.y -= (man.jumpCount ** 2) * 0.5 * neg
                    man.jumpCount -= 1
                    platform3 = False
                    Screen3obstacle2 = False

                elif Screen3obstacle3 and not Screen3pos3 + obstacle3x + ObstacleImage1.get_width() > man.x > Screen3pos3 + obstacle3x and not Screen3pos3 + obstacle3x + ObstacleImage1.get_width() > man.x + playerWidth > Screen3pos3 + obstacle3x:
                    neg = -1
                    man.y -= (man.jumpCount ** 2) * 0.5 * neg
                    man.jumpCount -= 1
                    platform3 = False
                    Screen3obstacle3 = False

                elif Screen3obstacle4 and not Screen3pos4 + obstacle3x + ObstacleImage2.get_width() > man.x > Screen3pos4 + obstacle3x and not Screen3pos4 + obstacle3x + ObstacleImage2.get_width() > man.x + playerWidth > Screen3pos4 + obstacle3x:
                    neg = -1
                    man.y -= (man.jumpCount ** 2) * 0.5 * neg
                    man.jumpCount -= 1
                    platform3 = False
                    Screen3obstacle4 = False

                Screen.blit(playGameImage, (0, 0))

                if obstacle3x <= -750:
                    Screen3 = False
                    obstacle3x = 520

                if obstacley % 1000 == 0 and not Menu and not Died:
                    variable -= 1
                if variable < 1:
                    variable = 1

            #--------------------3.9 Move the background------------------------

            if not Menu:
                background1x -= 1
                background2x -= 1

            #-------------------3.10 Detect when the player has passed the first obstacle--------------------
            
            if man.x+playerWidth>=Screen1pos1+obstacle1x:
                Begin = True

            Screen.blit(playGameImage, (0 + background1x, 0))
            Screen.blit(playGameImage, (0 + background2x, 0))
            
            #-------------------3.11 Loop the background------------------------
            
            if background1x == -playGameImage.get_width():
                background1x = background2x + playGameImage.get_width()
            if background2x == -playGameImage.get_width():
                background2x = background1x + playGameImage.get_width()

            Screen.blit(DropdownImage, ((Screen.get_width()-DropdownImageWidth)/2, Screeny-DropdownImageWidth-80))
            pygame.draw.rect(Screen, menuButton.colour, menu_button_rect)

            #--------------3.12 Draw first screen of the dropdown menu---------------

            if not MenuHelp:
                Screen.blit(ButtonImage, ((Screen.get_width() - ButtonImageWidth) / 2 + 10, Screeny - (Screen.get_height() - ButtonImageHeight) / 2 + 50))
                Screen.blit(ButtonImage,
                            ((Screen.get_width() - ButtonImageWidth) / 2 + 10,
                             Screeny - (Screen.get_height() - ButtonImageHeight) / 2 - 10))
                Screen.blit(ButtonImage,
                            ((Screen.get_width() - ButtonImageWidth) / 2 + 10,
                             Screeny - (Screen.get_height() - ButtonImageHeight) / 2 + 110))

            #-------------------3.13 Draw the second screen of the dropdown menu---------------------------------

            if MenuHelp:
                Screen.blit(ButtonImage,((Screen.get_width() - ButtonImageWidth) / 2 + 10,
                             Screeny - (Screen.get_height() - ButtonImageHeight) / 2 + 110))
                Screen.blit(ButtonImage, ((Screen.get_width() - ButtonImageWidth) / 2,
                                          youDiedy - ButtonImageHeight - 10))

            pygame.draw.rect(Screen, youDied.colour, you_died_rect)
            Screen.blit(ButtonImage,((Screen.get_width() - ButtonImageWidth)/2,
                                        youDiedy - ButtonImageHeight-10))
            Screen.blit(ButtonImage,((Screen.get_width() - ButtonImageWidth) / 2,
                                        youDiedy - ButtonImageHeight-70))


            #---------------------3.14 Detect and respond to events----------------------

            for event in pygame.event.get():

                #-------------3.14.1 Quit-----------------

                if event.type == pygame.QUIT:
                    game_over = True

                #-----------3.14.2 Mousebuttonup-------------

                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = event.pos
                    if (menu_button_rect[0] <= x <= menu_button_rect[0] + menu_button_rect[2] and
                            menu_button_rect[
                                1] <= y <= menu_button_rect[1] + menu_button_rect[3]):
                        if Menu:
                            Menu = False
                            MenuHelp = False
                        elif not Menu and not Died:
                            Menu = True
                    if Menu and not MenuHelp and (
                            (Screen.get_width() - ButtonImageWidth) / 2 <= x <= (Screen.get_width() - ButtonImageWidth) / 2 + ButtonImageWidth and
                            Screeny - (Screen.get_height() - ButtonImageHeight) / 2 + 110 <= y <= Screeny - (Screen.get_height() - ButtonImageHeight) / 2 + 110 + ButtonImageHeight):
                        game_over = True
                    if Menu and not MenuHelp and (
                            (Screen.get_width() - ButtonImageWidth) / 2 <= x <= (Screen.get_width() - ButtonImageWidth) / 2 + ButtonImageWidth and
                            Screeny - (Screen.get_height() - ButtonImageHeight) / 2 + 50 <= y <= Screeny - (Screen.get_height() - ButtonImageHeight) / 2 + 50 + ButtonImageHeight):
                        Menu = False
                        mainGame = False
                        Home = True
                        Screen1 = False
                        Screen1run = False
                        Screen2 = False
                        Screen2run = False
                        Screen3 = False
                        Screen3run = False
                    if Menu and not MenuHelp and (
                            (Screen.get_width() - ButtonImageWidth) / 2 <= x <= (Screen.get_width() - ButtonImageWidth) / 2 + ButtonImageWidth and
                            Screeny - (Screen.get_height() - ButtonImageHeight) / 2 - 10 <= y <= Screeny - (Screen.get_height() - ButtonImageHeight) / 2 - 10 + ButtonImageHeight):
                        MenuHelp = True

                    if MenuHelp and (
                            (Screen.get_width() - ButtonImageWidth) / 2 <= x <= (Screen.get_width() - ButtonImageWidth) / 2 + ButtonImageWidth and
                            Screeny - (Screen.get_height() - ButtonImageHeight) / 2 + 110 <= y <= Screeny - (Screen.get_height() - ButtonImageHeight) / 2 + 110 + ButtonImageHeight):
                        MenuHelp = False
                    if Died and (
                            (Screen.get_width() - ButtonImageWidth) / 2 <= x <= (Screen.get_width() - ButtonImageWidth) / 2  + ButtonImageWidth and
                            youDiedy - ButtonImageHeight - 70 <= y <= youDiedy - ButtonImageHeight - 70 + ButtonImageHeight):
                        Menu = False
                        mainGame = False
                        Home = True
                        Screen1 = False
                        Screen1run = False
                        Screen2 = False
                        Screen2run = False
                        Screen3 = False
                        Screen3run = False
                        Screen4 = False
                    if Died and (
                            (Screen.get_width() - ButtonImageWidth) / 2 <= x <= (Screen.get_width() - ButtonImageWidth) / 2  + ButtonImageWidth and
                            youDiedy - ButtonImageHeight - 10 <= y <= youDiedy - ButtonImageHeight - 10 + ButtonImageHeight):
                        Clock = pygame.time.Clock()
                        obstacle1x = 520
                        obstacle2x = 520
                        obstacle3x = 520
                        obstacley = 0
                        background1x = 0
                        background2x = 1920
                        variable = 0
                        counter = 1
                        score = 0
                        Screen1 = False
                        Screen2 = False
                        Screen3 = False
                        Screen1run = False
                        Screen2run = False
                        Screen3run = False
                        platform1 = False
                        platform2 = False
                        platform3 = False
                        Screen1obstacle1 = False
                        Screen1obstacle2 = False
                        Screen1obstacle3 = False
                        Screen1obstacle4 = False
                        Screen2obstacle1 = False
                        Screen2obstacle2 = False
                        Screen2obstacle3 = False
                        Screen2obstacle4 = False
                        Screen3obstacle1 = False
                        Screen3obstacle2 = False
                        Screen3obstacle3 = False
                        Screen3obstacle4 = False
                        Screen4obstacle1 = False
                        Screen4obstacle2 = False
                        Screen4obstacle3 = False
                        Screen4obstacle4 = False
                        Screens = 0
                        man.x = 100
                        Died = False
                        Begin = False

                #-----------------3.14.3 Mousemotion---------------

                if event.type == pygame.MOUSEMOTION:
                    x, y = event.pos
            if (menu_button_rect[0] <= x <= menu_button_rect[0] + menu_button_rect[2] and menu_button_rect[
                1] <= y <= menu_button_rect[1] + menu_button_rect[3]):
                pygame.draw.rect(Screen, menuButton.over_colour, menu_button_rect)
            if Menu and not MenuHelp and ((Screen.get_width() - ButtonImageWidth) / 2 + 10 <= x <= (Screen.get_width() - ButtonImageWidth) / 2 + 10 + ButtonImageWidth and
                         Screeny - (Screen.get_height() - ButtonImageHeight) / 2 + 110 <= y <= Screeny - (Screen.get_height() - ButtonImageHeight) / 2 + 110 + ButtonImageHeight):

                Screen.blit(ButtonOverImage,
                            ((Screen.get_width() - ButtonImageWidth) / 2 + 10,
                             Screeny - (Screen.get_height() - ButtonImageHeight) / 2 + 110))

            if Menu and not MenuHelp and ((Screen.get_width() - ButtonImageWidth) / 2 + 10 <= x <= (Screen.get_width() - ButtonImageWidth) / 2 + 10 + ButtonImageWidth and
                         Screeny - (Screen.get_height() - ButtonImageHeight) / 2 + 50 <= y <= Screeny - (Screen.get_height() - ButtonImageHeight) / 2 + 50 + ButtonImageHeight):
                Screen.blit(ButtonOverImage, ((Screen.get_width() - ButtonImageWidth) / 2 + 10, Screeny - (Screen.get_height() - ButtonImageHeight) / 2 + 50))

            if Menu and not MenuHelp and ((Screen.get_width() - ButtonImageWidth) / 2 + 10 <= x <= (Screen.get_width() - ButtonImageWidth) / 2 + 10 + ButtonImageWidth and
                         Screeny - (Screen.get_height() - ButtonImageHeight) / 2 - 10 <= y <= Screeny - (Screen.get_height() - ButtonImageHeight) / 2 - 10 + ButtonImageHeight):
                Screen.blit(ButtonOverImage,
                            ((Screen.get_width() - ButtonImageWidth) / 2 + 10,
                             Screeny - (Screen.get_height() - ButtonImageHeight) / 2 - 10))

            if Died and (
                            (Screen.get_width() - ButtonImageWidth) / 2 <= x <= (Screen.get_width() - ButtonImageWidth) / 2  + ButtonImageWidth and
                            youDiedy - ButtonImageHeight - 70 <= y <= youDiedy - ButtonImageHeight - 70 + ButtonImageHeight):
                Screen.blit(ButtonOverImage, ((Screen.get_width() - ButtonImageWidth) / 2,
                                              youDiedy - ButtonImageHeight - 70))

            if Died and (
                            (Screen.get_width() - ButtonImageWidth) / 2 <= x <= (Screen.get_width() - ButtonImageWidth) / 2  + ButtonImageWidth and
                            youDiedy - ButtonImageHeight - 10 <= y <= youDiedy - ButtonImageHeight - 10 + ButtonImageHeight):
                Screen.blit(ButtonOverImage, ((Screen.get_width() - ButtonImageWidth) / 2,
                                              youDiedy - ButtonImageHeight-10))
            if (menu_button_rect[0] <= x <= menu_button_rect[0] + menu_button_rect[2] and menu_button_rect[
                1] <= y <= menu_button_rect[1] + menu_button_rect[3]):
                pygame.draw.rect(Screen, menuButton.over_colour, menu_button_rect)

            if MenuHelp and (
                            (Screen.get_width() - ButtonImageWidth) / 2 <= x <= (Screen.get_width() - ButtonImageWidth) / 2 + ButtonImageWidth and
                            Screeny - (Screen.get_height() - ButtonImageHeight) / 2 + 110 <= y <= Screeny - (Screen.get_height() - ButtonImageHeight) / 2 + 110 + ButtonImageHeight):
                Screen.blit(ButtonOverImage, ((Screen.get_width() - ButtonImageWidth) / 2 + 10,
                                          Screeny - (Screen.get_height() - ButtonImageHeight) / 2 + 110))


            obstacle(Screen1pos1 + obstacle1x, Screen1pos1y, ObstacleImage1.get_width(),
                     ObstacleImage1.get_height()).drawObstacle1(Screen)
            obstacle(Screen1pos2 + obstacle1x, Screen1pos2y, ObstacleImage2.get_width(),
                     ObstacleImage2.get_height()).drawObstacle2(Screen)
            obstacle(Screen1pos3 + obstacle1x, Screen1pos3y, ObstacleImage2.get_width(),
                     ObstacleImage2.get_height()).drawObstacle2(Screen)
            obstacle(Screen1pos4 + obstacle1x, Screen1pos4y, ObstacleImage1.get_width(),
                     ObstacleImage1.get_height()).drawObstacle1(Screen)

            obstacle(Screen2pos1 + obstacle2x, Screen2pos1y, ObstacleImage2.get_width(),
                     ObstacleImage2.get_height()).drawObstacle2(Screen)
            obstacle(Screen2pos2 + obstacle2x, Screen2pos2y, ObstacleImage1.get_width(),
                     ObstacleImage1.get_height()).drawObstacle1(Screen)
            obstacle(Screen2pos3 + obstacle2x, Screen2pos3y, ObstacleImage2.get_width(),
                     ObstacleImage2.get_height()).drawObstacle2(Screen)
            obstacle(Screen2pos4 + obstacle2x, Screen2pos4y, ObstacleImage1.get_width(),
                     ObstacleImage1.get_height()).drawObstacle1(Screen)

            obstacle(Screen3pos1 + obstacle3x, Screen3pos1y, ObstacleImage2.get_width(),
                     ObstacleImage2.get_height()).drawObstacle2(Screen)
            obstacle(Screen3pos2 + obstacle3x, Screen3pos2y, ObstacleImage1.get_width(),
                     ObstacleImage1.get_height()).drawObstacle1(Screen)
            obstacle(Screen3pos3 + obstacle3x, Screen3pos3y, ObstacleImage1.get_width(),
                     ObstacleImage1.get_height()).drawObstacle1(Screen)
            obstacle(Screen3pos4 + obstacle3x, Screen3pos4y, ObstacleImage2.get_width(),
                     ObstacleImage2.get_height()).drawObstacle2(Screen)

            man.draw(Screen)


            Screen.blit(restartButton.text,
                        ((Screen.get_width() - ButtonImageWidth) / 2 + (ButtonImageWidth - restartButton.text.get_width()) / 2,
                         youDiedy - ButtonImageHeight - 10 + (
                                 ButtonImageHeight / 2 - restartButton.text.get_height() / 2)))
            Screen.blit(homeButton.text,
                        ((Screen.get_width() - ButtonImageWidth) / 2 + (
                                    ButtonImageWidth - restartButton.text.get_width()) / 2,
                          youDiedy - ButtonImageHeight - 70 + (
                                 ButtonImageHeight / 2 - restartButton.text.get_height() / 2)))
            Screen.blit(diedName, (
                (Screen.get_width() - diedName.get_width()) / 2, youDiedy - diedName.get_height() - 140))
            Screen.blit(menuButton.text,
                        (menu_button_rect[0] + (menuButton.width - menuButton.text.get_width()) / 2,
                         menu_button_rect[1] + (menuButton.height / 2 - menuButton.text.get_height() / 2) - 2.5))

            #------------------3.15 Print text on first screen--------------------

            if not MenuHelp:
                Screen.blit(homeButton.text,
                            ((Screen.get_width() - ButtonImageWidth) / 2 + (ButtonImageWidth - helpButton.text.get_width()) / 2,
                             Screeny - (Screen.get_height() - ButtonImageHeight) / 2 + 50 + (
                                     ButtonImageHeight / 2 - helpButton.text.get_height() / 2)))
                Screen.blit(quitButton.text,
                            ((Screen.get_width() - ButtonImageWidth) / 2 + (ButtonImageWidth - quitButton.text.get_width()) / 2,
                             Screeny - (Screen.get_height() - ButtonImageHeight) / 2 + 110 + (
                                     ButtonImageHeight / 2 - quitButton.text.get_height() / 2)))
                Screen.blit(helpButton.text,
                            ((Screen.get_width() - ButtonImageWidth) / 2 + (ButtonImageWidth - helpButton.text.get_width()) / 2,
                             Screeny - (Screen.get_height() - ButtonImageHeight) / 2 - 10 + (
                                     ButtonImageHeight / 2 - helpButton.text.get_height() / 2)))
                Screen.blit(menuName, ((Screen.get_width() - menuName.get_width()) / 2,
                                       0 + (Screen.get_height() - menuName.get_height()) / 2 - 600 + Screeny))

            #-------------------------3.16 print text on second screen-------------------------

            if MenuHelp:
                Screen.blit(helpName, ((Screen.get_width() - helpName.get_width()) / 2,
                                       0 + (Screen.get_height() - helpName.get_height()) / 2 - 600 + Screeny))
                Screen.blit(helpText1, ((Screen.get_width() - helpText1.get_width()) / 2 + 10,
                                        0 + (Screen.get_height() - helpText1.get_height()) / 2 - 560 + Screeny))
                Screen.blit(helpText2, ((Screen.get_width() - helpText2.get_width()) / 2 + 10,
                                        0 + (Screen.get_height() - helpText2.get_height()) / 2 - 545 + Screeny))
                Screen.blit(helpText3, ((Screen.get_width() - helpText3.get_width()) / 2 + 10,
                                        0 + (Screen.get_height() - helpText3.get_height()) / 2 - 530 + Screeny))
                Screen.blit(helpText4, ((Screen.get_width() - helpText4.get_width()) / 2 + 10,
                                        0 + (Screen.get_height() - helpText4.get_height()) / 2 - 515 + Screeny))
                Screen.blit(helpText5, ((Screen.get_width() - helpText5.get_width()) / 2 + 10,
                                        0 + (Screen.get_height() - helpText5.get_height()) / 2 - 500 + Screeny))
                Screen.blit(helpText6, ((Screen.get_width() - helpText6.get_width()) / 2 + 10,
                                        0 + (Screen.get_height() - helpText6.get_height()) / 2 - 485 + Screeny))
                Screen.blit(helpText7, ((Screen.get_width() - helpText7.get_width()) / 2 + 10,
                                        0 + (Screen.get_height() - helpText7.get_height()) / 2 + 470 + Screeny))
                Screen.blit(helpText8, ((Screen.get_width() - helpText8.get_width()) / 2 + 10,
                                        0 + (Screen.get_height() - helpText8.get_height()) / 2 + 355 + Screeny))
                Screen.blit(helpText9, ((Screen.get_width() - helpText9.get_width()) / 2 + 10,
                                        0 + (Screen.get_height() - helpText9.get_height()) / 2 + 340 + Screeny))
                Screen.blit(helpText10, ((Screen.get_width() - helpText10.get_width()) / 2 + 10,
                                         0 + (Screen.get_height() - helpText10.get_height()) / 2 + 325 + Screeny))
                Screen.blit(helpText11, ((Screen.get_width() - helpText11.get_width()) / 2 + 10,
                                         0 + (Screen.get_height() - helpText11.get_height()) / 2 + 310 + Screeny))
                Screen.blit(helpText12, ((Screen.get_width() - helpText12.get_width()) / 2 + 10,
                                         0 + (Screen.get_height() - helpText12.get_height()) / 2 + 295 + Screeny))
                Screen.blit(returnButton.text,
                            ((Screen.get_width() - ButtonImageWidth) / 2 + (ButtonImageWidth - returnButton.text.get_width()) / 2,
                             Screeny - (Screen.get_height() - ButtonImageHeight) / 2 + 110 + (
                                     ButtonImageHeight / 2 - returnButton.text.get_height() / 2)))


            Screen.blit(scoreText, (10, 10))
            Screen.blit(highScoreText, (10, 40))
            Screen.blit(scoreCountText,(scoreText.get_width()+15,10))
            Screen.blit(highScoreCountText, (highScoreText.get_width() + 15, 40))

            #--------------------3.17 Pause game if player touches the left side of the screen---------------------

            if man.x <= 0 or (man.y+playerHeight>=520 and Begin):
                Screen1 = False
                Screen1run = False
                Screen2 = False
                Screen2run = False
                Screen3 = False
                Screen3run = False
                Screen4 = False
                Screen4 = False
                obstacle1x = 520
                obstacle2x = 520
                obstacle3x = 520
                Screens = 0
                Died = True

            #-------------------------3.18 Move Died Screen---------------------------

            if Died:
                if youDiedy < 350:
                    youDiedy+=150
                elif youDiedy > 350:
                    youDiedy = 350

            if not Died:
                if youDiedy> -500:
                    youDiedy -= 150
                if youDiedy<-500:
                    youDiedy = -500

            #------------------------3.19 Prevent player from moving outside the boundairies of the game---------------------

            if man.y > Screen.get_height() - playerHeight:
                man.y = 520 - playerHeight
            if man.x > (Screen.get_width() - playerWidth):
                man.x = Screen.get_width() - playerWidth

            #----------------3.20 Move dropdown menu--------------------

            if Menu and Screeny < 500:
                Screeny += 75
            if Menu and Screeny > 500:
                Screeny = 500
            if not Menu and Screeny > 0:
                Screeny -= 75
            if not Menu and Screeny < 0:
                Screeny = 0
            if not Menu and not Died:
                obstacley += 1

            #-------------------3.21 Increase score-------------------

            if not Died and not Menu and obstacley % 10 == 0:
                score += 1
            if score > highScore:
                with open("score.txt", "w") as file:
                    file.write(str(score))
                highScore = score

            pygame.display.update()

while game_over == False:
    if Home:
        startGame()
    if Help:
        help()
    if mainGame:
        Game()