import pygame
import sys

# This is going to be a pygame. 

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Project")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)
text = font.render('Hello, Pygame!', True, (0, 0, 0))
text_rect = text.get_rect(center=(400, 300))
background_color = (255, 255, 255)
text_color = (255, 255, 255)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(background_color)
    screen.blit(text, text_rect)
    pygame.display.flip()
    clock.tick(60)

# The window will display a simple message and handle quitting properly.
# It will also maintain a consistent frame rate of 60 FPS.
