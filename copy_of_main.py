import pygame
from constants import *
pygame.init()

def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, 'light gray', [450 - (column * 150), row * 75, 75, 75])
        else:
            pygame.draw.rect(screen, 'light gray', [525 - (column * 150), row * 75, 75, 75])
        pygame.draw.rect(screen, (56, 56, 56), [600, 0, 200, HIGHT])
        pygame.draw.rect(screen, (125, 125, 125), [600, 0, 200, HIGHT], 5)
        status_text = ['Select a Piece to Move.', 'Select a Destination.', 'Select a Piece to Move.', 'Select a Destination.']
        screen.blit(font.render(status_text[turn_step], True, 'white'), (610, 40))
        color_select = ['White:', 'White:', 'Black:', 'Black:']
        screen.blit(big_font.render(color_select[turn_step], True, 'white'), (610, 10))
    screen.blit(big_font.render('FORFEIT', True, 'white'), (660, 570))

def draw_pices():
    for i in range(len(white)):
        index = piece_list.index(white[i])
        screen.blit(white_images[index], (location_white[i][0] * 75, location_white[i][1] * 75))

        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, 'red', [location_white[i][0] * 75, location_white[i][1] * 75, 75, 75], 2)

    for i in range(len(black)):
        index = piece_list.index(black[i])
        screen.blit(black_images[index], (location_black[i][0] * 75, location_black[i][1] * 75))

        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'red', [location_black[i][0] * 75, location_black[i][1] * 75, 75, 75], 2)

def check_options(peices, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range(len(peices)):
        location = locations[i]
        peice = peices[i]
        if peice == 'pawn':
            moves_list = check_pawn(location, turn)
        elif peice == 'rook':
            moves_list = check_rook(location, turn)
        elif peice == 'horse':
            moves_list = check_horse(location, turn)
        elif peice == 'bishop':
            moves_list = check_bishop(location, turn)
        elif peice == 'king':
            moves_list = check_king(location, turn)
        elif peice == 'queen':
            moves_list = check_queen(location, turn)
        all_moves_list.append(moves_list)

    return all_moves_list

def check_king(position, color):
    moves_list = []
    if color == 'white':
        enemies = location_black
        friends = location_white
    else:
        enemies = location_white
        friends = location_black

    targets = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)] #up, ner, höger, vänster, up-right, up-left, down-right, down-left
    for i in range(8): 
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append((target[0], target[1]))
    

    return moves_list

def check_queen(position, color):
    moves_list = []
    moves_list = check_bishop(position, color)
    second_list = check_rook(position, color)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    return moves_list

def check_horse(position, color):
    moves_list = []
    if color == 'white':
        enemies = location_black
        friends = location_white
    else:
        enemies = location_white
        friends = location_black

    targets = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):  # 8 squares to check for knights, they can go two squares in one direction and one in another
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append((target[0], target[1]))

    return moves_list

def check_bishop(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = location_black
        friends_list = location_white
    else:
        friends_list = location_black
        enemies_list = location_white
    for i in range(4):  # up-right, up-left, down-right, down-left
        path = True
        chain = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list

def check_rook(position, color):
    moves_list = []
    if color == 'white':
        enemies = location_black
        friends = location_white
    else:
        enemies = location_white
        friends = location_black

    for i in range(4): #ner, up, höger, vänster
        path = True
        chain = 1

        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends and 0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list

def check_pawn(position, color):
    moves_list = []
    if color == 'white':
        if  (position[0], position[1] + 1) not in location_white and (position[0], position[1] + 1) not in location_black and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
            if  (position[0], position[1] + 2) not in location_white and (position[0], position[1] + 2) not in location_black and position[1] == 1:
                moves_list.append((position[0], position[1] + 2))
        if (position[0] + 1, position[1] + 1) in location_black:
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) in location_black:
            moves_list.append((position[0] - 1, position[1] + 1))
#checking for en pessant
        if (position[0] + 1, position[1] + 1) == black_ep:
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) == black_ep:
            moves_list.append((position[0] - 1, position[1] + 1))
    else:
        if  (position[0], position[1] - 1) not in location_white and (position[0], position[1] - 1) not in location_black and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
            if  (position[0], position[1] - 2) not in location_white and (position[0], position[1] - 2) not in location_black and position[1] == 6:
                moves_list.append((position[0], position[1] - 2))
        if (position[0] + 1, position[1] - 1) in location_white:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in location_white:
            moves_list.append((position[0] - 1, position[1] - 1))
#checking for en pessant
        if (position[0] + 1, position[1] - 1) == white_ep:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) == white_ep:
            moves_list.append((position[0] - 1, position[1] - 1))
    return moves_list
    
def check_valid_moves():
    if turn_step < 2:
        opptions_list = white_options
    else:
        opptions_list = black_options
    valid_options = opptions_list[selection]
    return valid_options

def draw_dots(moves):
    color = 'red'
    for i in range(len(moves)):
        pygame.draw.circle(screen, color, (moves[i][0] * 75 + 38, moves[i][1] * 75 + 38), 5)

