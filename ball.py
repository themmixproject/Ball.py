# if (ball["y"] + (ball["width"]/2) + verticalSpeed) > 500:
#    verticalSpeed = -verticalSpeed * friction
# else:
#    verticalSpeed += gravity

# print(verticalSpeed)

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
red = (255, 0, 0)


# setup window
window = pygame.display.set_mode([winWidth, winHeight])

window.fill(black)

# get center
center = {
    "x":0,
    "y":0
}

center["x"], center["y"] = map( lambda x : int(x/2), pygame.display.get_surface().get_size() )

# ball coordinates

# TO MORE AWAKE STEVEN IMPROVE THIS
ball = {
    "x": center["x"],
    "y": center["y"],
    "radius": 30,
    "img": pygame.image.load("circ.png"),
    "size": pygame.image.load("circ.png").get_size(),
    "width": pygame.image.load("circ.png").get_size()[0],
    "height": pygame.image.load("circ.png").get_size()[1]
}

print(ball)

gravity = 0.001

friction = 0.89

verticalSpeed = 0.01

def updateBall(dt=1):
    global verticalSpeed, friction, gravity


    # "deletes" old ball
    pygame.draw.rect(window, black, (ball["x"], ball["y"], ball["img"].get_size()[0], ball["img"].get_size()[1]))
    


    # if (ball["y"] + (ball["width"]/2) + verticalSpeed) > 500:
    #    verticalSpeed = -verticalSpeed * friction
    # else:
    #    verticalSpeed += gravity

    if ball["y"] + ball["height"] + verticalSpeed > 500:
        verticalSpeed = -verticalSpeed * friction
    else:
        verticalSpeed += gravity

    ball["y"] += 1 * verticalSpeed * dt

    # if ball["y"] + ball["height"] > 500:
    #     ball["y"] = 250
    # else:
    #     ball["y"] += 1 * dt


    temp = pygame.Surface(ball["img"].get_rect().size, pygame.SRCALPHA)
    temp.blit(ball["img"], (0, 0))
    temp.convert_alpha()

    # window.blit( ball["img"], (ball["x"], ball["y"]) )
    window.blit(temp,( ball["x"], ball["y"]))

    # posx += dirx * speed * deltatime
    
    
    


def eventHandler(event):
    if event.type == pygame.QUIT:
        print("quit " + str(event))
        pygame.quit()
        quit()
    mouseButton = pygame.mouse.get_pressed()
    if mouseButton[0] == 1:
        pygame.draw.rect(window, black, (ball["x"], ball["y"], ball["img"].get_size()[0], ball["img"].get_size()[1]))
        ball["y"] = 250


def core():
    clock = pygame.time.Clock()
    dt = clock.get_time()

    while True:
	#Input check 

        # AS IN, MAYBE JUST INCLUDE THE CLICK EVENTS
        for event in pygame.event.get():
            eventHandler(event)
            # print(str(event))
	#game logic
        updateBall(dt)

	#Draw stuff

        # print(dt)

        pygame.display.update()
        dt = clock.tick()

# initialise
core()
