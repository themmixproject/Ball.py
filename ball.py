#
# TO MORE AWAKE STEVEN
# 
# - REPLACE BALL HEIGHT AND WITH WITH "DIAMETER"
# 
# - Make a limit for the sound on low speeds ;P
# - So, a way to make multiple sounds play on one channel is to let it stop playing the current sound
# - fix the bug that if you move the window
# the ball doesn't go off screen
# - fix the bug that somehow the ball sometimes goes
# off screen (just copy the other force fix from the ball drag function)
# - maybe an option to split the coordinate calculation
#  and the drawing functions
# 
# 
# 
# asd




# imports
import pygame

from pygame import gfxdraw
# from pygame import blit
import time
import random


pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init(22100, -16, 2, 64)
# pygame.mixer.init()
pygame.init()

# pygame.mixer.init()

pygame.mixer.set_num_channels(2000)

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
    "oldX":0,
    "oldY":0,
    "radius": 30,# Look at this
    "img": pygame.image.load("circ.png"),
    # "size": pygame.image.load("circ.png").get_size(),
    # "width": pygame.image.load("circ.png").get_size()[0],
    # "height": pygame.image.load("circ.png").get_size()[1],
    "diameter": pygame.image.load("circ.png").get_size()[0],
    "radius": pygame.image.load("circ.png").get_size()[0]/2,
    "ballSpeedVertical": 0.01,
    "ballSpeedHorizontal": 0.,
    "ballCollision": False,
    "ballGrab": False,
    "mouseButton": False
}

print(ball)

def easeLinear(t, b, c, d):
    return c*t/d + b

class trailBall:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alpha = 1.
        self.currentIteration = 0
        self.iterations = 15


    def update(self):
        # pygame.draw.rect(window, black, (this.x, this.y, ball["img"].get_size()[0], ball["img"].get_size()[1]))
        # pygame.draw.rect(window, black, (this.x, this.y, ball["img"].get_size()[0], ball["img"].get_size()[1]))
        temp = pygame.Surface(ball["img"].get_rect().size, pygame.SRCALPHA)

        
        imageCopy = ball["img"].copy()
        # this works on images with per pixel alpha too
        imageCopy.fill((255, 255, 255, self.alpha), None, pygame.BLEND_RGBA_MULT)


        temp.blit(imageCopy, (0, 0))
        temp.convert_alpha()
        # temp.set_alpha(this.alpha)

        # print(temp.get_alpha())
        window.blit(temp,(self.x, self.y))

        self.alpha = easeLinear(self.currentIteration, 255, -255, self.iterations)
        # this.currentIteration+=1
    def printStuff(self):
        print("trailBall class has been called")
    def draw(self):
        # pygame.draw.rect(window, black, (this.x, this.y, ball["img"].get_size()[0], ball["img"].get_size()[1]))

        temp = pygame.Surface(ball["img"].get_rect().size, pygame.SRCALPHA)
        
        imageCopy = ball["img"].copy()
        # this works on images with per pixel alpha too
        # imageCopy.fill((255, 255, 255), None, pygame.BLEND_RGBA_MULT)
        
        temp.blit(imageCopy, (0, 0))
        temp.convert_alpha()

        window.blit(temp,(this.x, this.y))


trailBallArr = []

gravity = 0.003

friction = 0.89

# verticalSpeed = 0.01

# MOUSE
mouse = {
    "x": 0,
    "y": 0,
    "relX": 0,
    "relY": 0
}

bounce = pygame.mixer.Sound("bounce1.wav")

def playBounce(speed):
    channel = pygame.mixer.find_channel()
    # channel.set_volume(abs(speed/5))
    channel.play(bounce)
    
    while pygame.mixer.find_channel() is None: 
        print (pygame.mixer.find_channel)
    # pygame.mixer.stop()
    # print(bounce.get_volume())
    # bounce.set_volume(abs(speed)/5)
    # pygame.mixer.find_channel().play(bounce)
    

