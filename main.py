import pygame

pygame.init()   # initializes the pygame module
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

window.fill((0, 0, 0))

width = robot.get_width()
height = robot.get_height()
window.blit(robot, ((640-width)/2, (480-height)/2))
window.blit(robot, (0, 0))
window.blit(robot, (640-width, 0))
window.blit(robot, (0, 480-height))
window.blit(robot, (640-width, 480-height))

pygame.display.flip()   # updates the contents of the window



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
