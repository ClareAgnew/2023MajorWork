import pygame
pygame.init()
Screen = pygame.display.set_mode((520,520))
pygame.display.set_caption("SDD Assignment 2")
playGameImage = pygame.image.load('Game Screen.jpg')
game = True
class box:
    def __init__(self, width, height, colour):
        self.width = width
        self.height = height
        self.colour = colour
Screen1box1 = box(40,40,(218,118,159))
Screen1box2 = box(80,165,(184,39,86))
Screen1box3 = box(75,63,(64,75,49))
Screen1box4 = box(20,54,(89,54,64))


def screen():
    Clock = pygame.time.Clock()
    x = 0
    global game
    while game:
        Clock.tick(24)
        Screen1box1_rect = [450+x, 460, Screen1box1.width, Screen1box1.height]
        Screen1box2_rect = [60+x, 340, Screen1box2.width, Screen1box2.height]
        Screen1box3_rect = [99+x, 49, Screen1box3.width, Screen1box3.height]
        Screen1box4_rect = [397+x, 97, Screen1box4.width, Screen1box4.height]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
        Screen.blit(playGameImage, (0, 0))
        pygame.draw.rect(Screen, Screen1box2.colour, Screen1box2_rect)
        pygame.draw.rect(Screen, Screen1box1.colour, Screen1box1_rect)
        pygame.draw.rect(Screen, Screen1box3.colour, Screen1box3_rect)
        pygame.draw.rect(Screen, Screen1box4.colour, Screen1box4_rect)
        pygame.display.update()
        x+=1

screen()