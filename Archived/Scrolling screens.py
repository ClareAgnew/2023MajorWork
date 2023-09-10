import pygame
import random
pygame.init()
Screen = pygame.display.set_mode((520,520))
pygame.display.set_caption("SDD Assignment 2")
playGameImage = pygame.image.load('Game Screen.jpg')
obstacle = pygame.image.load("token_2.png")
game = True

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
        if game:
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

class box():
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

screen1pos1 = 750
screen1pos2 = 280
screen1pos3 = 99
screen1pos4 = 497

screen2pos1 = 246
screen2pos2 = 34
screen2pos3 = 487
screen2pos4 = 684

screen3pos1 = 725
screen3pos2 = 498
screen3pos3 = 235
screen3pos4 = 38

screen4pos1 = 34
screen4pos2 = 259
screen4pos3 = 485
screen4pos4 = 708

Screen1 = False
Screen2 = False
Screen3 = False
Screen4 = False

def screen():
    Clock = pygame.time.Clock()
    x = 520
    y = 0
    background1x = 0
    background2x = 1920
    variable = 0
    global game
    vel = 5
    global pos1,pos2,pos3,pos4
    global Screen1,Screen2,Screen3,Screen4
    while game:
        if not Screen1 and not Screen2 and not Screen3 and not Screen4:
            i = random.randint(0, 3)
            if i == 0:
                Screen1 = True
            if i == 1:
                Screen2 = True
            if i == 2:
                Screen3 = True
            if i == 3:
                Screen4 = True
            while Screen1:
                print("1")
                print(background2x)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game = False
                keys = pygame.key.get_pressed()

                if keys[pygame.K_LEFT]:
                    man.x -= vel
                    man.x += 1
                    man.left = True
                    man.right = False
                    man.standing = False
                elif keys[pygame.K_RIGHT]:
                    man.x += vel
                    man.right = True
                    man.left = False
                    man.standing = False
                else:
                    man.standing = True
                    man.walkCount = 0

                if not (man.isJump):
                    if keys[pygame.K_UP]:
                        man.isJump = True
                        man.right = False
                        man.left = False
                        man.walkCount = 0
                else:
                    if man.jumpCount >= -10:
                        neg = 1
                        if man.jumpCount < 0:
                            neg = -1
                        man.y -= (man.jumpCount ** 2) * 0.5 * neg
                        man.jumpCount -= 1
                    else:
                        man.isJump = False
                        man.jumpCount = 10

                if not keys[pygame.K_UP]:
                    man.y += vel ^ 2

                if man.y > Screen.get_height() - playerHeight:
                    man.y = Screen.get_height() - playerHeight
                if man.x < 0:
                    man.x = 0
                if man.x > (Screen.get_width() - playerWidth):
                    man.x = Screen.get_width() - playerWidth
                for r in range(len(walkRight)):
                    walkRight[r] = pygame.transform.scale(walkRight[r], (playerWidth, playerHeight))
                for r in range(len(walkLeft)):
                    walkLeft[r] = pygame.transform.scale(walkLeft[r], (playerWidth, playerHeight))
                Clock.tick(35)
                Screen1box1_rect = [screen1pos1+x, 520-Screen1box1.height, Screen1box1.width, Screen1box1.height]
                Screen1box2_rect = [screen1pos2+x, 520-Screen1box2.height, Screen1box2.width, Screen1box2.height]
                Screen1box3_rect = [screen1pos3+x, 520-Screen1box3.height, Screen1box3.width, Screen1box3.height]
                Screen1box4_rect = [screen1pos4+x, 520-Screen1box4.height, Screen1box4.width, Screen1box4.height]

                if (Screen1box1_rect[0]) <= -Screen1box1.width and (Screen1box4_rect[0]) <= -Screen1box4.width and (Screen1box2_rect[0]) <= -Screen1box2.width and (Screen1box3_rect[0]) <= -Screen1box3.width:
                    #print(51)
                    x = 520
                    Screen1 = False
                Screen.blit(playGameImage, (0+background1x, 0))
                Screen.blit(playGameImage, (0 + background2x, 0))
                if background1x == -playGameImage.get_width():
                    background1x = background2x+playGameImage.get_width()
                if background2x == -playGameImage.get_width():
                    background2x = background1x+playGameImage.get_width()
                obstacle(screen1pos1+x,520-obstacleImage.get_height(),obstacleImage.get_width(),obstacleImage.get_height()).drawObstacle(Screen)
                obstacle(screen1pos2+x,520-obstacleImage.get_height(),obstacleImage.get_width(),obstacleImage.get_height()).drawObstacle(Screen)
                obstacle(screen1pos3+x,520-obstacleImage.get_height(),obstacleImage.get_width(),obstacleImage.get_height()).drawObstacle(Screen)
                obstacle(screen1pos4+x,520-obstacleImage.get_height(),obstacleImage.get_width(),obstacleImage.get_height()).drawObstacle(Screen)
                man.draw(Screen)
                pygame.display.update()
                #print(62)
                y+=1
                if y % (15 + variable) == 0:
                    x -= 20
                background1x-=1
                background2x-=1
                #print(64)
                if y%1000 == 0:
                    variable-=1
                if variable<1:
                    variable = 1
            while Screen2:
                print(background2x)
                print("2")
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game = False
                keys = pygame.key.get_pressed()

                if keys[pygame.K_LEFT]:
                    man.x -= vel
                    man.x += 1
                    man.left = True
                    man.right = False
                    man.standing = False
                elif keys[pygame.K_RIGHT]:
                    man.x += vel
                    man.right = True
                    man.left = False
                    man.standing = False
                else:
                    man.standing = True
                    man.walkCount = 0

                if not (man.isJump):
                    if keys[pygame.K_UP]:
                        man.isJump = True
                        man.right = False
                        man.left = False
                        man.walkCount = 0
                else:
                    if man.jumpCount >= -10:
                        neg = 1
                        if man.jumpCount < 0:
                            neg = -1
                        man.y -= (man.jumpCount ** 2) * 0.5 * neg
                        man.jumpCount -= 1
                    else:
                        man.isJump = False
                        man.jumpCount = 10

                if not keys[pygame.K_UP]:
                    man.y += vel ^ 2

                if man.y > Screen.get_height() - playerHeight:
                    man.y = Screen.get_height() - playerHeight
                if man.x < 0:
                    man.x = 0
                if man.x > (Screen.get_width() - playerWidth):
                    man.x = Screen.get_width() - playerWidth
                for r in range(len(walkRight)):
                    walkRight[r] = pygame.transform.scale(walkRight[r], (playerWidth, playerHeight))
                for r in range(len(walkLeft)):
                    walkLeft[r] = pygame.transform.scale(walkLeft[r], (playerWidth, playerHeight))
                Clock.tick(35)
                Screen2box1_rect = [screen2pos1 + x, 520 - Screen2box1.height, Screen2box1.width, Screen2box1.height]
                Screen2box2_rect = [screen2pos2 + x, 520 - Screen2box2.height, Screen2box2.width, Screen2box2.height]
                Screen2box3_rect = [screen2pos3 + x, 520 - Screen2box3.height, Screen2box3.width, Screen2box3.height]
                Screen2box4_rect = [screen2pos4 + x, 520 - Screen2box4.height, Screen2box4.width, Screen2box4.height]

                if (Screen2box1_rect[0]) <= -Screen2box1.width and (Screen2box4_rect[0]) <= -Screen2box4.width and (
                Screen2box2_rect[0]) <= -Screen2box2.width and (Screen2box3_rect[0]) <= -Screen2box3.width:
                    # print(51)
                    x = 520
                    Screen2 = False
                Screen.blit(playGameImage, (0 + background1x, 0))
                Screen.blit(playGameImage, (0 + background2x, 0))
                if background1x == -playGameImage.get_width():
                    background1x = background2x + playGameImage.get_width()
                if background2x == -playGameImage.get_width():
                    background2x = background1x + playGameImage.get_width()
                obstacle(screen1pos1 + x, 520 - obstacleImage.get_height(), obstacleImage.get_width(),
                         obstacleImage.get_height()).drawObstacle(Screen)
                obstacle(screen1pos2 + x, 520 - obstacleImage.get_height(), obstacleImage.get_width(),
                         obstacleImage.get_height()).drawObstacle(Screen)
                obstacle(screen1pos3 + x, 520 - obstacleImage.get_height(), obstacleImage.get_width(),
                         obstacleImage.get_height()).drawObstacle(Screen)
                obstacle(screen1pos4 + x, 520 - obstacleImage.get_height(), obstacleImage.get_width(),
                         obstacleImage.get_height()).drawObstacle(Screen)
                man.draw(Screen)
                pygame.display.update()
                # print(62)
                y += 1
                if y % (15 + variable) == 0:
                    x -= 20
                background1x-=1
                background2x-=1
                if y%1000 == 0:
                    variable-=1
                if variable<1:
                    variable = 1
                # print(64)
            while Screen3:
                print(background2x)
                print("3")
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game = False
                keys = pygame.key.get_pressed()

                if keys[pygame.K_LEFT]:
                    man.x -= vel
                    man.x += 1
                    man.left = True
                    man.right = False
                    man.standing = False
                elif keys[pygame.K_RIGHT]:
                    man.x += vel
                    man.right = True
                    man.left = False
                    man.standing = False
                else:
                    man.standing = True
                    man.walkCount = 0

                if not (man.isJump):
                    if keys[pygame.K_UP]:
                        man.isJump = True
                        man.right = False
                        man.left = False
                        man.walkCount = 0
                else:
                    if man.jumpCount >= -10:
                        neg = 1
                        if man.jumpCount < 0:
                            neg = -1
                        man.y -= (man.jumpCount ** 2) * 0.5 * neg
                        man.jumpCount -= 1
                    else:
                        man.isJump = False
                        man.jumpCount = 10

                if not keys[pygame.K_UP]:
                    man.y += vel ^ 2

                if man.y > Screen.get_height() - playerHeight:
                    man.y = Screen.get_height() - playerHeight
                if man.x < 0:
                    man.x = 0
                if man.x > (Screen.get_width() - playerWidth):
                    man.x = Screen.get_width() - playerWidth
                for r in range(len(walkRight)):
                    walkRight[r] = pygame.transform.scale(walkRight[r], (playerWidth, playerHeight))
                for r in range(len(walkLeft)):
                    walkLeft[r] = pygame.transform.scale(walkLeft[r], (playerWidth, playerHeight))

                Clock.tick(35)
                Screen3box1_rect = [screen3pos1 + x, 520-Screen3box1.height, Screen3box1.width, Screen3box1.height]
                Screen3box2_rect = [screen3pos2 + x, 520-Screen3box2.height, Screen3box2.width, Screen3box2.height]
                Screen3box3_rect = [screen3pos3 + x, 520-Screen3box3.height, Screen3box3.width, Screen3box3.height]
                Screen3box4_rect = [screen3pos4 + x, 520-Screen3box4.height, Screen3box4.width, Screen3box4.height]

                if (Screen3box1_rect[0]) <= -Screen3box1.width and (Screen3box4_rect[0]) <= -Screen3box4.width and (
                Screen3box2_rect[0]) <= -Screen3box2.width and (Screen3box3_rect[0]) <= -Screen3box3.width:
                    #print(51)
                    x = 520
                    Screen3 = False
                Screen.blit(playGameImage, (0 + background1x, 0))
                Screen.blit(playGameImage, (0 + background2x, 0))
                if background1x == -playGameImage.get_width():
                    background1x = background2x + playGameImage.get_width()
                if background2x == -playGameImage.get_width():
                    background2x = background1x + playGameImage.get_width()
                obstacle(screen3pos1 + x, 520 - obstacleImage.get_height(), obstacleImage.get_width(),
                         obstacleImage.get_height()).drawObstacle(Screen)
                obstacle(screen3pos2 + x, 520 - obstacleImage.get_height(), obstacleImage.get_width(),
                         obstacleImage.get_height()).drawObstacle(Screen)
                obstacle(screen3pos3 + x, 520 - obstacleImage.get_height(), obstacleImage.get_width(),
                         obstacleImage.get_height()).drawObstacle(Screen)
                obstacle(screen3pos4 + x, 520 - obstacleImage.get_height(), obstacleImage.get_width(),
                         obstacleImage.get_height()).drawObstacle(Screen)

                man.draw(Screen)
                pygame.display.update()
                #print(62)
                y += 1
                if y % (15 + variable) == 0:
                    x -= 20
                background1x-=1
                background2x-=1
                if y%1000 == 0:
                    variable-=1
                if variable<1:
                    variable = 1
                #print(64)
            while Screen4:
                print(background2x)
                print("4")
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game = False
                keys = pygame.key.get_pressed()

                if keys[pygame.K_LEFT]:
                    man.x -= vel
                    man.x += 1
                    man.left = True
                    man.right = False
                    man.standing = False
                elif keys[pygame.K_RIGHT]:
                    man.x += vel
                    man.right = True
                    man.left = False
                    man.standing = False
                else:
                    man.standing = True
                    man.walkCount = 0

                if not (man.isJump):
                    if keys[pygame.K_UP]:
                        man.isJump = True
                        man.right = False
                        man.left = False
                        man.walkCount = 0
                else:
                    if man.jumpCount >= -10:
                        neg = 1
                        if man.jumpCount < 0:
                            neg = -1
                        man.y -= (man.jumpCount ** 2) * 0.5 * neg
                        man.jumpCount -= 1
                    else:
                        man.isJump = False
                        man.jumpCount = 10

                if not keys[pygame.K_UP]:
                    man.y += vel ^ 2

                if man.y > Screen.get_height() - playerHeight:
                    man.y = Screen.get_height() - playerHeight
                if man.x < 0:
                    man.x = 0
                if man.x > (Screen.get_width() - playerWidth):
                    man.x = Screen.get_width() - playerWidth
                for r in range(len(walkRight)):
                    walkRight[r] = pygame.transform.scale(walkRight[r], (playerWidth, playerHeight))
                for r in range(len(walkLeft)):
                    walkLeft[r] = pygame.transform.scale(walkLeft[r], (playerWidth, playerHeight))

                Clock.tick(35)
                Screen4box1_rect = [screen4pos1 + x, 520-Screen4box1.height, Screen4box1.width, Screen4box1.height]
                Screen4box2_rect = [screen4pos2 + x, 520-Screen4box2.height, Screen4box2.width, Screen4box2.height]
                Screen4box3_rect = [screen4pos3 + x, 520-Screen4box3.height, Screen4box3.width, Screen4box3.height]
                Screen4box4_rect = [screen4pos4 + x, 520-Screen4box4.height, Screen4box4.width, Screen4box4.height]

                if (Screen4box1_rect[0]) <= -Screen4box1.width and (Screen4box4_rect[0]) <= -Screen4box4.width and (
                Screen4box2_rect[0]) <= -Screen4box2.width and (Screen4box3_rect[0]) <= -Screen4box3.width:
                    #print(51)
                    x = 520
                    Screen4 = False
                Screen.blit(playGameImage, (0 + background1x, 0))
                Screen.blit(playGameImage, (0 + background2x, 0))
                if background1x == -playGameImage.get_width():
                    background1x = background2x + playGameImage.get_width()
                if background2x == -playGameImage.get_width():
                    background2x = background1x + playGameImage.get_width()
                obstacle(screen4pos1 + x, 520 - obstacleImage.get_height(), obstacleImage.get_width(),
                         obstacleImage.get_height()).drawObstacle(Screen)
                obstacle(screen4pos2 + x, 520 - obstacleImage.get_height(), obstacleImage.get_width(),
                         obstacleImage.get_height()).drawObstacle(Screen)
                obstacle(screen4pos3 + x, 520 - obstacleImage.get_height(), obstacleImage.get_width(),
                         obstacleImage.get_height()).drawObstacle(Screen)
                obstacle(screen4pos4 + x, 520 - obstacleImage.get_height(), obstacleImage.get_width(),
                         obstacleImage.get_height()).drawObstacle(Screen)

                man.draw(Screen)
                pygame.display.update()
                #print(62)
                y += 1
                print(y)
                if y % (15 + variable) == 0:
                    x -= 20
                background1x-=1
                background2x-=1
                if y%1000 == 0:
                    variable-=1
                if variable<1:
                    variable = 1
                #print(64)

while game:
    screen()
