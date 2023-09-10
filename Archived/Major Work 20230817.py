import pygame
import random
import sys
from PIL import Image
#https://www.vecteezy.com/vector-art/5159239-nature-silhouette-landscape-spring-forest-pine-trees-summer-vector-illustration-design-winter-tree-illustration-vector-collection-for-christmas
pygame.init()

#Functional Test, can display multiple groups of obstacles at the same time

#-------------------WELCOME----------------------------

#game = False
#game_over = False

#while game==False:
Screen = pygame.display.set_mode((520,520))
pygame.display.set_caption("SDD Assignment 2")
startGameImage = pygame.image.load('Home Screen.jpg')
playGameImage = pygame.image.load('Game Screen.jpg')
font_1 = pygame.font.SysFont("Verdana",20)
font_2 = pygame.font.SysFont("Verdana",30)
text_colour_1 = (255,255,255)
text_colour_2 = (255,23,15)
obstacle = pygame.image.load("token_2.png")

playerWidth = (pygame.image.load('Charactere_Idle_Left_0.png')).get_width()*4
playerHeight = (pygame.image.load('Charactere_Idle_Left_0.png')).get_height()*4
walkRight = [pygame.image.load('Charater_Walk_Right_0.png'), pygame.image.load('Charater_Walk_Right_1.png'), pygame.image.load('Charater_Walk_Right_2.png'), pygame.image.load('Charater_Walk_Right_3.png'), pygame.image.load('Charater_Walk_Right_4.png'), pygame.image.load('Charater_Walk_Right_5.png'), pygame.image.load('Charater_Walk_Right_6.png'), pygame.image.load('Charater_Walk_Right_7.png')]
walkLeft = [pygame.image.load('Character_Walk_Left_0.png'), pygame.image.load('Character_Walk_Left_1.png'), pygame.image.load('Character_Walk_Left_2.png'), pygame.image.load('Character_Walk_Left_3.png'), pygame.image.load('Character_Walk_Left_4.png'), pygame.image.load('Character_Walk_Left_5.png'), pygame.image.load('Character_Walk_Left_6.png'), pygame.image.load('Character_Walk_Left_7.png')]
#charLeft = [pygame.image.load('Charactere_Idle_Left_0.png'),pygame.image.load('Character_Idle_Left_1.png'), pygame.image.load('Character_Idle_Left_2.png'), pygame.image.load('Character_Idle_Left_3.png')]
#charRight = [pygame.image.load('Character_Idle_Right_0.png'),pygame.image.load('Character_Idle_Right_1.png'), pygame.image.load('Character_Idle_Right_2.png'), pygame.image.load('Character_Idle_Right_3.png')]
jumpRight = [pygame.image.load('Character_Jump_Right_0.png'), pygame.image.load('Character_Jump_Right_1.png'), pygame.image.load('Character_Jump_Right_2.png')]
jumpLeft = [pygame.image.load('Character_Jump_Left_0.png'), pygame.image.load('Character_Jump_Left_1.png'), pygame.image.load('Character_Jump_Left_2.png')]
obstacleImageWidth = pygame.image.load("token_2.png").get_width()/2
obstacleImageHeight = pygame.image.load("token_2.png").get_height()/2
obstacleImage = pygame.transform.scale(obstacle, (playerWidth, playerHeight))

