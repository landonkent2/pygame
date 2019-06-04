
import pygame as pyg
import random
import time


pyg.init()
Win = pyg.display.set_mode((800,600))
coolperson = pyg.image.load('cool.png')
pyg.display.set_caption('tree')

clock = pyg.time.Clock()

dead = False

while not dead:

    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            dead = True


    pyg.display.update()
    clock.tick(60)

pyg.quit()
quit()
