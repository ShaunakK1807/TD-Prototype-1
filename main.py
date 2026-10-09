import pygame as pg
import numpy as np
import constants as c
#initialise pygame
pg.init()


#create clock object to control the frame rate
clock = pg.time.Clock()


#create the game window
screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
#set caption for the game window
pg.display.set_caption("TD Prototype 1")

clock.tick(c.FPS) #set the frame rate to 60 fps
run = True
while run:
    #event handling
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False


pg.quit()
