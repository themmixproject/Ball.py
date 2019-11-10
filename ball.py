
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

counter = 0

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

# TO FUTURE STEVEN IMPROVE THIS
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
    "radius": pygame.image.load("circ.png").get_size()[0]/2,
    "ballSpeedVertical": 0.01,
    "ballSpeedHorizontal": 0.,
    "ballCollision": False,
    "ballGrab": False,
    "mouseButton": False
}

print(ball)

gravity = 0.001

friction = 0.89

# verticalSpeed = 0.01

# MOUSE
mouse = {
    "x": 0,
    "y": 0,
    "relX": 0,
    "relY": 0
}

def updateBall(dt):
    global friction, gravity

    # "deletes" old ball
    pygame.draw.rect(window, black, (ball["x"], ball["y"], ball["img"].get_size()[0], ball["img"].get_size()[1]))

    # //IMP posx += dirx * speed * deltatime
    # ball["y"] += 1 * verticalSpeed * dt
    if ball["ballCollision"] == True and ball["ballGrab"] == True or ball["mouseButton"] == True:
        ball["x"] = mouse["x"] - ball["radius"]
        ball["y"] = mouse["y"] - ball["radius"]

    else:

        if (ball["y"] + ball["height"] + ball["ballSpeedVertical"] > winHeight or ball["y"] + ball["ballSpeedVertical"] < 0):
            ball["ballSpeedVertical"] = -ball["ballSpeedVertical"] * friction
        else:
            ball["ballSpeedVertical"] += gravity
        
        ball["y"] += 1 * ball["ballSpeedVertical"] * dt
    
        if ball["x"] + ball["diameter"] + ball["ballSpeedHorizontal"] > winWidth:

            ball["ballSpeedHorizontal"] = -ball["ballSpeedHorizontal"] * friction

        elif ball["x"] + ball["ballSpeedHorizontal"] < 0:

            ball["ballSpeedHorizontal"] = -ball["ballSpeedHorizontal"] * friction

        ball["x"] += 1 * ball["ballSpeedHorizontal"] * dt

    temp = pygame.Surface(ball["img"].get_rect().size, pygame.SRCALPHA)
    temp.blit(ball["img"], (0, 0))
    temp.convert_alpha()

    window.blit(temp,( ball["x"], ball["y"]))
    
    
def checkBallCollision():

    mouse["x"], mouse["y"] = pygame.mouse.get_pos()

    if (mouse["x"] - ( ball["x"] + ball["radius"] ) < ball["radius"] and
        mouse["x"] - ( ball["x"] + ball["radius"] ) > -ball["radius"] and
        mouse["y"] - ( ball["y"] + ball["radius"] ) < ball["radius"] and
        mouse["y"] - ( ball["y"] + ball["radius"] ) > -ball["radius"]):
            ball["ballCollision"] = True
            ball["img"] = pygame.image.load("circ_test.png")
    else:
        ball["ballCollision"] = False
        ball["img"] = pygame.image.load("circ.png")


def eventHandler(event):
    global verticalSpeed, counter
    if event.type == pygame.QUIT:
        print("quit " + str(event))
        pygame.quit()
        quit()
    
    mouseButton = pygame.mouse.get_pressed()
    if mouseButton[0] == 1:

        if ball["ballCollision"] == True:
            ball["ballGrab"] = True
            ball["mouseButton"] = True
            mouse["relX"], mouse["relY"] = pygame.mouse.get_rel()

    elif mouseButton[0] == 0 and ball["ballGrab"] == True:
        # print("rel-x: " + str(mouse["relX"]) + " rel-y: " + str(mouse["relY"]) +  " pygame mouse rel: " + str(pygame.mouse.get_rel()))
        ball["ballGrab"] = False
        ball["mouseButton"] = False
        if(ball["mouseButton"] == False):

            ball["ballSpeedVertical"] = mouse["relY"] * 0.08
            ball["ballSpeedHorizontal"] = mouse["relX"] * 0.08



def core():
    clock = pygame.time.Clock()
    dt = clock.get_time()

    while True:
	#Input check 

        # AS IN, MAYBE JUST INCLUDE THE CLICK EVENTS
        for event in pygame.event.get():
            eventHandler(event)
            # print(str(event))
        checkBallCollision()
	#game logic
        # print(ball["y"])
        updateBall(dt)
	#Draw stuff

        # print(dt)

        pygame.display.update()
        dt = clock.tick()

# initialise
core()
