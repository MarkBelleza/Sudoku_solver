import pygame

#Initial the pygame
pygame.init()

#Create the GUI 
screen = pygame.display.set_mode((900, 700)) #(widht, height)

#Change Title
pygame.display.set_caption("Sudoku Solver")
#Change Icon
icon = pygame.image.load('sudoku.png')
pygame.display.set_icon(icon)

#Keep the GUI running
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255,255,255)) #RGB colour
    pygame.display.update()


font = pygame.font.Font('freesansbold.ttf',32)
