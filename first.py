import pygame
pygame.init()

windowWidth = 500
windowHeight = 500
GameWindow = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Snake Game!")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

print("hello")