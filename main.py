import math

import pygame
import random

pygame.init()  # initializes the pygame module
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

width = robot.get_width()
height = robot.get_height()


x, y = 0, 0
angle = 0
clock = pygame.time.Clock()
window.fill((0, 0, 0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    x = math.cos(angle)*100 + 640/2 - robot.get_width()
    y = math.sin(angle)*100 + 320/2

    window.blit(robot, (x, y))
    pygame.display.flip()  # updates the contents of the window

    angle += 0.01
    clock.tick(60) # the loop should be executed 60 times a second

    #Make it up and down aniamtion ..x

