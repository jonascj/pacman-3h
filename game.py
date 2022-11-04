# Pac-Man clone made for learning/teaching git and Python

import time
import pygame as pg

## Setup ##
pg.init()

screen = pg.display.set_mode((300,400))
pg.display.set_caption("Pac-Man (clone)")

## Game loop ##
running = True
while running:
    
    ## Handle events (keypresses etc.)
    events = pg.event.get()
    for event in events:

        # Close window (e.g. pressing [x] or Ctrl+F4)
        if event.type == pg.QUIT:
            running = False

    ## Draw ##
    screen.fill((0,0,0)) # Black
    pg.draw.circle(screen, (220,220,10), (100,200), 16)


    # Update window with newly drawn pixels
    pg.display.flip()  

    # Limit framerate by waiting a 10-100 milliseconds
    time.sleep(0.02)