
import pygame as pyg
import random
import time


pyg.init()

winWidth = 800
winHeight = 600


background = (4,22,34)
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

playerWidth = 64
playerHeight = 64

Win = pyg.display.set_mode((winWidth,winHeight))
pyg.display.set_caption('tree')


sealion_up = pyg.image.load('sealion-up.png')
sealion_down = pyg.image.load('sealion-down.png')
seaweed = pyg.image.load('seaweed.png')
seafloor = pyg.image.load('seafloor.png')


clock = pyg.time.Clock()



def player(x,y):

    Win.blit(sealion_down,(x,y))

def text_objects(text,font):

    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
    

def message_display(text):

    largeText = pyg.font.Font('freesansbold.ttf',35)
    TextSurf, TextRect = text_objects(text,largeText)
    TextRect.center = ((winWidth/2),(winHeight/2))
    Win.blit(TextSurf,TextRect)


    pyg.display.update()

    time.sleep(2)

    game_loop()

def props(prop):

    for x in range(1,6):

        x = random.randrange(40,750,1)

        Win.blit(prop,(x,514))

        
def outofbounds():
    
    message_display("You left the Sea Lion's domain.")
    

def game_loop():
    
    x = (winWidth * 0.45)
    y = (winHeight * 0.8)

    x_change = 0

    gameExit = False


    
    while not gameExit:

        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                pyg.quit()
                quit()

                
            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_LEFT:
                    x_change = -5
                elif event.key ==  pyg.K_RIGHT:
                    x_change = 5


            if event.type == pyg.KEYUP:
                if event.key == pyg.K_LEFT or event.key == pyg.K_RIGHT:
                    x_change = 0


        x += x_change

        Win.fill(background)
        Win.blit(seafloor,(0,520))
        
        player(x,y)


        if x > winWidth - playerWidth or x < 0:
            outofbounds()

        pyg.display.update()
        clock.tick(60)


game_loop()

pyg.quit()
quit()
