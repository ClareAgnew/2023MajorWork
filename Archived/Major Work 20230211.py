import pygame
pygame.init()

#User Interface Test, User can navigate easily between screens

#-------------------WELCOME----------------------------

Screen = pygame.display.set_mode((520,520))
pygame.display.set_caption("SDD Assignment 2")
startGameImage = pygame.image.load('Home Screen.jpg')
playGameImage = pygame.image.load('Game Screen.jpg')
font_1 = pygame.font.SysFont("Verdana",20)
font_2 = pygame.font.SysFont("Verdana",30)
text_colour_1 = (255,255,255)
text_colour_2 = (255,23,15)

playerWidth = (pygame.image.load('Charactere_Idle_Left_0.png')).get_width()
playerHeight = (pygame.image.load('Charactere_Idle_Left_0.png')).get_height()
walkRight = [pygame.image.load('Charater_Walk_Right_0.png'), pygame.image.load('Charater_Walk_Right_1.png'), pygame.image.load('Charater_Walk_Right_2.png'), pygame.image.load('Charater_Walk_Right_3.png'), pygame.image.load('Charater_Walk_Right_4.png'), pygame.image.load('Charater_Walk_Right_5.png'), pygame.image.load('Charater_Walk_Right_6.png'), pygame.image.load('Charater_Walk_Right_7.png')]
walkLeft = [pygame.image.load('Character_Walk_Left_0.png'), pygame.image.load('Character_Walk_Left_1.png'), pygame.image.load('Character_Walk_Left_2.png'), pygame.image.load('Character_Walk_Left_3.png'), pygame.image.load('Character_Walk_Left_4.png'), pygame.image.load('Character_Walk_Left_5.png'), pygame.image.load('Character_Walk_Left_6.png'), pygame.image.load('Character_Walk_Left_7.png')]
jumpRight = [pygame.image.load('Character_Jump_Right_0.png'), pygame.image.load('Character_Jump_Right_1.png'), pygame.image.load('Character_Jump_Right_2.png')]
jumpLeft = [pygame.image.load('Character_Jump_Left_0.png'), pygame.image.load('Character_Jump_Left_1.png'), pygame.image.load('Character_Jump_Left_2.png')]


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

start_button_rect = [(Screen.get_width()-startButton.width)/2,(Screen.get_height()-startButton.height)/2+50,startButton.width,startButton.height]
help_button_rect = [(Screen.get_width()-helpButton.width)/2,(Screen.get_height()-helpButton.height)/2-10,helpButton.width,helpButton.height]
quit_button_rect = [(Screen.get_width()-quitButton.width)/2,(Screen.get_height()-quitButton.height)/2+110,quitButton.width,quitButton.height]
gameName = font_1.render("SDD Major Work", True, text_colour_1)

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


helpBoxOuterWidth = 75
helpBoxOuterHeight = 75

class box:
    def __init__(self, width, height, colour):
        self.width = width
        self.height = height
        self.colour = colour

helpBoxOuter = box(460,460,(218,118,159))
helpBoxMiddle = box(450,450,(255,162,157))
helpBoxInner = box(430,430,(255,219,208))
help_box_outer_rect = [(Screen.get_width()-helpBoxOuter.width)/2,(Screen.get_height()-helpBoxOuter.height)/2,helpBoxOuter.width,helpBoxOuter.height]
help_box_middle_rect = [(Screen.get_width()-helpBoxMiddle.width)/2,(Screen.get_height()-helpBoxMiddle.height)/2,helpBoxMiddle.width,helpBoxMiddle.height]
help_box_inner_rect = [(Screen.get_width()-helpBoxInner.width)/2,(Screen.get_height()-helpBoxInner.height)/2,helpBoxInner.width,helpBoxInner.height]

returnButton = button(125,50, (0,68,185), (30,30,30), font_1.render("Return", True, text_colour_1))

return_button_rect = [(Screen.get_width()-returnButton.width)/2,(Screen.get_height()-returnButton.height)/2+150,quitButton.width,quitButton.height]

