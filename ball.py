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
    "height": pygame.image.load("circ.png").get_size()[1],
    "diameter": pygame.image.load("circ.png").get_size()[0],
    "radius": pygame.image.load("circ.png").get_size()[0]/2
}

print(ball)

gravity = 0.001

friction = 0.89

verticalSpeed = 0.01

# MOUSE
mouse = {
    "x": 0,
    "y": 0
}


def updateBall(dt):
    global verticalSpeed, friction, gravity


    # "deletes" old ball
    pygame.draw.rect(window, black, (ball["x"], ball["y"], ball["img"].get_size()[0], ball["img"].get_size()[1]))

    # adds gravity and checks if it hit the bottom
    if ball["y"] + ball["height"] + verticalSpeed > 500:
        verticalSpeed = -verticalSpeed * friction
    else:
        verticalSpeed += gravity

    # posx += dirx * speed * deltatime
    ball["y"] += 1 * verticalSpeed * dt

    temp = pygame.Surface(ball["img"].get_rect().size, pygame.SRCALPHA)
    temp.blit(ball["img"], (0, 0))
    temp.convert_alpha()

    window.blit(temp,( ball["x"], ball["y"]))
    
    
    

counter = 0
def eventHandler(event):
    global verticalSpeed, counter
    if event.type == pygame.QUIT:
        print("quit " + str(event))
        pygame.quit()
        quit()
    if event.type == pygame.MOUSEMOTION:
        mouse["x"] = event.pos[0]
        mouse["y"] = event.pos[1]
        print( mouse["x"] - (ball["x"] + ball["radius"]) )



        if mouse["x"] - (ball["x"] + ball["radius"] ) < ball["radius"] and mouse["x"] - (ball["x"] + ball["radius"] ) > -ball["radius"] and mouse["y"] - (ball["y"] + ball["radius"]) < ball["radius"] and mouse["y"] - (ball["y"] + ball["radius"]) > -ball["radius"]:
                ball["img"] = pygame.image.load("circ_test.png")
        else:
            ball["img"] = pygame.image.load("circ.png")

        # print("True %d" % counter)
        # counter+=1
        


    mouseButton = pygame.mouse.get_pressed()
    # print(event.type)
    if mouseButton[0] == 1:
        pygame.draw.rect(window, black, (ball["x"], ball["y"], ball["img"].get_size()[0], ball["img"].get_size()[1]))
        verticalSpeed = 0.01
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
