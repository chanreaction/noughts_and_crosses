#replicate nought and crosses using input method on Python
#Print out board
#Record locations of grid from 1-9, left to right then top-down
# "-------------", 
# "| 1 | 2 | 3 |", 
# "|---|---|---|", 
# "| 4 | 5 | 6 |", 
# "|---|---|---|", 
# "| 7 | 8 | 9 |", 
# "-------------"
#Track turn order by iterating turn variable, player 1 for odd turns, player 2 for even
#Accept input of numbers from 1-9 from player 1, place "O" in appropriate grid, print new board
#Accept input of numbers from 1-9 from player 2, place "X" in appropriate grid, print new board
#... repeat until one player has 3 in a row OR all 9 grids are filled
#WIN CONDITIONS
# 0=1=2
# 3=4=5
#6=7=8
#0=3=6
# 1=4=7
# 2=5=8
# 2=4=6
# 0=4=8



turn = 1
# # grid_occupied = []

board = ["_" for num in range(1, 10)]
print(board)



while turn <=9:
    if turn % 2 == 1:
        move = int(input("Player 1 move "))
        if move > 9 or type(move) != int or board[move-1] == "_": #need to separate out test conditions
            board[move-1] = "O"
            for i in [board[c:c+3] for c in range(0,len(board),3) if c%3 == 0]:
                print(*i)
            if board[0]==board[1]==board[2] and board[0] != "_" or board[3]==board[4]==board[5] and board[3] != "_" or board[6]==board[7]==board[8] and board[6] != "_" or board[0]==board[3]==board[6] and board[0] != "_" or board[1]==board[4]==board[7] and board[1] != "_" or board[2]==board[5]==board[8] and board[2] != "_" or board[2]==board[4]==board[6] and board[2] != "_" or board[0]==board[4]==board[8] and board[0] != "_":
                print("PLAYER 1 WINS!!!!!")
                break
            else:
                turn += 1
        else:
            print("Move is invalid, make another selection")
    else:
        move = int(input("Player 2 move "))
        if board[move-1] == "_" or move > 9 or type(move) != int:
            board[move-1] = "X"
            for i in [board[c:c+3] for c in range(0,len(board),3) if c%3 == 0]:
                print(*i)
            if board[0]==board[1]==board[2] and board[0] != "_" or board[3]==board[4]==board[5] and board[3] != "_" or board[6]==board[7]==board[8] and board[6] != "_" or board[0]==board[3]==board[6] and board[0] != "_" or board[1]==board[4]==board[7] and board[1] != "_" or board[2]==board[5]==board[8] and board[2] != "_" or board[2]==board[4]==board[6] and board[2] != "_" or board[0]==board[4]==board[8] and board[0] != "_":
                print("PLAYER 2 WINS!!!!!")
                break
            else:
                turn += 1
        else:
            print("Move is invalid, make another selection")
if turn == 10:
    print("OUTCOME IS A DRAW")
#print(board)
