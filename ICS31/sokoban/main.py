from ICS31.sokoban.game_settings import *
partner1_uci_email_id = "jieul17@uci.edu" # both partner's email IDs must be on each submission
partner2_uci_email_id = "eunbis@uci.edu" # both partner's email IDs must be on each submission

import copy

board_copy = copy.deepcopy(board)
def print_board():
    for i in board:
        for j in range(len(i)):
            if j == len(i) - 1:
                print(i[j])
            else:
                print(i[j],end = ' ')
    print()

def print_board_copy():
    for i in board_copy:
        for j in range(len(i)):
            if j == len(i) - 1:
                print(i[j])
            else:
                print(i[j],end = ' ')

def gameover():
    for i in board_copy:
        if TARGET in i:
            status = False
            break
        else:
            status = True
    return status
print_board_copy()
print()
user_input = input()

#w - move the sprite up
#s - move the sprite down
#a - move the sprite left
#d - move the sprite right
#q - quit the game
#space - reset the board

while user_input != QUIT:
    position = []
    for i in range(1,len(board_copy)-1):
        #if user_input == 's' and i == len(board_copy)-2:
        #     continue
        for j in range(1,len(board_copy[i])-1):
            if board_copy[i][j] == SPRITE or board_copy[i][j] == SPRITE_T:
                first_index = i
                second_index = j
                current = board_copy[first_index][second_index]
                position.append((first_index,second_index))

    if user_input == CONTROLS[1]: #left
        next_position_1 = board_copy[first_index][second_index - 1]
        next_position_2 = board_copy[first_index][second_index - 2]
        position.append((first_index,second_index-1))
        position.append((first_index,second_index-2))
    elif user_input == CONTROLS[3]: #right
        next_position_1 = board_copy[first_index][second_index + 1]
        next_position_2 = board_copy[first_index][second_index + 2]
        position.append((first_index, second_index + 1))
        position.append((first_index, second_index + 2))
    elif user_input == CONTROLS[0]: #up
        next_position_1 = board_copy[first_index-1][second_index]
        next_position_2 = board_copy[first_index-2][second_index]
        position.append((first_index-1, second_index))
        position.append((first_index-2, second_index))
    elif user_input == CONTROLS[2]: #down
        if first_index == len(board_copy)-2:
            next_position_1 = '+'
            next_position_2 = '+'
        else:
            next_position_1 = board_copy[first_index + 1][second_index]
            next_position_2 = board_copy[first_index + 2][second_index]
            position.append((first_index + 1, second_index))
            position.append((first_index + 2, second_index))
    elif user_input == CONTROLS[4]:
        print_board()
        board_copy = copy.deepcopy(board)
        user_input = input()
        continue
    else:
        user_input = input('enter a valid move:\n')
        continue

    if not (next_position_1 == WALL or (next_position_1 == BOX_NS and (next_position_2 == BOX_NS or next_position_2 == WALL or next_position_2 == BOX_S))):
        # FIXME
        if board_copy[position[0][0]][position[0][1]] == SPRITE:
            board_copy[position[0][0]][position[0][1]] = EMPTY
        elif board_copy[position[0][0]][position[0][1]] == SPRITE_T:
            board_copy[position[0][0]][position[0][1]] = TARGET
        if next_position_1 == EMPTY:
            #current = ' '
            #next_position_1 = 'i'
            board_copy[position[1][0]][position[1][1]] = SPRITE
        elif next_position_1 == BOX_NS:
            #current = ' '
            #next_position_1 = 'i'
            #next_position_2 = '!'
            board_copy[position[1][0]][position[1][1]] = SPRITE
            board_copy[position[2][0]][position[2][1]] = BOX_NS
            if next_position_2 == TARGET:
                board_copy[position[1][0]][position[1][1]] = SPRITE
                board_copy[position[2][0]][position[2][1]] = BOX_S
            #elif next_position_2 == '.':
            #    continue
        elif next_position_1 == TARGET:
                #current = ' '
                #next_position_1 = 'I'
                board_copy[position[1][0]][position[1][1]] = SPRITE_T
        elif next_position_1 == BOX_S:
            if next_position_2 == BOX_NS:
                continue
            else:
                #current = ' '
                #next_position_1 = 'I'
                #next_position_2 = '!'
                board_copy[position[1][0]][position[1][1]] = SPRITE_T
                board_copy[position[2][0]][position[2][1]] = BOX_NS
        print_board_copy()
        if gameover() == False:
            print()
            user_input = input()
        else:
            print("You Win!")
            break
    else:
        print_board_copy()
        if gameover() == False:
            print()
            user_input = input()
        else:
            print("You Win!")
            break

if user_input == QUIT:
    print("Goodbye")