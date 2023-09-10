import pygame

pygame.init()

#Functional test made, mousebuttonover works



#-------------------WELCOME----------------------------


welcome = pygame.display.set_mode((500,540))
helpScreen = pygame.display.set_mode((520,520))
pygame.display.set_caption("SDD Assignment 2")
startGameImage = pygame.image.load('Home Screen.jpg')
font_1 = pygame.font.SysFont("Verdana",20)
text_colour_1 = (255,255,255)

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

start_button_rect = [(welcome.get_width()-startButton.width)/2,(welcome.get_height()-startButton.height)/2+50,startButton.width,startButton.height]
help_button_rect = [(welcome.get_width()-helpButton.width)/2,(welcome.get_height()-helpButton.height)/2-10,helpButton.width,helpButton.height]
quit_button_rect = [(welcome.get_width()-quitButton.width)/2,(welcome.get_height()-quitButton.height)/2+110,quitButton.width,quitButton.height]
gameName = font_1.render("SDD Major Work", True, text_colour_1)

game_over = False
mainGame = False
Home = True
Help = False
def startGame():
    x, y = (0, 0)
    global game_over
    global mainGame
    global Home
    global Help
    while not game_over and not mainGame and not Help:
        welcome.blit(startGameImage,(0,0))
        pygame.draw.rect(welcome, startButton.colour, start_button_rect)
        pygame.draw.rect(welcome, quitButton.colour, quit_button_rect)
        pygame.draw.rect(welcome, helpButton.colour, help_button_rect)
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
            pygame.draw.rect(welcome, startButton.over_colour, start_button_rect)
            pygame.draw.rect(welcome, quitButton.colour, quit_button_rect)
            pygame.draw.rect(welcome, helpButton.colour, help_button_rect)


        if (quit_button_rect[0] <= x <= quit_button_rect[0] + quit_button_rect[2] and quit_button_rect[1] <= y <=
                quit_button_rect[1] + quit_button_rect[3]):
            pygame.draw.rect(welcome, startButton.colour, start_button_rect)
            pygame.draw.rect(welcome, quitButton.over_colour, quit_button_rect)
            pygame.draw.rect(welcome, helpButton.colour, help_button_rect)

        if (help_button_rect[0] <= x <= help_button_rect[0] + help_button_rect[2] and help_button_rect[1] <= y <=
                help_button_rect[1] + help_button_rect[3]):
            pygame.draw.rect(welcome, startButton.colour, start_button_rect)
            pygame.draw.rect(welcome, helpButton.over_colour, help_button_rect)
            pygame.draw.rect(welcome, quitButton.colour, quit_button_rect)


        welcome.blit(startButton.text, (start_button_rect[0] + (startButton.width - startButton.text.get_width()) / 2,
                                  start_button_rect[1] + (startButton.height / 2 - startButton.text.get_height() / 2)))
        welcome.blit(quitButton.text, (quit_button_rect[0] + (quitButton.width - quitButton.text.get_width()) / 2,
                                        quit_button_rect[1] + (quitButton.height / 2 - quitButton.text.get_height() / 2)))
        welcome.blit(helpButton.text, (help_button_rect[0] + (helpButton.width - helpButton.text.get_width()) / 2,
                                        help_button_rect[1] + (helpButton.height / 2 - helpButton.text.get_height() / 2)))
        welcome.blit(gameName, ((welcome.get_width() - gameName.get_width())/2, (welcome.get_height()-gameName.get_height())/2-70))


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
help_box_outer_rect = [(helpScreen.get_width()-helpBoxOuter.width)/2,(helpScreen.get_height()-helpBoxOuter.height)/2,helpBoxOuter.width,helpBoxOuter.height]
help_box_middle_rect = [(helpScreen.get_width()-helpBoxMiddle.width)/2,(helpScreen.get_height()-helpBoxMiddle.height)/2,helpBoxMiddle.width,helpBoxMiddle.height]
help_box_inner_rect = [(helpScreen.get_width()-helpBoxInner.width)/2,(helpScreen.get_height()-helpBoxInner.height)/2,helpBoxInner.width,helpBoxInner.height]

returnButton = button(125,50, (0,68,185), (30,30,30), font_1.render("Return", True, text_colour_1))

return_button_rect = [(helpScreen.get_width()-returnButton.width)/2,(helpScreen.get_height()-returnButton.height)/2+150,quitButton.width,quitButton.height]


def help():
    global game_over
    helpScreen.blit(startGameImage, (0, 0))
    pygame.draw.rect(helpScreen, helpBoxOuter.colour, help_box_outer_rect)
    pygame.draw.rect(helpScreen, helpBoxMiddle.colour, help_box_middle_rect)
    pygame.draw.rect(helpScreen, helpBoxInner.colour, help_box_inner_rect)
    pygame.draw.rect(helpScreen, returnButton.colour, return_button_rect)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

while game_over == False:
    if Home:
        startGame()
    if Help:
        help()