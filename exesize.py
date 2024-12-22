#tic tac toe
# b= [0]*9
# def board():
b = [i for i in range(0,9)]
print(b)
turns = 0 # count turns to stop after tie
playerx = True # too change the turn to 'X' again after the loop
win_condition = [[b[0],b[1],b[2]], # posbilites for win
                 [b[3],b[4],b[5]],
                 [b[6],b[7],b[8]],
                  [b[0],b[4],b[8]],
                 [b[2],b[4],b[6]]]


while turns < len(b):
    print(b[0:3]) #prints the board with the actuals places
    print(b[3:6])
    print(b[6:9])

    if playerx: # now player 'X'
        print("'X' - turn")

    else:
        print("'O' - turn")

    a = int(input("insert your play in board: "))
    b[a] = "X" if playerx else "O"


    player_mark = "X" if playerx else "O"
    for condition in win_condition:
        if all(b[pos] == player_mark for pos in condition):
            print(f"{player_mark} won!")
        exit()  # Exit the game or break the loop

    playerx = not playerx

    turns += 1
