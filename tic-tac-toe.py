
# prepare_board
# X player, play
# input location - valid: 1) 1-3/1-3 2). free place
# put X in the board
# draw the board
# check if won
# board is full == tie
# O player, play
# X player, play
# input location - valid: 1) 1-3/1-3 2). free place
# put X in the board
# draw the board
# check if won

def create_game() -> dict:
    return {
        'board': [
            ['_', '_', '_'],
            ['_', '_', '_'],
            ['_', '_', '_'],
        ], # could be better board[1, 1]
        'turn': 'X',
        'counter': 1
    }

def draw_board(game):
    print("  0 1 2")
    counter = 0
    for row in game['board']:
        print(counter, ' '.join(row))
        counter += 1
    print()

def input_square(game, x_or_o):
    input(f'Enter location for {x_or_o}: ')

def check_win(game, x_o: str) -> bool:
    pass

def check_tie(game) -> bool:
    return game['counter'] >= 9

def play_x_o():
    # prepare_game
    my_game = create_game()

    # prepare_board ?

    # while board_is_not_full and there_is_no_win:
    while True:
        #   X player, play
        #   input location - valid: 1. range 1-3/1-3 2. free cell
        draw_board(my_game)
        x_play = input_square(my_game, 'X')
        my_game['board'][x_play] = 'X'
        my_game['counter'] += 1

        #   check if won ?
        if check_win(my_game, 'X'):
            break

        #   board is full (counter == 9), tie
        if check_tie(my_game):
            break

        #   O player, play
        #   input location - valid: 1. range 1-3/1-3 2. free cell
        draw_board(my_game)
        o_play = input_square(my_game, 'O')
        my_game['board'][o_play] = 'O'
        my_game['counter'] += 1

        #   check if won ?
        if check_win(my_game, 'O'):
            break
print()