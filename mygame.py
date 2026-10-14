import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game")

clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

screen.fill((75, 90, 81))

pygame.display.flip()

clock.tick(60)

pygame.quit()
sys.exit()