def draw_captured():
    for i in range(len(captured_pieces_white)):
        captured_piece = captured_pieces_white[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_black_images[index], (620, (55 + 30*i)))

    for i in range(len(captured_pieces_black)):
        captured_piece = captured_pieces_black[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_white_images[index], (660, (55 + 30*i)))

def draw_check():
    checked = False
    if turn_step < 2:
        if 'king' in white:
            king_index = white.index('king')
            king_location = location_white[king_index]
            for i in range(len(black_options)):
                if king_location in black_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark red', [location_white[king_index][0] * 75, location_white[king_index][1] * 75, 75, 75], 5)
    else:
        if 'king' in black:
            king_index = black.index('king')
            king_location = location_black[king_index]
            for i in range(len(white_options)):
                if king_location in white_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark red', [location_black[king_index][0] * 75, location_black[king_index][1] * 75, 75, 75], 5)

def draw_game_over():
    pygame.draw.rect(screen, 'black', [200, 200, 400, 100])
    screen.blit(font.render(f'{winner} won the game!', True, 'white'), (210, 210))
    screen.blit(font.render(f'Press ENTER to Restart', True, 'white'), (210, 240))

def check_ep(old_cords, new_cords):
    if turn_step <= 1:
        index = location_white.index(old_cords)
        ep_coords = (new_cords[0], new_cords[1] - 1)
        piece = white[index]
    else:
        index = location_black.index(old_cords)
        ep_coords = (new_cords[0], new_cords[1] + 1)
        piece = black[index]
    if piece == 'pawn' and abs(old_cords[1] - new_cords[1]) > 1:
        pass
    else:
        ep_coords = (100, 100)
    return ep_coords

#game
black_options = check_options(black, location_black, 'black')
white_options = check_options(white, location_white, 'white')
run = True
while run:
    timer.tick(fps)
    if counter < 30:
        counter += 1
    else:
        counter = 0
    screen.fill((74, 122, 64))
    draw_board()
    draw_pices()
    draw_captured()
    draw_check()
    if selection != 100:
        valid_moves = check_valid_moves()
        draw_dots(valid_moves)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            x_coord = event.pos[0] // 75
            y_coord = event.pos[1] // 75
            click_coords =(x_coord, y_coord)
            if turn_step <= 1:
                if click_coords == (8, 7) or click_coords == (10, 7) or click_coords == (9, 7):
                    winner = 'Black'

                if click_coords in location_white:
                    selection = location_white.index(click_coords)

                    if turn_step == 0:
                        turn_step = 1

                if click_coords in valid_moves and selection != 100:
                    white_ep = check_ep(location_white[selection], click_coords)
                    location_white[selection] = click_coords
#capturing of pieces for white
                    if click_coords in location_black:
                        black_piece = location_black.index(click_coords)
                        captured_pieces_white.append(black[black_piece])
#if king is captured you win
                        if black[black_piece] == 'king':
                            winner = 'White'

                        black.pop(black_piece)
                        location_black.pop(black_piece)
# En passant capture
                    if click_coords == black_ep:
                        black_piece = location_black.index((black_ep[0], black_ep[1] - 1))
                        captured_pieces_white.append(black[black_piece])

                        black.pop(black_piece)
                        location_black.pop(black_piece)

                    black_options = check_options(black, location_black, 'black')
                    white_options = check_options(white, location_white, 'white')
                    turn_step = 2
                    selection = 100
                    valid_moves = []

            if turn_step > 1:
                if click_coords == (8, 7) or click_coords == (10, 7) or click_coords == (9, 7):
                    winner = 'White'

                if click_coords in location_black:
                    selection = location_black.index(click_coords)
                    if turn_step == 2:
                        turn_step = 3

                if click_coords in valid_moves and selection != 100:
                    black_ep = check_ep(location_black[selection], click_coords)
                    location_black[selection] = click_coords
#capturing of pieces for black
                    if click_coords in location_white:
                        white_piece = location_white.index(click_coords)
                        captured_pieces_black.append(white[white_piece])
#if king is captured you win
                        if white[white_piece] == 'king':
                            winner = 'Black'

                        white.pop(white_piece)
                        location_white.pop(white_piece)
# en pessant capture
                    if click_coords == white_ep:
                        white_piece = location_white.index((white_ep[0], white_ep[1] + 1))
                        captured_pieces_black.append(white[white_piece])

                        white.pop(white_piece)
                        location_white.pop(white_piece)

                    black_options = check_options(black, location_black, 'black')
                    white_options = check_options(white, location_white, 'white')
                    turn_step = 0
                    selection = 100
                    valid_moves = []
        
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_RETURN:
                game_over = False
                white = ['rook', 'horse', 'bishop', 'king', 'queen', 'bishop', 'horse', 'rook',
                        'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                location_white = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]

                black = ['rook', 'horse', 'bishop', 'king', 'queen', 'bishop', 'horse', 'rook',
                        'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                location_black = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                captured_pieces_white = []
                captured_pieces_black = []

                turn_step = 0
                selection = 100
                valid_moves = []
                winner = ''

                black_options = check_options(black, location_black, 'black')
                white_options = check_options(white, location_white, 'white')

    if winner != '':
        game_over = True
        draw_game_over()
    pygame.display.flip()
pygame.quit()