def updateBall(dt):
    global friction, gravity

    ball["oldX"] = ball["x"]
    ball["oldY"] = ball["y"]

    if ball["ballCollision"] == True and ball["ballGrab"] == True or ball["mouseButton"] == True:
        # if(ball["x"] > 0 and ball["x"] + ball["diameter"] < winWidth and ball["y"] > 0 and ball["y"] + ball["height"] < winHeight):
        ball["x"] = mouse["x"] - ball["radius"]
        ball["y"] = mouse["y"] - ball["radius"]

        if ball["x"] <= 0:
            ball["x"] = 0
        elif ball["x"] + ball["diameter"] >= winWidth:
            ball["x"] = winWidth - ball["diameter"]
        if ball["y"] <= 0:
            ball["y"] = 0
        elif ball["y"] + ball["diameter"] >= winHeight:
            ball["y"] = winWidth - ball["diameter"]

    else:

        if (ball["y"] + ball["diameter"] + ball["ballSpeedVertical"] > winHeight or
            ball["y"] + ball["ballSpeedVertical"] < 0):
            ball["ballSpeedVertical"] = -ball["ballSpeedVertical"] * friction

            if(abs(ball["ballSpeedVertical"]) > 0.06):

                playBounce(ball["ballSpeedVertical"])

                # print(ball["ballSpeedVertical"])

        else:
            ball["ballSpeedVertical"] += gravity
    
        if (ball["x"] + ball["diameter"] + ball["ballSpeedHorizontal"] > winWidth
            or ball["x"] + ball["ballSpeedHorizontal"] < 0):

            ball["ballSpeedHorizontal"] = -ball["ballSpeedHorizontal"] * friction

            playBounce(ball["ballSpeedHorizontal"])

        ball["y"] += ball["ballSpeedVertical"] * dt

        ball["x"] += ball["ballSpeedHorizontal"] * dt
    


def drawBall():
    temp = pygame.Surface(ball["img"].get_rect().size, pygame.SRCALPHA)
    temp.blit(ball["img"], (0, 0))
    temp.convert_alpha()

    window.blit(temp,( ball["x"], ball["y"]))


def updateTrail():
     if  (
            ball["x"]!=ball["oldX"] or ball["y"]!=ball["oldY"]
            and
            ball["x"] > ball["oldX"] or ball["x"] < ball["oldX"]
            or
            ball["y"] > ball["oldY"] or ball["y"] < ball["oldY"]
        ):
            newTrailBall = trailBall(ball["x"], ball["y"])
            trailBallArr.append(newTrailBall)
            # newTrailBall.update()
            # print("newBall")
def drawTrail():
    for val in reversed(trailBallArr):
        # print(val)
        if(val.currentIteration <= val.iterations):
            val.update()
            val.currentIteration += 1
        else:
            trailBallArr.remove(val)



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
        print("rel-x: " + str(mouse["relX"]) + " rel-y: " + str(mouse["relY"]) +  " pygame mouse rel: " + str(pygame.mouse.get_rel()))
        ball["ballGrab"] = False
        ball["mouseButton"] = False
        if(ball["mouseButton"] == False):

            ball["ballSpeedVertical"] = mouse["relY"] * 0.08
            ball["ballSpeedHorizontal"] = mouse["relX"] * 0.08

            bounce.play()


        if ball["x"] <= 0:
            ball["ballSpeedHorizontal"] = 0
            ball["ballSpeedVertical"] = 0
        elif ball["x"] + ball["diameter"] >= winWidth:
            ball["ballSpeedHorizontal"] = 0
            ball["ballSpeedVertical"] = 0
        if ball["y"] <= 0:
            ball["ballSpeedVertical"] = 0
        elif ball["y"] + ball["diameter"] >= winHeight:
            ball["ballSpeedVertical"] = 0



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

        updateBall(dt)

        updateTrail()
        
	#Draw stuff
        window.fill(black)    

        drawBall()

        drawTrail()

        pygame.display.update()
        dt = clock.tick()

# initialise
core()
