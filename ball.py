
# imports
import pygame

from pygame import gfxdraw
# from pygame import blit
import time
import random

pygame.init()

winHeight = 500
winWidth = 500

black = (0, 0, 0)
white = (255, 255, 255)


# setup window
window = pygame.display.set_mode([winWidth, winHeight])

# get center
center = {
    "x":0,
    "y":0
}

center["x"], center["y"] = map( lambda x : int(x/2), pygame.display.get_surface().get_size() )

# ball coordinates
ball = {
    "x": center["x"],
    "y": center["y"],
    "radius": 30
}

clock = pygame.time.Clock()

frameTime = 0

window.fill(black)

def updateBall(dt):
    drawCirc(ball["x"], ball["y"], ball["radius"], white)


def eventHandler(event):
    if event.type == pygame.QUIT:
        print("quit " + str(event))
        pygame.quit()
        quit()

def core():
    dt = clock.get_time()

    while True:
	#Input check 
        # make this more efficient
        # AS IN, MAYBE JUST INCLUDE THE CLICK EVENTS

        for event in pygame.event.get():
            eventHandler(event)
            # print(str(event))
	#game logic
        updateBall(dt)

	#Draw stuff

        print(dt)

        pygame.display.update()
        dt = clock.tick()

# initialise
core()
