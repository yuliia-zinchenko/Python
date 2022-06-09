from random import randint

play_board = '--------------------'
print('Playing board:')
print(play_board)

position_1 = 0
position_2 = 0
mark_1 = 0
mark_2 = 0
congrats = 0


def results(board):
    global congrats
    global mark_1
    global play_board
    while True:
        if 'xxx' in play_board:
            if mark_1 == 'x':
                congrats = 'You win!'
                return(congrats)
            else:
                congrats = 'Computer win'
                return (congrats)
            break
        elif 'ooo' in play_board:
            if mark_1 == 'o':
                congrats = 'You win!'
                return (congrats)
            else:
                congrats = 'Computer win'
                return (congrats)
            break

        elif '-' not in play_board and 'ooo' not in play_board and 'xxx' not in play_board:
            congrats = 'No free space, draw'
            return (congrats)
            break
        elif '-' in play_board and 'ooo' not in play_board and 'xxx':
            return ('Your turn')


def player_move(position):
    global play_board
    global position_1
    global position_2
    while True:
        position_1 = int(input('Choose your position: '))
        if position_1 > 0 and position_1 <= 20:
            break
        if play_board[position_1 - 1] == '-':
            break
        elif play_board[position_1 - 1] != 'x' or play_board[position_1 - 1] != 'o':
            break
        else:
            print('Wrong value, try again')
    play_board = play_board[:position_1 - 1] + mark_1 + play_board[position_1:]
    return play_board

def computer_move(position):
    global play_board
    global position_1
    global position_2
    while True:
        position_2 = randint(1, 21)
        if play_board[position_2 - 1] == '-':
            break
    print('Computer move: ')
    play_board = play_board[:position_2 - 1] + mark_2 + play_board[position_2:]
    return play_board


while True:
    mark_1 = input('Please, choose your mark (x or o): ')
    if mark_1 == 'x' or mark_1 == 'o':
        print(f'You are playing with {mark_1}')
        break

if mark_1 == "x":
    mark_2 = 'o'
else:
    mark_2 = 'x'

while True:
    move_1 = player_move(position_1)
    print(move_1)
    move_2 = computer_move(position_2)
    print(move_2)
    game_results = results(play_board)
    print(game_results)
    if congrats == 'You win!' or congrats == 'Computer win' or congrats == 'No free space, draw':
        break








