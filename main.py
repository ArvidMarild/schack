import pygame
from constants import *  # Importing constants from a separate file
pygame.init()

def draw_board():
    # Draw the chessboard grid
    for i in range(32):
        # Calculate the column and row indices for each square
        column = i % 4
        row = i // 4
        
        # Determine the color of the square based on row parity
        if row % 2 == 0:
            # Alternate between light gray and dark gray for even rows
            pygame.draw.rect(screen, 'light gray', [450 - (column * 150), row * 75, 75, 75])
        else:
            # Alternate between light gray and dark gray for odd rows
            pygame.draw.rect(screen, 'light gray', [525 - (column * 150), row * 75, 75, 75])
    
    # Draw the status bar on the right side
    pygame.draw.rect(screen, (56, 56, 56), [600, 0, 200, HIGHT])
    pygame.draw.rect(screen, (125, 125, 125), [600, 0, 200, HIGHT], 5)
    # Define status messages for different turn steps
    status_text = ['Select a Piece to Move.', 'Select a Destination.', 'Select a Piece to Move.', 'Select a Destination.']
    # Display the current status text based on the turn step
    screen.blit(font.render(status_text[turn_step], True, 'white'), (610, 40))
    # Define color indicators for different turn steps
    color_select = ['White:', 'White:', 'Black:', 'Black:']
    # Display the current color selection prompt based on the turn step
    screen.blit(big_font.render(color_select[turn_step], True, 'white'), (610, 10))
    # Display the "FORFEIT" option
    screen.blit(big_font.render('FORFEIT', True, 'white'), (660, 570))


def draw_pieces():
    # Draw all white pieces
    for i in range(len(white)):
        index = piece_list.index(white[i])
        screen.blit(white_images[index], (location_white[i][0] * 75, location_white[i][1] * 75))
        
        # Highlight the selected piece if applicable
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, 'red', [location_white[i][0] * 75, location_white[i][1] * 75, 75, 75], 2)

    # Draw all black pieces
    for i in range(len(black)):
        index = piece_list.index(black[i])
        screen.blit(black_images[index], (location_black[i][0] * 75, location_black[i][1] * 75))
        
        # Highlight the selected piece if applicable
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'red', [location_black[i][0] * 75, location_black[i][1] * 75, 75, 75], 2)

def check_options(pieces, locations, turn):
    # Determine possible moves for each piece
    moves_list = []
    all_moves_list = []
    for i in range(len(pieces)):
        piece = pieces[i]
        location = locations[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'horse':
            moves_list = check_horse(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)
        elif piece == 'king':
            moves_list = check_king(location, turn)
        elif piece == 'queen':
            moves_list = check_queen(location, turn)
        all_moves_list.append(moves_list)

    return all_moves_list

#Functions to check possible moves for each type of piece
#Funktion som ser vart kungen kan gå
def check_king(position, color):
    moves_list = []
    #definera vilka som är sin medspelar och vilka som är fienden (dem som kan bli tagna/inte tagan)
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
    # Initialize the list of possible moves for the queen
    moves_list = []
    # Get the moves for the bishop and rook combined
    moves_list = check_bishop(position, color)
    second_list = check_rook(position, color)
    # Combine the moves from the rook and bishop
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    return moves_list

def check_horse(position, color):
    # Initialize the list of possible moves for the knight
    moves_list = []
    # Determine the locations of friendly and enemy pieces based on color
    if color == 'white':
        enemies = location_black
        friends = location_white
    else:
        enemies = location_white
        friends = location_black

    # Define the possible knight move targets
    targets = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    # Check each target for valid knight moves
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        # Check if the move is valid and not obstructed by friendly pieces
        if target not in friends and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append((target[0], target[1]))
    return moves_list

def check_bishop(position, color):
    # Initialize the list of possible moves for the bishop
    moves_list = []
    # Determine the locations of friendly and enemy pieces based on color
    if color == 'white':
        enemies_list = location_black
        friends_list = location_white
    else:
        friends_list = location_black
        enemies_list = location_white
    # Check diagonals for valid bishop moves
    for i in range(4):
        path = True
        chain = 1
        # Define the direction of the diagonal
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
        # Check each diagonal path
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                # Stop if an enemy piece is encountered
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list

def check_rook(position, color):
    # Initialize the list of possible moves for the rook
    moves_list = []
    # Determine the locations of friendly and enemy pieces based on color
    if color == 'white':
        enemies = location_black
        friends = location_white
    else:
        enemies = location_white
        friends = location_black

    # Check four cardinal directions for valid rook moves
    for i in range(4):
        path = True
        chain = 1
        # Define the direction of the cardinal direction
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
        # Check each path
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends and 0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                # Stop if an enemy piece is encountered
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list

def check_pawn(position, color):
    # Initialize the list of possible moves for the pawn
    moves_list = []
    # Determine the locations of friendly and enemy pieces based on color
    if color == 'white':
        # Check forward moves for white pawns
        if  (position[0], position[1] + 1) not in location_white and (position[0], position[1] + 1) not in location_black and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
            # Allow double move from starting position
            if  (position[0], position[1] + 2) not in location_white and (position[0], position[1] + 2) not in location_black and position[1] == 1:
                moves_list.append((position[0], position[1] + 2))
        # Check diagonal captures for white pawns
        if (position[0] + 1, position[1] + 1) in location_black:
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) in location_black:
            moves_list.append((position[0] - 1, position[1] + 1))
        # Check for en passant moves
        if (position[0] + 1, position[1] + 1) == black_ep:
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) == black_ep:
            moves_list.append((position[0] - 1, position[1] + 1))
    else:
        # Check forward moves for black pawns
        if  (position[0], position[1] - 1) not in location_white and (position[0], position[1] - 1) not in location_black and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
            # Allow double move from starting position
            if  (position[0], position[1] - 2) not in location_white and (position[0], position[1] - 2) not in location_black and position[1] == 6:
                moves_list.append((position[0], position[1] - 2))
        # Check diagonal captures for black pawns
        if (position[0] + 1, position[1] - 1) in location_white:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in location_white:
            moves_list.append((position[0] - 1, position[1] - 1))
        # Check for en passant moves
        if (position[0] + 1, position[1] - 1) == white_ep:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) == white_ep:
            moves_list.append((position[0] - 1, position[1] - 1))
    return moves_list