helpName = font_2.render("Help", True, text_colour_2)

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



def Game():
    (x, y) = (0, 0)
    screeny = 0
    vel = 5
    global game_over
    global mainGame
    global Help
    global Home
    global Menu
    while not game_over and not Help and not Home:
        menuButton = button(25, 25, (0, 68, 185), (30, 30, 30), font_1.render("||", True, text_colour_1))
        homeButton = button(125, 50, (0, 68, 185), (30, 30, 30), font_1.render("Home", True, text_colour_1))
        menuQuitButton = button(125, 50, (0, 68, 185), (30, 30, 30), font_1.render("Quit", True, text_colour_1))
        menuHelpButton = button(125, 50, (0, 68, 185), (30, 30, 30), font_1.render("Help", True, text_colour_1))
        menu_button_rect = [(Screen.get_width() - menuButton.width) - 20, 20, menuButton.width,
                            menuButton.height]
        menu_help_button_rect = [(Screen.get_width() - menuHelpButton.width) / 2,
                                 (0 - menuHelpButton.height) - 190 + screeny, menuHelpButton.width,
                                 menuHelpButton.height]
        menu_quit_button_rect = [(Screen.get_width() - menuQuitButton.width) / 2,
                                 (0 - menuQuitButton.height) - 70 + screeny, menuQuitButton.width,
                                 menuQuitButton.height]
        menu_home_button_rect = [(Screen.get_width() - homeButton.width) / 2,
                                 (0 - homeButton.height) - 130 + screeny,
                                 homeButton.width, homeButton.height]
        menuName = font_2.render("Menu", True, text_colour_2)

        menuBoxOuter = box(460, 460, (218, 118, 159))
        menuBoxMiddle = box(450, 450, (255, 162, 157))
        menuBoxInner = box(430, 430, (255, 219, 208))

        menu_box_outer_rect = [(Screen.get_width() - menuBoxOuter.width) / 2, (screeny - menuBoxOuter.height),
                               menuBoxOuter.width, menuBoxOuter.height]
        menu_box_middle_rect = [(Screen.get_width() - menuBoxMiddle.width) / 2,
                                (screeny - menuBoxMiddle.height - 5),
                                menuBoxMiddle.width, menuBoxMiddle.height]
        menu_box_inner_rect = [(Screen.get_width() - menuBoxInner.width) / 2, (screeny - menuBoxInner.height - 15),
                               menuBoxInner.width, menuBoxInner.height]
        Screen.blit(playGameImage, (0, 0))
        pygame.draw.rect(Screen, menuBoxOuter.colour, menu_box_outer_rect)
        pygame.draw.rect(Screen, menuBoxMiddle.colour, menu_box_middle_rect)
        pygame.draw.rect(Screen, menuBoxInner.colour, menu_box_inner_rect)
        pygame.draw.rect(Screen, homeButton.colour, menu_home_button_rect)
        pygame.draw.rect(Screen, menuQuitButton.colour, menu_quit_button_rect)
        pygame.draw.rect(Screen, menuHelpButton.colour, menu_help_button_rect)
        pygame.draw.rect(Screen, menuButton.colour, menu_button_rect)

        clock = pygame.time.Clock()
        clock.tick(24)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True


            pygame.display.update()
            # Mousebuttondown
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if (menu_button_rect[0] <= x <= menu_button_rect[0] + menu_button_rect[2] and menu_button_rect[
                    1] <= y <= menu_button_rect[1] + menu_button_rect[3]):
                    if Menu:
                        Menu = False
                    else:
                        Menu = True

                if Menu and (menu_quit_button_rect[0] <= x <= menu_quit_button_rect[0] + menu_quit_button_rect[2] and menu_quit_button_rect[
                    1] <= y <= menu_quit_button_rect[1] + menu_quit_button_rect[3]):
                    game_over = True
                if Menu and (menu_home_button_rect[0] <= x <= menu_home_button_rect[0] + menu_home_button_rect[2] and menu_home_button_rect[
                    1] <= y <= menu_home_button_rect[1] + menu_home_button_rect[3]):
                    Menu = False
                    mainGame = False
                    Home = True
                if Menu and (menu_help_button_rect[0] <= x <= menu_help_button_rect[0] + menu_help_button_rect[2] and menu_help_button_rect[
                    1] <= y <= menu_help_button_rect[1] + menu_help_button_rect[3]):
                    Menu = False
                    mainGame = False
                    Help = True


            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
        if (menu_button_rect[0] <= x <= menu_button_rect[0] + menu_button_rect[2] and menu_button_rect[
            1] <= y <= menu_button_rect[1] + menu_button_rect[3]):
            pygame.draw.rect(Screen, menuButton.over_colour, menu_button_rect)

        if Menu and (menu_quit_button_rect[0] <= x <= menu_quit_button_rect[0] + menu_quit_button_rect[2] and menu_quit_button_rect[
            1] <= y <= menu_quit_button_rect[1] + menu_quit_button_rect[3]):
            pygame.draw.rect(Screen, menuQuitButton.over_colour, menu_quit_button_rect)

        if Menu and (menu_home_button_rect[0] <= x <= menu_home_button_rect[0] + menu_home_button_rect[2] and menu_home_button_rect[
            1] <= y <= menu_home_button_rect[1] + menu_home_button_rect[3]):
            pygame.draw.rect(Screen, homeButton.over_colour, menu_home_button_rect)
        if Menu and (menu_help_button_rect[0] <= x <= menu_help_button_rect[0] + menu_help_button_rect[2] and menu_help_button_rect[
            1] <= y <= menu_help_button_rect[1] + menu_help_button_rect[3]):
            pygame.draw.rect(Screen, menuHelpButton.over_colour, menu_help_button_rect)
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
                man.walkCount = 0
        else:
            if man.jumpCount >= -10 and not Menu:
                neg = 1
                if man.jumpCount < 0:
                    neg = -1
                man.y -= (man.jumpCount ** 2) * 0.5 * neg
                man.jumpCount -= 1
            elif Menu:
                man.jumpCount -= 0
            else:
                man.isJump = False
                man.jumpCount = 10

        if not keys[pygame.K_UP] and not Menu:
            man.y += vel ^ 2

        if man.y > Screen.get_height() - playerHeight:
            man.y = Screen.get_height() - playerHeight
        if man.x < 0:
            man.x = 0
        if man.x > (Screen.get_width() - playerWidth):
            man.x = Screen.get_width() - playerWidth

        man.draw(Screen)
        Screen.blit(homeButton.text,
                     (menu_home_button_rect[0] + (homeButton.width - homeButton.text.get_width()) / 2,
                      menu_home_button_rect[1] + (homeButton.height / 2 - homeButton.text.get_height() / 2)))
        Screen.blit(menuQuitButton.text, (menu_quit_button_rect[0] + (menuQuitButton.width - menuQuitButton.text.get_width()) / 2,
                                       menu_quit_button_rect[1] + (menuQuitButton.height / 2 - menuQuitButton.text.get_height() / 2)))
        Screen.blit(helpButton.text, (help_button_rect[0] + (helpButton.width - helpButton.text.get_width()) / 2,
                                       menu_help_button_rect[1] + (
                                                   menuHelpButton.height / 2 - menuHelpButton.text.get_height() / 2)))
        Screen.blit(menuName, ((Screen.get_width() - menuName.get_width()) / 2,
                                0-(Screen.get_height() - menuName.get_height()) / 2 - 395+screeny))


        Screen.blit(menuButton.text,
                     (menu_button_rect[0] + (menuButton.width - menuButton.text.get_width()) / 2,
                      menu_button_rect[1] + (menuButton.height / 2 - menuButton.text.get_height() / 2)-2.5))
        if Menu and screeny < 500:
            screeny += 75
        if Menu and screeny>500:
            screeny = 500
        if not Menu and screeny>0:
            screeny-=75
        if not Menu and screeny<0:
            screeny = 0
        pygame.display.update()


while game_over == False:
    if Home:
        startGame()
    if Help:
        help()
    if mainGame:
        Game()