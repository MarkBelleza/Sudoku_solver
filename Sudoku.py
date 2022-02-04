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

def printBrd(brd):
  for i in range(len(board)): #row 
    if i % 3 == 0 and i != 0:
      print("- - - - - - - - - - - ")
    for j in range(len(board[0])): #column
      if j % 3 == 0 and j != 0:
        print("| ", end = '')
      print(str(board[i][j]) + " ", end='')
    print('')
#printBrd fucntion ends here

def check(ans, pos, newBrd):
#pos = [row, col]
  
  #Check condition for row
  for i in range(len(newBrd[0])):
    if newBrd[pos[0]][i] == ans and pos[1] != i:
      return False
  
  #Check condition for column
  for j in range(len(newBrd)):
    if newBrd[j][pos[1]] == ans and pos[0] != j:
      return False

  #Check condition for each sub squares
  sqrRow = pos[0] // 3
  sqrCol = pos[1] // 3
  for i in range(sqrRow * 3, (sqrRow * 3) + 3):
    for j in range(sqrCol * 3, (sqrCol * 3) + 3):
      if newBrd[i][j] == ans and i != pos[0] and j != pos[1]:
        return False

  return True
#check function ends here

def solve(brd):
  #look for zeros
  pos = []
  for i in range(len(brd)):
    for j in range(len(brd[0])):
      if brd[i][j] == 0:
        pos = [i, j]
   #--------------------------

  #End case
  if not pos: #if board has no 0 (board is done)
    return True 

  #Base case
  for i in range(1, 10):
    if check(i, pos, brd):
      brd[pos[0]][pos[1]] = i
      if solve(brd):
        return True
      else:
        brd[pos[0]][pos[1]] = 0
  return False
#Solve funtion end

print("Before *")
printBrd(board)
print("-- -- -- -- -- -- -- -- -- -- -- --")
print("After *")
solve(board)
printBrd(board)