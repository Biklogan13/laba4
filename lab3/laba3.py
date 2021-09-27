import pygame
from pygame.draw import *

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()

rect(screen, (143, 198, 246), (0, 0, 1000, 500))
rect(screen, (103, 217, 108), (0, 500, 1000, 500))
ellipse(screen, (185, 155, 191), (220, 350, 150, 300))
circle(screen, (231, 208, 185), (295, 320), 50)
lines(screen, (0, 0, 0), False, ((335, 620), (370, 820), (420, 820)), width=2)
lines(screen, (0, 0, 0), False, ((255, 620), (150, 820), (100, 820)), width=2)
line(screen, (0, 0, 0), (250, 380), (150, 480), width=2)
line(screen, (0, 0, 0), (340, 380), (470, 480), width=2)
polygon(screen, (227, 201, 67), ((160, 480), (110, 460), (165, 420)))
circle(screen, (255, 0, 0), (145, 425), 18)
circle(screen, (95, 0, 0), (120, 445), 18)
circle(screen, (255, 255, 255), (120, 420), 18)
polygon(screen, (255, 95, 177), ((620, 350), (540, 650), (700, 650)))
circle(screen, (231, 208, 185), (620, 320), 50)
lines(screen, (0, 0, 0), False, ((600, 650), (550, 820), (500, 825)), width=2)
lines(screen, (0, 0, 0), False, ((640, 650), (690, 820), (740, 820)), width=2)
line(screen, (0, 0, 0), (605, 410), (470, 480), width=2)
lines(screen, (0, 0, 0), False, ((635, 410), (680, 455), (740, 440)), width=2)
line(screen, (0, 0, 0), (720, 490), (800, 300), width=2)
polygon(screen, (255, 0, 0), ((800, 300), (850, 250), (790, 230)))
circle(screen, (255, 0, 0), (835, 240), 18)
circle(screen, (255, 0, 0), (807, 230), 18)
pygame.display.update()

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()