def check_valid_moves():
    # Check valid moves for the selected piece
    if turn_step < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options

def draw_dots(moves):
    # Draw dots to indicate valid moves
    color = 'red'
    for i in range(len(moves)):
        pygame.draw.circle(screen, color, (moves[i][0] * 75 + 38, moves[i][1] * 75 + 38), 5)

def draw_captured():
    # Draw captured pieces on the side
    for i in range(len(captured_pieces_white)):
        captured_piece = captured_pieces_white[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_black_images[index], (620, (55 + 30*i)))

    for i in range(len(captured_pieces_black)):
        captured_piece = captured_pieces_black[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_white_images[index], (660, (55 + 30*i)))

def draw_check():
    # Draw a red border around the king if in check
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
    # Draw the game over message
    pygame.draw.rect(screen, 'black', [200, 200, 400, 100])
    screen.blit(font.render(f'{winner} won the game!', True, 'white'), (210, 210))
    screen.blit(font.render(f'Press ENTER to Restart', True, 'white'), (210, 240))

def check_ep(old_coords, new_coords):
    # Check for en passant moves
    if turn_step <= 1:
        index = location_white.index(old_coords)
        ep_coords = (new_coords[0], new_coords[1] - 1)
        piece = white[index]
    else:
        index = location_black.index(old_coords)
        ep_coords = (new_coords[0], new_coords[1] + 1)
        piece = black[index]
    if piece == 'pawn' and abs(old_coords[1] - new_coords[1]) > 1:
        pass
    else:
        ep_coords = (100, 100)
    return ep_coords

# Main game loop
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
    draw_pieces()
    draw_captured()
    draw_check()
    if selection != 100:
        valid_moves = check_valid_moves()
        draw_dots(valid_moves)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            x_coord = event.pos[0] // 75
            y_coord = event.pos[1] // 75
            click_coords =(x_coord, y_coord)
            if turn_step <= 1:
                # Check if forfeit button is clicked
                if click_coords == (8, 7) or click_coords == (10, 7) or click_coords == (9, 7):
                    winner = 'Black'
                # Handle piece selection for white player
                if click_coords in location_white:
                    selection = location_white.index(click_coords)
                    if turn_step == 0:
                        turn_step = 1
                # Handle piece movement for white player
                if click_coords in valid_moves and selection != 100:
                    white_ep = check_ep(location_white[selection], click_coords)
                    location_white[selection] = click_coords
                    # Capturing of pieces for white
                    if click_coords in location_black:
                        black_piece = location_black.index(click_coords)
                        captured_pieces_white.append(black[black_piece])
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
                # Check if forfeit button is clicked
                if click_coords == (8, 7) or click_coords == (10, 7) or click_coords == (9, 7):
                    winner = 'White'
                # Handle piece selection for black player
                if click_coords in location_black:
                    selection = location_black.index(click_coords)
                    if turn_step == 2:
                        turn_step = 3
                # Handle piece movement for black player
                if click_coords in valid_moves and selection != 100:
                    black_ep = check_ep(location_black[selection], click_coords)
                    location_black[selection] = click_coords
                    # Capturing of pieces for black
                    if click_coords in location_white:
                        white_piece = location_white.index(click_coords)
                        captured_pieces_black.append(white[white_piece])
                        if white[white_piece] == 'king':
                            winner = 'Black'
                        white.pop(white_piece)
                        location_white.pop(white_piece)
                    # En passant capture
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
        # Restart the game if it's over and the user presses ENTER
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_RETURN:
                game_over = False
                # Reset game state variables and board
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

    # Display game over message if a winner is determined
    if winner != '':
        game_over = True
        draw_game_over()
    pygame.display.flip()

# Quit pygame when the game loop ends
pygame.quit()
