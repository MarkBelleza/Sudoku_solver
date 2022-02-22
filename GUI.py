from lib2to3.pgen2 import pgen
from multiprocessing.connection import wait
from operator import truediv
from os import system
import pygame

#Initial the pygame
pygame.init()

#Change Title
pygame.display.set_caption("Sudoku Solver")
#Change Icon
icon = pygame.image.load('sudoku.png')
pygame.display.set_icon(icon)

font = pygame.font.Font('freesansbold.ttf',80)

#Create the GUI 
screen = pygame.display.set_mode((900, 900)) #(widht, height)


board = [
    [0,0,0,0,4,8,0,7,2],
    [9,6,0,0,7,0,8,0,0],
    [7,0,0,6,3,1,0,0,0],
    [0,9,6,3,0,0,0,1,5],
    [5,0,8,4,9,0,0,0,0],
    [0,0,0,0,0,0,0,2,8],
    [6,0,9,8,2,3,1,5,0],
    [0,0,1,7,0,4,0,0,6],
    [3,7,0,0,0,0,2,8,0]
]

def check(ans, x, y, newBrd):
# x = row number
# y = column number
  #Check condition for row
  for i in range(len(newBrd[0])):
    if newBrd[x][i] == ans and y != i:
      return False
  
  #Check condition for column
  for j in range(len(newBrd)):
    if newBrd[j][y] == ans and x != j:
      return False

  #Check condition for each sub squares
  sqrRow = x // 3
  sqrCol = y // 3
  for i in range(sqrRow * 3, (sqrRow * 3) + 3):
    for j in range(sqrCol * 3, (sqrCol * 3) + 3):
      if newBrd[i][j] == ans and i != x and j != y:
        return False
  return True
#check function end---*

def solve(brd):
  for i in range(len(brd)):
    for j in range(len(brd[0])):
      if brd[i][j] == 0:
        for s in range(1, 10): #iterate through possible numbers
          if check(s, i, j, brd):
            brd[i][j] = s
            if solve(brd): #checks the next
              return True
            else: brd[i][j] = 0 #goes back to for loop and finds another possible number
        return False #if no possible possible number found, backtrack!
  else: return True #if board has no 0 (board is done)
#solve funtion end---*

def board_numbers():
    pygame.time.delay(500)
    for row in range(9):
        for col in range(9):
            output = board[row][col]
            if (output == 0):
              n_text = font.render(str(output), True, (255,0,0))
            else:
              n_text = font.render(str(output), True, (0,0,0))
            screen.blit(n_text, pygame.Vector2((col * 99) + 30, (row * 99) + 20))

def draw_grid():
    screen.fill((255,255,255)) #RGB colour
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(5, 5, 890, 890), 5) #drawing param. = (screen, colour, coordinates, width of line)

    off_set = 99
    #Draw the lines
    for i in range(9):
        if (i == 3) | (i == 6):
            pygame.draw.line(screen, (0,0,0), pygame.Vector2((i * off_set) + 5, 5), pygame.Vector2((i * off_set) + 5, 890), 10) #colomns 
            pygame.draw.line(screen, (0,0,0), pygame.Vector2(5, (i * off_set) + 5), pygame.Vector2(890, (i * off_set) + 5), 10) #rows
        else:
            pygame.draw.line(screen, (0,0,0), pygame.Vector2((i * off_set) + 5, 5), pygame.Vector2((i * off_set) + 5, 890), 5) #colomns 
            pygame.draw.line(screen, (0,0,0), pygame.Vector2(5, (i * off_set) + 5), pygame.Vector2(890, (i * off_set) + 5), 5) #rows


#Keep the GUI running
draw_grid()
board_numbers()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            system.exit()
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_BACKSPACE:
            solve(board)
            draw_grid()
            board_numbers()            
    pygame.display.update()



    




# def board_numbers():
#    row = 0
#    while row < 9:
#        col = 0
#        while col < 9:
#            output = board[row][col]
#            n_text = font.render(str(output), True, (0,0,0))
#            screen.blit(n_text, pygame.Vector2((col * 99) + 30, (row * 99) + 10))
#            col += 1
#        row += 1