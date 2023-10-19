import pygame
import random

pygame.init()   # initializes the pygame module
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

window.fill((0, 0, 0))

width = robot.get_width()
height = robot.get_height()
#window.blit(robot, ((640-width)/2, (480-height)/2))
#window.blit(robot, (0, 0))
#window.blit(robot, (640-width, 0))
#window.blit(robot, (0, 480-height))
#window.blit(robot, (640-width, 480-height))

#Like in the university
for i in range(10):
    for j in range(10):
        window.blit(robot, (42*(2+j) + i*10, 20*(1+i)))
        print(i, " : ", j)

""" random robots
for _ in range(1000):
    rangeOfWidth = random.randint(0, 640 - width)
    rangeOfHeight = random.randint(0, 480 - height)

    window.blit(robot, (rangeOfWidth, rangeOfHeight))
    print(rangeOfWidth)
"""

pygame.display.flip()   # updates the contents of the window

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
