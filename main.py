import pygame
import random

pygame.init()  # initializes the pygame module
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

width = robot.get_width()
height = robot.get_height()


x, y = 0, 0
velocity = 1
clock = pygame.time.Clock()
window.fill((0, 0, 0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.blit(robot, (x, y))
    pygame.display.flip()  # updates the contents of the window

    x += velocity
    if velocity > 0 and x+robot.get_width() >= 640:
        velocity = -velocity
    if velocity < 0 and x <= 0:
        velocity = -velocity

    clock.tick(240) # the loop should be executed 60 times a second
