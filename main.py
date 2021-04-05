import pygame
from random import randint as rnd

WIDTH = 800
HEIGHT = 300

window = pygame.display.set_mode((WIDTH, HEIGHT))

lines = [rnd(1, HEIGHT) for _ in range(WIDTH)]

def draw(win, lines):
    win.fill((255,255,255))

    for i, line in enumerate(lines):
        pygame.draw.line(win, (0,0,0), (i, HEIGHT-line), (i, HEIGHT))

while True:

    ### BUBBLE SORT ###

    for i in range(len(lines)-1):
        for j in range(len(lines)-1-i):
            if lines[j] > lines[j+1]:
                lines[j], lines[j+1] = lines[j+1], lines[j]

        draw(window, lines)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    ###################