class obstacle(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def drawObstacle(self, win):
        if not game_over:
            win.blit(obstacleImage, (self.x,self.y))

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
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
#start_button_colour = (0,68,185)
#start_button_over_colour = (30,30,30)
#start_button_width = 125
#start_button_height:int = 50

start_button_rect = [(Screen.get_width()-startButton.width)/2,(Screen.get_height()-startButton.height)/2+50,startButton.width,startButton.height]
help_button_rect = [(Screen.get_width()-helpButton.width)/2,(Screen.get_height()-helpButton.height)/2-10,helpButton.width,helpButton.height]
quit_button_rect = [(Screen.get_width()-quitButton.width)/2,(Screen.get_height()-quitButton.height)/2+110,quitButton.width,quitButton.height]
#start_button_text = start_button_font.render("Start Game", True, text_colour)
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

Screen2pos1 = 34
Screen2pos2 = 246
Screen2pos3 = 487
Screen2pos4 = 684

Screen3pos1 = 38
Screen3pos2 = 235
Screen3pos3 = 498
Screen3pos4 = 725

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
help_box_outer_rect = [(Screen.get_width()-helpBoxOuter.width)/2,(Screen.get_height()-helpBoxOuter.height)/2,helpBoxOuter.width,helpBoxOuter.height]
help_box_middle_rect = [(Screen.get_width()-helpBoxMiddle.width)/2,(Screen.get_height()-helpBoxMiddle.height)/2,helpBoxMiddle.width,helpBoxMiddle.height]
help_box_inner_rect = [(Screen.get_width()-helpBoxInner.width)/2,(Screen.get_height()-helpBoxInner.height)/2,helpBoxInner.width,helpBoxInner.height]

returnButton = button(125,50, (0,68,185), (30,30,30), font_1.render("Return", True, text_colour_1))

return_button_rect = [(Screen.get_width()-returnButton.width)/2,(Screen.get_height()-returnButton.height)/2+150,quitButton.width,quitButton.height]

helpName = font_2.render("Help", True, text_colour_2)

game_over = False
mainGame = False
Home = True
Help = False
Menu = False
def startGame():
    x, y = (0, 0)
    global game_over
    global mainGame
    global Home
    global Help
    while not game_over and not mainGame and not Help:
        Screen.blit(startGameImage,(0,0))
        pygame.draw.rect(Screen, startButton.colour, start_button_rect)
        pygame.draw.rect(Screen, quitButton.colour, quit_button_rect)
        pygame.draw.rect(Screen, helpButton.colour, help_button_rect)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over = True

            # Mousebuttondown
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if (quit_button_rect[0] <= x <= quit_button_rect[0] + quit_button_rect[2] and quit_button_rect[1] <= y <= quit_button_rect[1] +
                        quit_button_rect[3]):
                    game_over = True
                if (start_button_rect[0]<= x <= start_button_rect[0]+start_button_rect[2] and start_button_rect[1]<= y<=start_button_rect[1]+start_button_rect[3]):
                    Home = False
                    mainGame = True

                if (help_button_rect[0]<= x <= help_button_rect[0]+help_button_rect[2] and help_button_rect[1]<= y<=help_button_rect[1]+help_button_rect[3]):
                    Home = False
                    Help = True

            if event.type==pygame.MOUSEMOTION:
                x,y = event.pos
        if (start_button_rect[0] <= x <= start_button_rect[0] + start_button_rect[2] and start_button_rect[1] <= y <= start_button_rect[1] + start_button_rect[3]):
            pygame.draw.rect(Screen, startButton.over_colour, start_button_rect)
            pygame.draw.rect(Screen, quitButton.colour, quit_button_rect)
            pygame.draw.rect(Screen, helpButton.colour, help_button_rect)


        if (quit_button_rect[0] <= x <= quit_button_rect[0] + quit_button_rect[2] and quit_button_rect[1] <= y <=
                quit_button_rect[1] + quit_button_rect[3]):
            pygame.draw.rect(Screen, startButton.colour, start_button_rect)
            pygame.draw.rect(Screen, quitButton.over_colour, quit_button_rect)
            pygame.draw.rect(Screen, helpButton.colour, help_button_rect)

        if (help_button_rect[0] <= x <= help_button_rect[0] + help_button_rect[2] and help_button_rect[1] <= y <=
                help_button_rect[1] + help_button_rect[3]):
            pygame.draw.rect(Screen, startButton.colour, start_button_rect)
            pygame.draw.rect(Screen, helpButton.over_colour, help_button_rect)
            pygame.draw.rect(Screen, quitButton.colour, quit_button_rect)


        Screen.blit(startButton.text, (start_button_rect[0] + (startButton.width - startButton.text.get_width()) / 2,
                                  start_button_rect[1] + (startButton.height / 2 - startButton.text.get_height() / 2)))
        Screen.blit(quitButton.text, (quit_button_rect[0] + (quitButton.width - quitButton.text.get_width()) / 2,
                                        quit_button_rect[1] + (quitButton.height / 2 - quitButton.text.get_height() / 2)))
        Screen.blit(helpButton.text, (help_button_rect[0] + (helpButton.width - helpButton.text.get_width()) / 2,
                                        help_button_rect[1] + (helpButton.height / 2 - helpButton.text.get_height() / 2)))
        Screen.blit(gameName, ((Screen.get_width() - gameName.get_width())/2, (Screen.get_height()-gameName.get_height())/2-70))


        pygame.display.update()



def help():
    (x,y) = (0,0)
    global game_over
    global mainGame
    global Help
    global Home
    while not game_over and not mainGame and not Home:
        Screen.blit(startGameImage, (0, 0))
        pygame.draw.rect(Screen, helpBoxOuter.colour, help_box_outer_rect)
        pygame.draw.rect(Screen, helpBoxMiddle.colour, help_box_middle_rect)
        pygame.draw.rect(Screen, helpBoxInner.colour, help_box_inner_rect)
        pygame.draw.rect(Screen, returnButton.colour, return_button_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            # Mousebuttondown
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if (return_button_rect[0] <= x <= return_button_rect[0] + return_button_rect[2] and return_button_rect[
                    1] <= y <= return_button_rect[1] + return_button_rect[3]):
                    Home = True
                    Help = False

            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
        if (return_button_rect[0] <= x <= return_button_rect[0] + return_button_rect[2] and return_button_rect[1] <= y <=
                return_button_rect[1] + return_button_rect[3]):
            pygame.draw.rect(Screen, returnButton.over_colour, return_button_rect)


        Screen.blit(returnButton.text, (return_button_rect[0] + (returnButton.width - returnButton.text.get_width()) / 2,
                                        return_button_rect[1] + (returnButton.height / 2 - returnButton.text.get_height() / 2)))
        Screen.blit(helpName, ((Screen.get_width() - helpName.get_width()) / 2, (Screen.get_height() - helpName.get_height()) / 2 - 150))

        pygame.display.update()


MenuHelp = False
platform = False
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

def Game():
    Clock = pygame.time.Clock()
    obstacle1x = 520
    obstacle2x = 520
    obstacle3x = 520
    obstacley = 0
    background1x = 0
    background2x = 1920
    variable = 0
    i = 0
    n = 0
    counter = 1
    storedi = 0
    Screen1run = False
    Screen2run = False
    Screen3run = False
    global Screens
    global pos1, pos2, pos3, pos4
    global Screen1, Screen2, Screen3, Screen4
    global Screen1obstacle1, Screen1obstacle2, Screen1obstacle3, Screen1obstacle4, Screen2obstacle1, Screen2obstacle2, Screen2obstacle3, Screen2obstacle4, Screen3obstacle1, Screen3obstacle2, Screen3obstacle3, Screen3obstacle4, Screen4obstacle1, Screen4obstacle2, Screen4obstacle3, Screen4obstacle4
    (x, y) = (0, 0)
    Screeny = 0
    vel = 5
    man.x = 100
    man.y = 520-playerHeight
    menuButton = button(25, 25, (0, 68, 185), (30, 30, 30), font_1.render("||", True, text_colour_1))
    homeButton = button(125, 50, (0, 68, 185), (30, 30, 30), font_1.render("Home", True, text_colour_1))
    menuQuitButton = button(125, 50, (0, 68, 185), (30, 30, 30), font_1.render("Quit", True, text_colour_1))
    menuHelpButton = button(125, 50, (0, 68, 185), (30, 30, 30), font_1.render("Help", True, text_colour_1))
    menu_button_rect = [(Screen.get_width() - menuButton.width) - 20, 20, menuButton.width,
                        menuButton.height]
    menuBoxOuter = box(460, 460, (218, 118, 159))
    menuBoxMiddle = box(450, 450, (255, 162, 157))
    menuBoxInner = box(430, 430, (255, 219, 208))
    menuName = font_2.render("Menu", True, text_colour_2)
    global MenuHelp, game_over, mainGame, Help, Home, Menu, platform
    while not game_over and not Help and not Home:
        #print(Screen1pos1)
        #print(obstacleImage.get_height())
        #print(obstacleImage.get_width())

        if Screens==0:
            Screen1 = True
            Screen1run = True
            storedi = 0
            Screens += 1
            #if i == 2:
             #   Screen1 = True
              #  Screens += 1
               # storedi = 2
            #if i == 3:
             #   Screen1 = True
              #  Screens += 1
               # storedi = 3

        while Screens >= 1 and not game_over and not Home:
            while Screens == 1:
                print(417)
                n = random.randint(0, 2)
                print("n is", n)
                print(Screen1)
                print(Screen2)
                print(Screen3)
                if n == 0 and not(Screen1):
                    Screen1 = True
                    Screen1run = True
                    if counter == 2:
                        obstacle1x = obstacle2x + 704
                    if counter == 3:
                        obstacle1x = obstacle3x + 745
                    counter = 1
                    Screens += 1
                if n == 1 and not(Screen2):
                    print('added')
                    Screen2 = True
                    Screen2run = True
                    if counter == 1:
                        obstacle2x = obstacle1x + 770
                    if counter == 3:
                        obstacle2x = obstacle3x + 745
                    counter = 2
                    Screens += 1

                if n == 2 and not(Screen3):
                    print('added')
                    Screen3 = True
                    Screen3run = True
                    if counter == 1:
                        obstacle3x = obstacle1x + 770
                    if counter == 2:
                        obstacle3x = obstacle2x + 704
                    counter = 3
                    Screens += 1

                # if n == 3 and (storedi == 0 or storedi == 1 or storedi == 2):
                #   print('added')
                #  Screen2 = True
                # storedi = 3
                # Screens += 1
            print(Screens)
            print(Screen1)
            print(Screen2)
            print(Screen3)
            print(obstacle1x+Screen1pos4)
            print(obstacle2x+Screen2pos4)
            print(obstacle3x+Screen3pos4)
            print("Screens is", Screens)
            menu_help_button_rect = [(Screen.get_width() - menuHelpButton.width) / 2,
                                     (0 - menuHelpButton.height) - 190 + Screeny, menuHelpButton.width,
                                     menuHelpButton.height]
            menu_quit_button_rect = [(Screen.get_width() - menuQuitButton.width) / 2,
                                     (0 - menuQuitButton.height) - 70 + Screeny, menuQuitButton.width,
                                     menuQuitButton.height]
            menu_home_button_rect = [(Screen.get_width() - homeButton.width) / 2,
                                     (0 - homeButton.height) - 130 + Screeny,
                                     homeButton.width, homeButton.height]

            menu_box_outer_rect = [(Screen.get_width() - menuBoxOuter.width) / 2, (Screeny - menuBoxOuter.height),
                                   menuBoxOuter.width, menuBoxOuter.height]
            menu_box_middle_rect = [(Screen.get_width() - menuBoxMiddle.width) / 2,
                                    (Screeny - menuBoxMiddle.height - 5),
                                    menuBoxMiddle.width, menuBoxMiddle.height]
            menu_box_inner_rect = [(Screen.get_width() - menuBoxInner.width) / 2, (Screeny - menuBoxInner.height - 15),
                                   menuBoxInner.width, menuBoxInner.height]
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if (menu_button_rect[0] <= x <= menu_button_rect[0] + menu_button_rect[2] and menu_button_rect[
                        1] <= y <= menu_button_rect[1] + menu_button_rect[3]):
                        if Menu:
                            Menu = False
                            MenuHelp = False
                        else:
                            Menu = True

                    if Menu and (
                            menu_quit_button_rect[0] <= x <= menu_quit_button_rect[0] + menu_quit_button_rect[2] and
                            menu_quit_button_rect[
                                1] <= y <= menu_quit_button_rect[1] + menu_quit_button_rect[3]):
                        game_over = True
                    if Menu and (
                            menu_home_button_rect[0] <= x <= menu_home_button_rect[0] + menu_home_button_rect[2] and
                            menu_home_button_rect[
                                1] <= y <= menu_home_button_rect[1] + menu_home_button_rect[3]):
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
                        #Screen3run = False
                    if Menu and (
                            menu_help_button_rect[0] <= x <= menu_help_button_rect[0] + menu_help_button_rect[2] and
                            menu_help_button_rect[
                                1] <= y <= menu_help_button_rect[1] + menu_help_button_rect[3]):
                        MenuHelp = True

            if Menu and Screeny < 500:
                Screeny += 75
            if Menu and Screeny > 500:
                Screeny = 500
            if not Menu and Screeny > 0:
                Screeny -= 75
            if not Menu and Screeny < 0:
                Screeny = 0
            if not Menu:
                obstacley += 1

            if man.y + playerHeight < 520 - obstacleImage.get_height():
                platform = False

            if man.y > Screen.get_height() - playerHeight:
                man.y = Screen.get_height() - playerHeight
            if man.x < 0:
                Screen1 = False
                Screen2 = False
                Screen3 = False
                Screen4 = False
                mainGame = False
                Home = True
            if man.x > (Screen.get_width() - playerWidth):
                man.x = Screen.get_width() - playerWidth

            for r in range(len(walkRight)):
                walkRight[r] = pygame.transform.scale(walkRight[r], (playerWidth, playerHeight))
            for r in range(len(walkLeft)):
                walkLeft[r] = pygame.transform.scale(walkLeft[r], (playerWidth, playerHeight))
            if Screen1 and not game_over:
                print("screen1")
                Clock.tick(24)
                if Screen1pos4+obstacle1x <= 520 and Screen1run:
                    Screens -= 1
                    Screen1run = False
                def Falling1():
                    if Screen1pos1 + obstacle1x + obstacleImage.get_width() > man.x > Screen1pos1 + obstacle1x or Screen1pos1 + obstacle1x + obstacleImage.get_width() > man.x + playerWidth > Screen1pos1 + obstacle1x or Screen1pos2 + obstacle1x + obstacleImage.get_width() > man.x > Screen1pos2 + obstacle1x or Screen1pos2 + obstacle1x + obstacleImage.get_width() > man.x + playerWidth > Screen1pos2 + obstacle1x or Screen1pos3 + obstacle1x + obstacleImage.get_width() > man.x > Screen1pos3 + obstacle1x or Screen1pos3 + obstacle1x + obstacleImage.get_width() > man.x + playerWidth > Screen1pos3 + obstacle1x or Screen1pos4 + obstacle1x + obstacleImage.get_width() > man.x > Screen1pos4 + obstacle1x or Screen1pos4 + obstacle1x + obstacleImage.get_width() > man.x + playerWidth > Screen1pos4 + obstacle1x:
                        if man.y + playerHeight > 520 - obstacleImage.get_height():
                            man.y = 520 - obstacleImage.get_height() - playerHeight

                if man.y + playerHeight == 520 - obstacleImage.get_height():
                    platform = True
                elif man.y + playerHeight > 520 - obstacleImage.get_height() or man.y + playerHeight < 520 - obstacleImage.get_height():
                    platform = False

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_over = True

                    pygame.display.update()

                keys = pygame.key.get_pressed()

                if keys[pygame.K_LEFT] and not Menu:
                    man.x -= vel
                    man.left = True
                    man.right = False
                    man.standing = False
                elif keys[pygame.K_RIGHT] and not Menu:
                    man.x += vel
                    man.right = True
                    man.left = False
                    man.standing = False
                else:
                    man.standing = True
                    man.walkCount = 0


                if not (man.isJump):
                    if keys[pygame.K_UP] and not Menu:
                        man.isJump = True
                        man.right = False
                        man.left = False
                        platform = False
                        man.walkCount = 0

                else:

                    if man.jumpCount >= -10 and not Menu:
                        neg = 1
                        if man.jumpCount < 0:
                            neg = -1
                        man.y -= (man.jumpCount ** 2) * 0.5 * neg
                        Falling1()
                        man.jumpCount -= 1

                    elif Menu:
                        man.jumpCount -= 0
                    else:
                        man.isJump = False
                        man.jumpCount = 10

                if Screen1pos1 + obstacle1x + obstacleImage.get_width() > man.x > Screen1pos1 + obstacle1x or Screen1pos1 + obstacle1x + obstacleImage.get_width() > man.x + playerWidth > Screen1pos1 + obstacle1x:
                    if man.y + playerHeight == 520 - obstacleImage.get_height():
                        Screen1obstacle1 = True
                if Screen1pos2 + obstacle1x + obstacleImage.get_width() > man.x > Screen1pos2 + obstacle1x or Screen1pos2 + obstacle1x + obstacleImage.get_width() > man.x + playerWidth > Screen1pos2 + obstacle1x:
                    if man.y + playerHeight == 520 - obstacleImage.get_height():
                        Screen1obstacle2 = True
                if Screen1pos3 + obstacle1x + obstacleImage.get_width() > man.x > Screen1pos3 + obstacle1x or Screen1pos3 + obstacle1x + obstacleImage.get_width() > man.x + playerWidth > Screen1pos3 + obstacle1x:
                    if man.y + playerHeight == 520 - obstacleImage.get_height():
                        Screen1obstacle3 = True
                if Screen1pos4 + obstacle1x + obstacleImage.get_width() > man.x > Screen1pos4 + obstacle1x or Screen1pos4 + obstacle1x + obstacleImage.get_width() > man.x + playerWidth > Screen1pos4 + obstacle1x:
                    if man.y + playerHeight == 520 - obstacleImage.get_height():
                        Screen1obstacle4 = True

                if platform:
                    if Screen1obstacle1 and not Screen1pos1 + obstacle1x + obstacleImage.get_width() > man.x > Screen1pos1 + obstacle1x and not Screen1pos1 + obstacle1x + obstacleImage.get_width() > man.x + playerWidth > Screen1pos1 + obstacle1x:
                        if man.y+playerHeight >= 520-obstacleImage.get_height():
                            neg = -1
                            man.y -= (man.jumpCount ** 2) * 0.5 * neg
                            platform = False
                            Screen1obstacle1 = False

                    elif Screen1obstacle2 and not Screen1pos2 + obstacle1x + obstacleImage.get_width() > man.x > Screen1pos2 + obstacle1x and not Screen1pos2 + obstacle1x + obstacleImage.get_width() > man.x + playerWidth > Screen1pos2 + obstacle1x:
                        if man.y+playerHeight >= 520-obstacleImage.get_height():
                            neg = -1
                            man.y -= (man.jumpCount ** 2) * 0.5 * neg
                            platform = False
                            Screen1obstacle2 = False

                    elif Screen1obstacle3 and not Screen1pos3 + obstacle1x + obstacleImage.get_width() > man.x > Screen1pos3 + obstacle1x and not Screen1pos3 + obstacle1x + obstacleImage.get_width() > man.x + playerWidth > Screen1pos3 + obstacle1x:
                        if man.y+playerHeight >= 520-obstacleImage.get_height():
                            neg = -1
                            man.y -= (man.jumpCount ** 2) * 0.5 * neg
                            platform = False
                            Screen1obstacle3 = False

                    elif Screen1obstacle4 and not Screen1pos4 + obstacle1x + obstacleImage.get_width() > man.x > Screen1pos4 + obstacle1x and not Screen1pos4 + obstacle1x + obstacleImage.get_width() > man.x + playerWidth > Screen1pos4 + obstacle1x:
                        if man.y+playerHeight >= 520-obstacleImage.get_height():
                            neg = -1
                            man.y -= (man.jumpCount ** 2) * 0.5 * neg
                            platform = False
                            Screen1obstacle4 = False

                if man.x+playerWidth>Screen1pos1+obstacle1x:
                    if man.y+playerHeight>520-obstacleImage.get_height():
                        if man.x<Screen1pos1+obstacle1x:
                            man.x = Screen1pos1 + obstacle1x - playerWidth+1
                if man.x<Screen1pos1+obstacle1x+obstacleImage.get_width():
                    if man.y+playerHeight>520-obstacleImage.get_height():
                        if man.x>Screen1pos1+obstacle1x:
                            man.x = Screen1pos1+obstacle1x+obstacleImage.get_width()

                if man.x+playerWidth>Screen1pos2+obstacle1x:
                    if man.y+playerHeight>520-obstacleImage.get_height():
                        if man.x<Screen1pos2+obstacle1x:
                            man.x = Screen1pos2 + obstacle1x - playerWidth+1
                if man.x<Screen1pos2+obstacle1x+obstacleImage.get_width():
                    if man.y+playerHeight>520-obstacleImage.get_height():
                        if man.x>Screen1pos2+obstacle1x:
                            man.x = Screen1pos2+obstacle1x+obstacleImage.get_width()

                if man.x+playerWidth>Screen1pos3+obstacle1x:
                    if man.y+playerHeight>520-obstacleImage.get_height():
                        if man.x<Screen1pos3+obstacle1x:
                            man.x = Screen1pos3 + obstacle1x - playerWidth+1
                if man.x<Screen1pos3+obstacle1x+obstacleImage.get_width():
                    if man.y+playerHeight>520-obstacleImage.get_height():
                        if man.x>Screen1pos3+obstacle1x:
                            man.x = Screen1pos3+obstacle1x+obstacleImage.get_width()

                if man.x+playerWidth>Screen1pos4+obstacle1x:
                    if man.y+playerHeight>520-obstacleImage.get_height():
                        if man.x<Screen1pos4+obstacle1x:
                            man.x = Screen1pos4 + obstacle1x - playerWidth+1
                if man.x<Screen1pos4+obstacle1x+obstacleImage.get_width():
                    if man.y+playerHeight>520-obstacleImage.get_height():
                        if man.x>Screen1pos4+obstacle1x:
                            man.x = Screen1pos4+obstacle1x+obstacleImage.get_width()



                Screen.blit(playGameImage, (0, 0))
                Screen1box1_rect = [Screen1pos1 + obstacle1x, 520 - Screen1box1.height, Screen1box1.width, Screen1box1.height]
                Screen1box2_rect = [Screen1pos2 + obstacle1x, 520 - Screen1box2.height, Screen1box2.width, Screen1box2.height]
                Screen1box3_rect = [Screen1pos3 + obstacle1x, 520 - Screen1box3.height, Screen1box3.width, Screen1box3.height]
                Screen1box4_rect = [Screen1pos4 + obstacle1x, 520 - Screen1box4.height, Screen1box4.width, Screen1box4.height]

                if obstacle1x <= -750:
                    print(1)
                    Screen1 = False
                    obstacle1x = 520
                Screen.blit(playGameImage, (0 + background1x, 0))
                Screen.blit(playGameImage, (0 + background2x, 0))
                if background1x == -playGameImage.get_width():
                    background1x = background2x + playGameImage.get_width()
                if background2x == -playGameImage.get_width():
                    background2x = background1x + playGameImage.get_width()
                man.draw(Screen)
                pygame.draw.rect(Screen, menuBoxOuter.colour, menu_box_outer_rect)
                pygame.draw.rect(Screen, menuBoxMiddle.colour, menu_box_middle_rect)
                pygame.draw.rect(Screen, menuBoxInner.colour, menu_box_inner_rect)
                pygame.draw.rect(Screen, menuButton.colour, menu_button_rect)
                Screen.blit(menuButton.text,
                            (menu_button_rect[0] + (menuButton.width - menuButton.text.get_width()) / 2,
                             menu_button_rect[1] + (menuButton.height / 2 - menuButton.text.get_height() / 2) - 2.5))
                if not MenuHelp:
                    pygame.draw.rect(Screen, menuHelpButton.colour, menu_help_button_rect)
                    pygame.draw.rect(Screen, homeButton.colour, menu_home_button_rect)
                    pygame.draw.rect(Screen, menuQuitButton.colour, menu_quit_button_rect)
                    pygame.draw.rect(Screen, menuButton.colour, menu_button_rect)
                    Screen.blit(menuButton.text,
                                (menu_button_rect[0] + (menuButton.width - menuButton.text.get_width()) / 2,
                                 menu_button_rect[1] + (menuButton.height / 2 - menuButton.text.get_height() / 2) - 2.5))
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEMOTION:
                            x, y = event.pos
                    if (menu_button_rect[0] <= x <= menu_button_rect[0] + menu_button_rect[2] and menu_button_rect[
                        1] <= y <= menu_button_rect[1] + menu_button_rect[3]):
                        pygame.draw.rect(Screen, menuButton.over_colour, menu_button_rect)
                        pygame.draw.rect(Screen, menuHelpButton.colour, menu_help_button_rect)
                        pygame.draw.rect(Screen, homeButton.colour, menu_home_button_rect)
                        pygame.draw.rect(Screen, menuQuitButton.colour, menu_quit_button_rect)
                        Screen.blit(menuButton.text,
                                    (menu_button_rect[0] + (menuButton.width - menuButton.text.get_width()) / 2,
                                     menu_button_rect[1] + (menuButton.height / 2 - menuButton.text.get_height() / 2) - 2.5))
                    if Menu and (menu_quit_button_rect[0] <= x <= menu_quit_button_rect[0] + menu_quit_button_rect[2] and
                                 menu_quit_button_rect[
                                     1] <= y <= menu_quit_button_rect[1] + menu_quit_button_rect[3]):
                        pygame.draw.rect(Screen, menuQuitButton.over_colour, menu_quit_button_rect)
                        pygame.draw.rect(Screen, menuHelpButton.colour, menu_help_button_rect)
                        pygame.draw.rect(Screen, homeButton.colour, menu_home_button_rect)
                        pygame.draw.rect(Screen, menuButton.colour, menu_button_rect)
                        Screen.blit(menuButton.text,
                                    (menu_button_rect[0] + (menuButton.width - menuButton.text.get_width()) / 2,
                                     menu_button_rect[1] + (menuButton.height / 2 - menuButton.text.get_height() / 2) - 2.5))

                    if Menu and (menu_home_button_rect[0] <= x <= menu_home_button_rect[0] + menu_home_button_rect[2] and
                                 menu_home_button_rect[
                                     1] <= y <= menu_home_button_rect[1] + menu_home_button_rect[3]):
                        pygame.draw.rect(Screen, homeButton.over_colour, menu_home_button_rect)
                        pygame.draw.rect(Screen, menuHelpButton.colour, menu_help_button_rect)
                        pygame.draw.rect(Screen, menuQuitButton.colour, menu_quit_button_rect)
                        pygame.draw.rect(Screen, menuButton.colour, menu_button_rect)
                        Screen.blit(menuButton.text,
                                    (menu_button_rect[0] + (menuButton.width - menuButton.text.get_width()) / 2,
                                     menu_button_rect[1] + (menuButton.height / 2 - menuButton.text.get_height() / 2) - 2.5))

                    if Menu and (menu_help_button_rect[0] <= x <= menu_help_button_rect[0] + menu_help_button_rect[2] and
                                 menu_help_button_rect[
                                     1] <= y <= menu_help_button_rect[1] + menu_help_button_rect[3]):
                        pygame.draw.rect(Screen, menuHelpButton.over_colour, menu_help_button_rect)
                        pygame.draw.rect(Screen, homeButton.colour, menu_home_button_rect)
                        pygame.draw.rect(Screen, menuQuitButton.colour, menu_quit_button_rect)
                        pygame.draw.rect(Screen, menuButton.colour, menu_button_rect)
                        Screen.blit(menuButton.text,
                                    (menu_button_rect[0] + (menuButton.width - menuButton.text.get_width()) / 2,
                                     menu_button_rect[1] + (menuButton.height / 2 - menuButton.text.get_height() / 2) - 2.5))

                    Screen.blit(homeButton.text,
                                 (menu_home_button_rect[0] + (homeButton.width - homeButton.text.get_width()) / 2,
                                  menu_home_button_rect[1] + (homeButton.height / 2 - homeButton.text.get_height() / 2)))
                    Screen.blit(menuQuitButton.text, (menu_quit_button_rect[0] + (menuQuitButton.width - menuQuitButton.text.get_width()) / 2,
                                                   menu_quit_button_rect[1] + (menuQuitButton.height / 2 - menuQuitButton.text.get_height() / 2)))
                    Screen.blit(helpButton.text, (help_button_rect[0] + (helpButton.width - helpButton.text.get_width()) / 2,
                                                   menu_help_button_rect[1] + (
                                                               menuHelpButton.height / 2 - menuHelpButton.text.get_height() / 2)))
                    Screen.blit(menuName, ((Screen.get_width() - menuName.get_width()) / 2,
                                        0+(Screen.get_height() - menuName.get_height()) / 2 - 600+Screeny))

                if MenuHelp:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEMOTION:
                            x, y = event.pos
                    if (menu_button_rect[0] <= x <= menu_button_rect[0] + menu_button_rect[2] and menu_button_rect[
                        1] <= y <= menu_button_rect[1] + menu_button_rect[3]):
                        pygame.draw.rect(Screen, menuButton.over_colour, menu_button_rect)
                        Screen.blit(menuButton.text,
                                    (menu_button_rect[0] + (menuButton.width - menuButton.text.get_width()) / 2,
                                     menu_button_rect[1] + (menuButton.height / 2 - menuButton.text.get_height() / 2) - 2.5))

                    Screen.blit(helpName, ((Screen.get_width() - helpName.get_width()) / 2,
                                           0 + (Screen.get_height() - helpName.get_height()) / 2 - 600 + Screeny))


                if obstacley % (15 + variable) == 0:
                    obstacle1x -= 20
                    if platform:
                        man.x -= 20
                if not Menu:
                    background1x -= 1
                    background2x -= 1
                if obstacley % 1000 == 0:
                    variable -= 1
                if variable < 1:
                    variable = 1
            if Screen2 and not game_over:
                print('screen2')
                Clock.tick(24)

                if Screen2pos4+obstacle2x <= 520 and Screen2run:
                    Screens -= 1
                    Screen2run = False

                def Falling2():
                    if Screen2pos1 + obstacle2x + obstacleImage.get_width() > man.x > Screen2pos1 + obstacle2x or Screen2pos1 + obstacle2x + obstacleImage.get_width() > man.x + playerWidth > Screen2pos1 + obstacle2x or Screen2pos2 + obstacle2x + obstacleImage.get_width() > man.x > Screen2pos2 + obstacle2x or Screen2pos2 + obstacle2x + obstacleImage.get_width() > man.x + playerWidth > Screen2pos2 + obstacle2x or Screen2pos3 + obstacle2x + obstacleImage.get_width() > man.x > Screen2pos3 + obstacle2x or Screen2pos3 + obstacle2x + obstacleImage.get_width() > man.x + playerWidth > Screen2pos3 + obstacle2x or Screen2pos4 + obstacle2x + obstacleImage.get_width() > man.x > Screen2pos4 + obstacle2x or Screen2pos4 + obstacle2x + obstacleImage.get_width() > man.x + playerWidth > Screen2pos4 + obstacle2x:
                        if man.y + playerHeight > 520 - obstacleImage.get_height():
                            man.y = 520 - obstacleImage.get_height() - playerHeight

                if man.y + playerHeight == 520 - obstacleImage.get_height():
                    platform = True
                elif man.y + playerHeight > 520 - obstacleImage.get_height() or man.y + playerHeight < 520 - obstacleImage.get_height():
                    platform = False

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_over = True

                    pygame.display.update()

                keys = pygame.key.get_pressed()

                if keys[pygame.K_LEFT] and not Menu:
                    man.x -= vel
                    man.left = True
                    man.right = False
                    man.standing = False
                elif keys[pygame.K_RIGHT] and not Menu:
                    man.x += vel
                    man.right = True
                    man.left = False
                    man.standing = False
                else:
                    man.standing = True
                    man.walkCount = 0


                if not (man.isJump):
                    if keys[pygame.K_UP] and not Menu:
                        man.isJump = True
                        man.right = False
                        man.left = False
                        platform = False
                        man.walkCount = 0

                else:

                    if man.jumpCount >= -10 and not Menu:
                        neg = 1
                        if man.jumpCount < 0:
                            neg = -1
                        man.y -= (man.jumpCount ** 2) * 0.5 * neg
                        Falling2()
                        man.jumpCount -= 1

                    elif Menu:
                        man.jumpCount -= 0
                    else:
                        man.isJump = False
                        man.jumpCount = 10

                if Screen2pos1 + obstacle2x + obstacleImage.get_width() > man.x > Screen2pos1 + obstacle2x or Screen2pos1 + obstacle2x + obstacleImage.get_width() > man.x + playerWidth > Screen2pos1 + obstacle2x:
                    if man.y + playerHeight == 520 - obstacleImage.get_height():
                        Screen2obstacle1 = True
                if Screen2pos2 + obstacle2x + obstacleImage.get_width() > man.x > Screen2pos2 + obstacle2x or Screen2pos2 + obstacle2x + obstacleImage.get_width() > man.x + playerWidth > Screen2pos2 + obstacle2x:
                    if man.y + playerHeight == 520 - obstacleImage.get_height():
                        Screen2obstacle2 = True
                if Screen2pos3 + obstacle2x + obstacleImage.get_width() > man.x > Screen2pos3 + obstacle2x or Screen2pos3 + obstacle2x + obstacleImage.get_width() > man.x + playerWidth > Screen2pos3 + obstacle2x:
                    if man.y + playerHeight == 520 - obstacleImage.get_height():
                        Screen2obstacle3 = True
                if Screen2pos4 + obstacle2x + obstacleImage.get_width() > man.x > Screen2pos4 + obstacle2x or Screen2pos4 + obstacle2x + obstacleImage.get_width() > man.x + playerWidth > Screen2pos4 + obstacle2x:
                    if man.y + playerHeight == 520 - obstacleImage.get_height():
                        Screen2obstacle4 = True

                if platform:
                    if Screen2obstacle1 and not Screen2pos1 + obstacle2x + obstacleImage.get_width() > man.x > Screen2pos1 + obstacle2x and not Screen2pos1 + obstacle2x + obstacleImage.get_width() > man.x + playerWidth > Screen2pos1 + obstacle2x:
                        if man.y+playerHeight >= 520-obstacleImage.get_height():

                            neg = -1
                            man.y -= (man.jumpCount ** 2) * 0.5 * neg
                            platform = False
                            Screen2obstacle1 = False

                    elif Screen2obstacle2 and not Screen2pos2 + obstacle2x + obstacleImage.get_width() > man.x > Screen2pos2 + obstacle2x and not Screen2pos2 + obstacle2x + obstacleImage.get_width() > man.x + playerWidth > Screen2pos2 + obstacle2x:
                        if man.y+playerHeight >= 520-obstacleImage.get_height():
                            neg = -1
                            man.y -= (man.jumpCount ** 2) * 0.5 * neg
                            platform = False
                            Screen2obstacle2 = False

                    elif Screen2obstacle3 and not Screen2pos3 + obstacle2x + obstacleImage.get_width() > man.x > Screen2pos3 + obstacle2x and not Screen2pos3 + obstacle2x + obstacleImage.get_width() > man.x + playerWidth > Screen2pos3 + obstacle2x:
                        if man.y+playerHeight >= 520-obstacleImage.get_height():
                            neg = -1
                            man.y -= (man.jumpCount ** 2) * 0.5 * neg
                            platform = False
                            Screen2obstacle3 = False

                    elif Screen2obstacle4 and not Screen2pos4 + obstacle2x + obstacleImage.get_width() > man.x > Screen2pos4 + obstacle2x and not Screen2pos4 + obstacle2x + obstacleImage.get_width() > man.x + playerWidth > Screen2pos4 + obstacle2x:
                        if man.y+playerHeight >= 520-obstacleImage.get_height():
                            neg = -1
                            man.y -= (man.jumpCount ** 2) * 0.5 * neg
                            platform = False
                            Screen2obstacle4 = False

                if man.x+playerWidth>Screen2pos1+obstacle2x:
                    if man.y+playerHeight>520-obstacleImage.get_height():
                        if man.x<Screen2pos1+obstacle2x:
                            man.x = Screen2pos1 + obstacle2x - playerWidth+1
                if man.x<Screen2pos1+obstacle2x+obstacleImage.get_width():
                    if man.y+playerHeight>520-obstacleImage.get_height():
                        if man.x>Screen2pos1+obstacle2x:
                            man.x = Screen2pos1+obstacle2x+obstacleImage.get_width()

                if man.x+playerWidth>Screen2pos2+obstacle2x:
                    if man.y+playerHeight>520-obstacleImage.get_height():
                        if man.x<Screen2pos2+obstacle2x:
                            man.x = Screen2pos2 + obstacle2x - playerWidth+1
                if man.x<Screen2pos2+obstacle2x+obstacleImage.get_width():
                    if man.y+playerHeight>520-obstacleImage.get_height():
                        if man.x>Screen2pos2+obstacle2x:
                            man.x = Screen2pos2+obstacle2x+obstacleImage.get_width()

                if man.x+playerWidth>Screen2pos3+obstacle2x:
                    if man.y+playerHeight>520-obstacleImage.get_height():
                        if man.x<Screen2pos3+obstacle2x:
                            man.x = Screen2pos3 + obstacle2x - playerWidth+1
                if man.x<Screen2pos3+obstacle2x+obstacleImage.get_width():
                    if man.y+playerHeight>520-obstacleImage.get_height():
                        if man.x>Screen2pos3+obstacle2x:
                            man.x = Screen2pos3+obstacle2x+obstacleImage.get_width()

                if man.x+playerWidth>Screen2pos4+obstacle2x:
                    if man.y+playerHeight>520-obstacleImage.get_height():
                        if man.x<Screen2pos4+obstacle2x:
                            man.x = Screen2pos4 + obstacle2x - playerWidth+1
                if man.x<Screen2pos4+obstacle2x+obstacleImage.get_width():
                    if man.y+playerHeight>520-obstacleImage.get_height():
                        if man.x>Screen2pos4+obstacle2x:
                            man.x = Screen2pos4+obstacle2x+obstacleImage.get_width()



                Screen.blit(playGameImage, (0, 0))
                Screen2box1_rect = [Screen2pos1 + obstacle2x, 520 - Screen2box1.height, Screen2box1.width, Screen2box1.height]
                Screen2box2_rect = [Screen2pos2 + obstacle2x, 520 - Screen2box2.height, Screen2box2.width, Screen2box2.height]
                Screen2box3_rect = [Screen2pos3 + obstacle2x, 520 - Screen2box3.height, Screen2box3.width, Screen2box3.height]
                Screen2box4_rect = [Screen2pos4 + obstacle2x, 520 - Screen2box4.height, Screen2box4.width, Screen2box4.height]

                if obstacle2x <= -684:
                    print(2)
                    Screen2 = False
                    obstacle2x = 520
                Screen.blit(playGameImage, (0 + background1x, 0))
                Screen.blit(playGameImage, (0 + background2x, 0))
                if background1x == -playGameImage.get_width():
                    background1x = background2x + playGameImage.get_width()
                if background2x == -playGameImage.get_width():
                    background2x = background1x + playGameImage.get_width()

                man.draw(Screen)
                pygame.draw.rect(Screen, menuBoxOuter.colour, menu_box_outer_rect)
                pygame.draw.rect(Screen, menuBoxMiddle.colour, menu_box_middle_rect)
                pygame.draw.rect(Screen, menuBoxInner.colour, menu_box_inner_rect)
                pygame.draw.rect(Screen, menuButton.colour, menu_button_rect)
                Screen.blit(menuButton.text,
                            (menu_button_rect[0] + (menuButton.width - menuButton.text.get_width()) / 2,
                             menu_button_rect[1] + (menuButton.height / 2 - menuButton.text.get_height() / 2) - 2.5))
                if not MenuHelp:
                    pygame.draw.rect(Screen, menuHelpButton.colour, menu_help_button_rect)
                    pygame.draw.rect(Screen, homeButton.colour, menu_home_button_rect)
                    pygame.draw.rect(Screen, menuQuitButton.colour, menu_quit_button_rect)
                    pygame.draw.rect(Screen, menuButton.colour, menu_button_rect)
                    Screen.blit(menuButton.text,
                                (menu_button_rect[0] + (menuButton.width - menuButton.text.get_width()) / 2,
                                 menu_button_rect[1] + (menuButton.height / 2 - menuButton.text.get_height() / 2) - 2.5))
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEMOTION:
                            x, y = event.pos
                    if (menu_button_rect[0] <= x <= menu_button_rect[0] + menu_button_rect[2] and menu_button_rect[
                        1] <= y <= menu_button_rect[1] + menu_button_rect[3]):
                        pygame.draw.rect(Screen, menuButton.over_colour, menu_button_rect)
                        pygame.draw.rect(Screen, menuHelpButton.colour, menu_help_button_rect)
                        pygame.draw.rect(Screen, homeButton.colour, menu_home_button_rect)
                        pygame.draw.rect(Screen, menuQuitButton.colour, menu_quit_button_rect)
                        Screen.blit(menuButton.text,
                                    (menu_button_rect[0] + (menuButton.width - menuButton.text.get_width()) / 2,
                                     menu_button_rect[1] + (menuButton.height / 2 - menuButton.text.get_height() / 2) - 2.5))
                    if Menu and (menu_quit_button_rect[0] <= x <= menu_quit_button_rect[0] + menu_quit_button_rect[2] and
                                 menu_quit_button_rect[
                                     1] <= y <= menu_quit_button_rect[1] + menu_quit_button_rect[3]):
                        pygame.draw.rect(Screen, menuQuitButton.over_colour, menu_quit_button_rect)
                        pygame.draw.rect(Screen, menuHelpButton.colour, menu_help_button_rect)
                        pygame.draw.rect(Screen, homeButton.colour, menu_home_button_rect)
                        pygame.draw.rect(Screen, menuButton.colour, menu_button_rect)
                        Screen.blit(menuButton.text,
                                    (menu_button_rect[0] + (menuButton.width - menuButton.text.get_width()) / 2,
                                     menu_button_rect[1] + (menuButton.height / 2 - menuButton.text.get_height() / 2) - 2.5))

                    if Menu and (menu_home_button_rect[0] <= x <= menu_home_button_rect[0] + menu_home_button_rect[2] and
                                 menu_home_button_rect[
                                     1] <= y <= menu_home_button_rect[1] + menu_home_button_rect[3]):
                        pygame.draw.rect(Screen, homeButton.over_colour, menu_home_button_rect)
                        pygame.draw.rect(Screen, menuHelpButton.colour, menu_help_button_rect)
                        pygame.draw.rect(Screen, menuQuitButton.colour, menu_quit_button_rect)
                        pygame.draw.rect(Screen, menuButton.colour, menu_button_rect)
                        Screen.blit(menuButton.text,
                                    (menu_button_rect[0] + (menuButton.width - menuButton.text.get_width()) / 2,
                                     menu_button_rect[1] + (menuButton.height / 2 - menuButton.text.get_height() / 2) - 2.5))

                    if Menu and (menu_help_button_rect[0] <= x <= menu_help_button_rect[0] + menu_help_button_rect[2] and
                                 menu_help_button_rect[
                                     1] <= y <= menu_help_button_rect[1] + menu_help_button_rect[3]):
                        pygame.draw.rect(Screen, menuHelpButton.over_colour, menu_help_button_rect)
                        pygame.draw.rect(Screen, homeButton.colour, menu_home_button_rect)
                        pygame.draw.rect(Screen, menuQuitButton.colour, menu_quit_button_rect)
                        pygame.draw.rect(Screen, menuButton.colour, menu_button_rect)
                        Screen.blit(menuButton.text,
                                    (menu_button_rect[0] + (menuButton.width - menuButton.text.get_width()) / 2,
                                     menu_button_rect[1] + (menuButton.height / 2 - menuButton.text.get_height() / 2) - 2.5))

                    Screen.blit(homeButton.text,
                                 (menu_home_button_rect[0] + (homeButton.width - homeButton.text.get_width()) / 2,
                                  menu_home_button_rect[1] + (homeButton.height / 2 - homeButton.text.get_height() / 2)))
                    Screen.blit(menuQuitButton.text, (menu_quit_button_rect[0] + (menuQuitButton.width - menuQuitButton.text.get_width()) / 2,
                                                   menu_quit_button_rect[1] + (menuQuitButton.height / 2 - menuQuitButton.text.get_height() / 2)))
                    Screen.blit(helpButton.text, (help_button_rect[0] + (helpButton.width - helpButton.text.get_width()) / 2,
                                                   menu_help_button_rect[1] + (
                                                               menuHelpButton.height / 2 - menuHelpButton.text.get_height() / 2)))
                    Screen.blit(menuName, ((Screen.get_width() - menuName.get_width()) / 2,
                                        0+(Screen.get_height() - menuName.get_height()) / 2 - 600+Screeny))

                if MenuHelp:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEMOTION:
                            x, y = event.pos
                    if (menu_button_rect[0] <= x <= menu_button_rect[0] + menu_button_rect[2] and menu_button_rect[
                        1] <= y <= menu_button_rect[1] + menu_button_rect[3]):
                        pygame.draw.rect(Screen, menuButton.over_colour, menu_button_rect)
                        Screen.blit(menuButton.text,
                                    (menu_button_rect[0] + (menuButton.width - menuButton.text.get_width()) / 2,
                                     menu_button_rect[1] + (menuButton.height / 2 - menuButton.text.get_height() / 2) - 2.5))

                    Screen.blit(helpName, ((Screen.get_width() - helpName.get_width()) / 2,
                                           0 + (Screen.get_height() - helpName.get_height()) / 2 - 600 + Screeny))

                if obstacley % (15 + variable) == 0:
                    obstacle2x -= 20
                    if platform:
                        man.x-=20
                if not Menu:
                    background1x -= 1
                    background2x -= 1
                if obstacley % 1000 == 0:
                    variable -= 1
                if variable < 1:
                    variable = 1
            if Screen3 and not game_over:
                print('screen3')
                Clock.tick(24)

                if Screen3pos4+obstacle3x <= 520 and Screen3run:
                    Screens -= 1
                    Screen3run = False

                def Falling3():
                    if Screen3pos1 + obstacle3x + obstacleImage.get_width() > man.x > Screen3pos1 + obstacle3x or Screen3pos1 + obstacle3x + obstacleImage.get_width() > man.x + playerWidth > Screen3pos1 + obstacle3x or Screen3pos2 + obstacle3x + obstacleImage.get_width() > man.x > Screen3pos2 + obstacle3x or Screen3pos2 + obstacle3x + obstacleImage.get_width() > man.x + playerWidth > Screen3pos2 + obstacle3x or Screen3pos3 + obstacle3x + obstacleImage.get_width() > man.x > Screen3pos3 + obstacle3x or Screen3pos3 + obstacle3x + obstacleImage.get_width() > man.x + playerWidth > Screen3pos3 + obstacle3x or Screen3pos4 + obstacle3x + obstacleImage.get_width() > man.x > Screen3pos4 + obstacle3x or Screen3pos4 + obstacle3x + obstacleImage.get_width() > man.x + playerWidth > Screen3pos4 + obstacle3x:
                        if man.y + playerHeight > 520 - obstacleImage.get_height():
                            man.y = 520 - obstacleImage.get_height() - playerHeight

                if man.y + playerHeight == 520 - obstacleImage.get_height():
                    platform = True
                elif man.y + playerHeight > 520 - obstacleImage.get_height() or man.y + playerHeight < 520 - obstacleImage.get_height():
                    platform = False

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_over = True

                    pygame.display.update()

                keys = pygame.key.get_pressed()

                if keys[pygame.K_LEFT] and not Menu:
                    man.x -= vel
                    man.left = True
                    man.right = False
                    man.standing = False
                elif keys[pygame.K_RIGHT] and not Menu:
                    man.x += vel
                    man.right = True
                    man.left = False
                    man.standing = False
                else:
                    man.standing = True
                    man.walkCount = 0


                if not (man.isJump):
                    if keys[pygame.K_UP] and not Menu:
                        man.isJump = True
                        man.right = False
                        man.left = False
                        platform = False
                        man.walkCount = 0

                else:

                    if man.jumpCount >= -10 and not Menu:
                        neg = 1
                        if man.jumpCount < 0:
                            neg = -1
                        man.y -= (man.jumpCount ** 2) * 0.5 * neg
                        Falling3()
                        man.jumpCount -= 1

                    elif Menu:
                        man.jumpCount -= 0
                    else:
                        man.isJump = False
                        man.jumpCount = 10

                if Screen3pos1 + obstacle3x + obstacleImage.get_width() > man.x > Screen3pos1 + obstacle3x or Screen3pos1 + obstacle3x + obstacleImage.get_width() > man.x + playerWidth > Screen3pos1 + obstacle3x:
                    if man.y + playerHeight == 520 - obstacleImage.get_height():
                        Screen3obstacle1 = True
                if Screen3pos2 + obstacle3x + obstacleImage.get_width() > man.x > Screen3pos2 + obstacle3x or Screen3pos2 + obstacle3x + obstacleImage.get_width() > man.x + playerWidth > Screen3pos2 + obstacle3x:
                    if man.y + playerHeight == 520 - obstacleImage.get_height():
                        Screen3obstacle2 = True
                if Screen3pos3 + obstacle3x + obstacleImage.get_width() > man.x > Screen3pos3 + obstacle3x or Screen3pos3 + obstacle3x + obstacleImage.get_width() > man.x + playerWidth > Screen3pos3 + obstacle3x:
                    if man.y + playerHeight == 520 - obstacleImage.get_height():
                        Screen3obstacle3 = True
                if Screen3pos4 + obstacle3x + obstacleImage.get_width() > man.x > Screen3pos4 + obstacle3x or Screen3pos4 + obstacle3x + obstacleImage.get_width() > man.x + playerWidth > Screen3pos4 + obstacle3x:
                    if man.y + playerHeight == 520 - obstacleImage.get_height():
                        Screen3obstacle4 = True

                if platform:
                    if Screen3obstacle1 and not Screen3pos1 + obstacle3x + obstacleImage.get_width() > man.x > Screen3pos1 + obstacle3x and not Screen3pos1 + obstacle3x + obstacleImage.get_width() > man.x + playerWidth > Screen3pos1 + obstacle3x:
                        if man.y+playerHeight >= 520-obstacleImage.get_height():

                            neg = -1
                            man.y -= (man.jumpCount ** 2) * 0.5 * neg
                            platform = False
                            Screen3obstacle1 = False

                    elif Screen3obstacle2 and not Screen3pos2 + obstacle3x + obstacleImage.get_width() > man.x > Screen3pos2 + obstacle3x and not Screen3pos2 + obstacle3x + obstacleImage.get_width() > man.x + playerWidth > Screen3pos2 + obstacle3x:
                        if man.y+playerHeight >= 520-obstacleImage.get_height():
                            neg = -1
                            man.y -= (man.jumpCount ** 2) * 0.5 * neg
                            platform = False
                            Screen3obstacle2 = False

                    elif Screen3obstacle3 and not Screen3pos3 + obstacle3x + obstacleImage.get_width() > man.x > Screen3pos3 + obstacle3x and not Screen3pos3 + obstacle3x + obstacleImage.get_width() > man.x + playerWidth > Screen3pos3 + obstacle3x:
                        if man.y+playerHeight >= 520-obstacleImage.get_height():
                            neg = -1
                            man.y -= (man.jumpCount ** 2) * 0.5 * neg
                            platform = False
                            Screen3obstacle3 = False

                    elif Screen3obstacle4 and not Screen3pos4 + obstacle3x + obstacleImage.get_width() > man.x > Screen3pos4 + obstacle3x and not Screen3pos4 + obstacle3x + obstacleImage.get_width() > man.x + playerWidth > Screen3pos4 + obstacle3x:
                        if man.y+playerHeight >= 520-obstacleImage.get_height():
                            neg = -1
                            man.y -= (man.jumpCount ** 2) * 0.5 * neg
                            platform = False
                            Screen3obstacle4 = False

                if man.x+playerWidth>Screen3pos1+obstacle3x:
                    if man.y+playerHeight>520-obstacleImage.get_height():
                        if man.x<Screen3pos1+obstacle3x:
                            man.x = Screen3pos1 + obstacle3x - playerWidth+1
                if man.x<Screen3pos1+obstacle3x+obstacleImage.get_width():
                    if man.y+playerHeight>520-obstacleImage.get_height():
                        if man.x>Screen3pos1+obstacle3x:
                            man.x = Screen3pos1+obstacle3x+obstacleImage.get_width()

                if man.x+playerWidth>Screen3pos2+obstacle3x:
                    if man.y+playerHeight>520-obstacleImage.get_height():
                        if man.x<Screen3pos2+obstacle3x:
                            man.x = Screen3pos2 + obstacle3x - playerWidth+1
                if man.x<Screen3pos2+obstacle3x+obstacleImage.get_width():
                    if man.y+playerHeight>520-obstacleImage.get_height():
                        if man.x>Screen3pos2+obstacle3x:
                            man.x = Screen3pos2+obstacle3x+obstacleImage.get_width()

                if man.x+playerWidth>Screen3pos3+obstacle3x:
                    if man.y+playerHeight>520-obstacleImage.get_height():
                        if man.x<Screen3pos3+obstacle3x:
                            man.x = Screen3pos3 + obstacle3x - playerWidth+1
                if man.x<Screen3pos3+obstacle3x+obstacleImage.get_width():
                    if man.y+playerHeight>520-obstacleImage.get_height():
                        if man.x>Screen3pos3+obstacle3x:
                            man.x = Screen3pos3+obstacle3x+obstacleImage.get_width()

                if man.x+playerWidth>Screen3pos4+obstacle3x:
                    if man.y+playerHeight>520-obstacleImage.get_height():
                        if man.x<Screen3pos4+obstacle3x:
                            man.x = Screen3pos4 + obstacle3x - playerWidth+1
                if man.x<Screen3pos4+obstacle3x+obstacleImage.get_width():
                    if man.y+playerHeight>520-obstacleImage.get_height():
                        if man.x>Screen3pos4+obstacle3x:
                            man.x = Screen3pos4+obstacle3x+obstacleImage.get_width()



                Screen.blit(playGameImage, (0, 0))
                Screen3box1_rect = [Screen3pos1 + obstacle3x, 520 - Screen3box1.height, Screen3box1.width, Screen3box1.height]
                Screen3box2_rect = [Screen3pos2 + obstacle3x, 520 - Screen3box2.height, Screen3box2.width, Screen3box2.height]
                Screen3box3_rect = [Screen3pos3 + obstacle3x, 520 - Screen3box3.height, Screen3box3.width, Screen3box3.height]
                Screen3box4_rect = [Screen3pos4 + obstacle3x, 520 - Screen3box4.height, Screen3box4.width, Screen3box4.height]

                if obstacle3x <= -720:
                    print(3)
                    Screen3 = False
                    obstacle3x = 520
                Screen.blit(playGameImage, (0 + background1x, 0))
                Screen.blit(playGameImage, (0 + background2x, 0))
                if background1x == -playGameImage.get_width():
                    background1x = background2x + playGameImage.get_width()
                if background2x == -playGameImage.get_width():
                    background2x = background1x + playGameImage.get_width()


                man.draw(Screen)
                pygame.draw.rect(Screen, menuBoxOuter.colour, menu_box_outer_rect)
                pygame.draw.rect(Screen, menuBoxMiddle.colour, menu_box_middle_rect)
                pygame.draw.rect(Screen, menuBoxInner.colour, menu_box_inner_rect)
                pygame.draw.rect(Screen, menuButton.colour, menu_button_rect)
                Screen.blit(menuButton.text,
                            (menu_button_rect[0] + (menuButton.width - menuButton.text.get_width()) / 2,
                             menu_button_rect[1] + (menuButton.height / 2 - menuButton.text.get_height() / 2) - 2.5))
                if not MenuHelp:
                    pygame.draw.rect(Screen, menuHelpButton.colour, menu_help_button_rect)
                    pygame.draw.rect(Screen, homeButton.colour, menu_home_button_rect)
                    pygame.draw.rect(Screen, menuQuitButton.colour, menu_quit_button_rect)
                    pygame.draw.rect(Screen, menuButton.colour, menu_button_rect)
                    Screen.blit(menuButton.text,
                                (menu_button_rect[0] + (menuButton.width - menuButton.text.get_width()) / 2,
                                 menu_button_rect[1] + (menuButton.height / 2 - menuButton.text.get_height() / 2) - 2.5))
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEMOTION:
                            x, y = event.pos
                    if (menu_button_rect[0] <= x <= menu_button_rect[0] + menu_button_rect[2] and menu_button_rect[
                        1] <= y <= menu_button_rect[1] + menu_button_rect[3]):
                        pygame.draw.rect(Screen, menuButton.over_colour, menu_button_rect)
                        pygame.draw.rect(Screen, menuHelpButton.colour, menu_help_button_rect)
                        pygame.draw.rect(Screen, homeButton.colour, menu_home_button_rect)
                        pygame.draw.rect(Screen, menuQuitButton.colour, menu_quit_button_rect)
                        Screen.blit(menuButton.text,
                                    (menu_button_rect[0] + (menuButton.width - menuButton.text.get_width()) / 2,
                                     menu_button_rect[1] + (menuButton.height / 2 - menuButton.text.get_height() / 2) - 2.5))
                    if Menu and (menu_quit_button_rect[0] <= x <= menu_quit_button_rect[0] + menu_quit_button_rect[2] and
                                 menu_quit_button_rect[
                                     1] <= y <= menu_quit_button_rect[1] + menu_quit_button_rect[3]):
                        pygame.draw.rect(Screen, menuQuitButton.over_colour, menu_quit_button_rect)
                        pygame.draw.rect(Screen, menuHelpButton.colour, menu_help_button_rect)
                        pygame.draw.rect(Screen, homeButton.colour, menu_home_button_rect)
                        pygame.draw.rect(Screen, menuButton.colour, menu_button_rect)
                        Screen.blit(menuButton.text,
                                    (menu_button_rect[0] + (menuButton.width - menuButton.text.get_width()) / 2,
                                     menu_button_rect[1] + (menuButton.height / 2 - menuButton.text.get_height() / 2) - 2.5))

                    if Menu and (menu_home_button_rect[0] <= x <= menu_home_button_rect[0] + menu_home_button_rect[2] and
                                 menu_home_button_rect[
                                     1] <= y <= menu_home_button_rect[1] + menu_home_button_rect[3]):
                        pygame.draw.rect(Screen, homeButton.over_colour, menu_home_button_rect)
                        pygame.draw.rect(Screen, menuHelpButton.colour, menu_help_button_rect)
                        pygame.draw.rect(Screen, menuQuitButton.colour, menu_quit_button_rect)
                        pygame.draw.rect(Screen, menuButton.colour, menu_button_rect)
                        Screen.blit(menuButton.text,
                                    (menu_button_rect[0] + (menuButton.width - menuButton.text.get_width()) / 2,
                                     menu_button_rect[1] + (menuButton.height / 2 - menuButton.text.get_height() / 2) - 2.5))

                    if Menu and (menu_help_button_rect[0] <= x <= menu_help_button_rect[0] + menu_help_button_rect[2] and
                                 menu_help_button_rect[
                                     1] <= y <= menu_help_button_rect[1] + menu_help_button_rect[3]):
                        pygame.draw.rect(Screen, menuHelpButton.over_colour, menu_help_button_rect)
                        pygame.draw.rect(Screen, homeButton.colour, menu_home_button_rect)
                        pygame.draw.rect(Screen, menuQuitButton.colour, menu_quit_button_rect)
                        pygame.draw.rect(Screen, menuButton.colour, menu_button_rect)
                        Screen.blit(menuButton.text,
                                    (menu_button_rect[0] + (menuButton.width - menuButton.text.get_width()) / 2,
                                     menu_button_rect[1] + (menuButton.height / 2 - menuButton.text.get_height() / 2) - 2.5))

                    Screen.blit(homeButton.text,
                                 (menu_home_button_rect[0] + (homeButton.width - homeButton.text.get_width()) / 2,
                                  menu_home_button_rect[1] + (homeButton.height / 2 - homeButton.text.get_height() / 2)))
                    Screen.blit(menuQuitButton.text, (menu_quit_button_rect[0] + (menuQuitButton.width - menuQuitButton.text.get_width()) / 2,
                                                   menu_quit_button_rect[1] + (menuQuitButton.height / 2 - menuQuitButton.text.get_height() / 2)))
                    Screen.blit(helpButton.text, (help_button_rect[0] + (helpButton.width - helpButton.text.get_width()) / 2,
                                                   menu_help_button_rect[1] + (
                                                               menuHelpButton.height / 2 - menuHelpButton.text.get_height() / 2)))
                    Screen.blit(menuName, ((Screen.get_width() - menuName.get_width()) / 2,
                                        0+(Screen.get_height() - menuName.get_height()) / 2 - 600+Screeny))

                if MenuHelp:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEMOTION:
                            x, y = event.pos
                    if (menu_button_rect[0] <= x <= menu_button_rect[0] + menu_button_rect[2] and menu_button_rect[
                        1] <= y <= menu_button_rect[1] + menu_button_rect[3]):
                        pygame.draw.rect(Screen, menuButton.over_colour, menu_button_rect)
                        Screen.blit(menuButton.text,
                                    (menu_button_rect[0] + (menuButton.width - menuButton.text.get_width()) / 2,
                                     menu_button_rect[1] + (menuButton.height / 2 - menuButton.text.get_height() / 2) - 2.5))

                    Screen.blit(helpName, ((Screen.get_width() - helpName.get_width()) / 2,
                                           0 + (Screen.get_height() - helpName.get_height()) / 2 - 600 + Screeny))

                if obstacley % (15 + variable) == 0:
                    obstacle3x -= 20
                    if platform:
                        man.x-=20
                if not Menu:
                    background1x -= 1
                    background2x -= 1
                if obstacley % 1000 == 0:
                    variable -= 1
                if variable < 1:
                    variable = 1

            obstacle(Screen1pos1 + obstacle1x, 520 - obstacleImage.get_height(), obstacleImage.get_width(),
                     obstacleImage.get_height()).drawObstacle(Screen)
            obstacle(Screen1pos2 + obstacle1x, 520 - obstacleImage.get_height(), obstacleImage.get_width(),
                     obstacleImage.get_height()).drawObstacle(Screen)
            obstacle(Screen1pos3 + obstacle1x, 520 - obstacleImage.get_height(), obstacleImage.get_width(),
                     obstacleImage.get_height()).drawObstacle(Screen)
            obstacle(Screen1pos4 + obstacle1x, 520 - obstacleImage.get_height(), obstacleImage.get_width(),
                     obstacleImage.get_height()).drawObstacle(Screen)

            obstacle(Screen2pos1 + obstacle2x, 520 - obstacleImage.get_height(), obstacleImage.get_width(),
                     obstacleImage.get_height()).drawObstacle(Screen)
            obstacle(Screen2pos2 + obstacle2x, 520 - obstacleImage.get_height(), obstacleImage.get_width(),
                     obstacleImage.get_height()).drawObstacle(Screen)
            obstacle(Screen2pos3 + obstacle2x, 520 - obstacleImage.get_height(), obstacleImage.get_width(),
                     obstacleImage.get_height()).drawObstacle(Screen)
            obstacle(Screen2pos4 + obstacle2x, 520 - obstacleImage.get_height(), obstacleImage.get_width(),
                     obstacleImage.get_height()).drawObstacle(Screen)

            obstacle(Screen3pos1 + obstacle3x, 520 - obstacleImage.get_height(), obstacleImage.get_width(),
                     obstacleImage.get_height()).drawObstacle(Screen)
            obstacle(Screen3pos2 + obstacle3x, 520 - obstacleImage.get_height(), obstacleImage.get_width(),
                     obstacleImage.get_height()).drawObstacle(Screen)
            obstacle(Screen3pos3 + obstacle3x, 520 - obstacleImage.get_height(), obstacleImage.get_width(),
                     obstacleImage.get_height()).drawObstacle(Screen)
            obstacle(Screen3pos4 + obstacle3x, 520 - obstacleImage.get_height(), obstacleImage.get_width(),
                     obstacleImage.get_height()).drawObstacle(Screen)

            pygame.display.update()

while game_over == False:
    if Home:
        startGame()
    if Help:
        help()
    if mainGame:
        Game()