import pygame
import random

pygame.init()  # initializes the pygame module
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

width = robot.get_width()
height = robot.get_height()


x, y = 0, 0
clock = pygame.time.Clock()
window.fill((0, 0, 0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.blit(robot, (x, y))
    pygame.display.flip()  # updates the contents of the window

    x += 1
    clock.tick(60) # the loop should be executed 60 times a second
