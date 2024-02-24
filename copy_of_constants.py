#i denna fillen är alla kostanter/setup som används i main koden
import pygame
pygame.init()

WIDTH = 800 #sätter brädden på spelet
HIGHT = 600 #sätter höjden på spelet
screen = pygame.display.set_mode([WIDTH, HIGHT])
pygame.display.set_caption('Chess.com')
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 15)
big_font = pygame.font.Font('freesansbold.ttf', 20)

#startpositionerna för vits pjäser
white = ['rook', 'horse', 'bishop', 'king', 'queen', 'bishop', 'horse', 'rook',
         'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
location_white = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]

#för svart
black = ['rook', 'horse', 'bishop', 'king', 'queen', 'bishop', 'horse', 'rook',
         'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
location_black = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
captured_pieces_white = []
captured_pieces_black = []
# 0 - whites turn no selection: 1-whites turn piece selected: 2- black turn no selection, 3 - black turn piece selected
turn_step = 0
color = 0
selection = 100
valid_moves = []

#laddar in bilderna och hur stor bilden ska vara
white_king = pygame.image.load('assets\img\Chess_klt60.png')
white_king = pygame.transform.scale(white_king, (80, 80))
white_king_small = pygame.transform.scale(white_king, (40, 40))
white_queen = pygame.image.load('assets\img\Chess_qlt60.png')
white_queen = pygame.transform.scale(white_queen, (80, 80))
white_queen_small = pygame.transform.scale(white_queen, (40, 40))
white_bishop = pygame.image.load('assets\img\Chess_blt60.png')
white_bishop = pygame.transform.scale(white_bishop, (80, 80))
white_bishop_small = pygame.transform.scale(white_bishop, (40, 40))
white_horse = pygame.image.load('assets\img\Chess_nlt60.png')
white_horse = pygame.transform.scale(white_horse, (80, 80))
white_horse_small = pygame.transform.scale(white_horse, (40, 40))
white_rook = pygame.image.load('assets\img\Chess_rlt60.png')
white_rook = pygame.transform.scale(white_rook, (80, 80))
white_rook_small = pygame.transform.scale(white_rook, (40, 40))
white_pawn = pygame.image.load('assets\img\Chess_plt60.png')
white_pawn = pygame.transform.scale(white_pawn, (65, 65))
white_pawn_small = pygame.transform.scale(white_pawn, (40, 40))

#laddar in bilderna och hur stor bilden ska vara
black_king = pygame.image.load('assets\img\Chess_kdt60.png')
black_king = pygame.transform.scale(black_king, (80, 80))
black_king_small = pygame.transform.scale(black_king, (40, 40))
black_queen = pygame.image.load('assets\img\Chess_qdt60.png')
black_queen = pygame.transform.scale(black_queen, (80, 80))
black_queen_small = pygame.transform.scale(black_queen, (40, 40))
black_bishop = pygame.image.load('assets\img\Chess_bdt60.png')
black_bishop = pygame.transform.scale(black_bishop, (80, 80))
black_bishop_small = pygame.transform.scale(black_bishop, (40, 40))
black_horse = pygame.image.load('assets\img\Chess_ndt60.png')
black_horse = pygame.transform.scale(black_horse, (80, 80))
black_horse_small = pygame.transform.scale(black_horse, (40, 40))
black_rook = pygame.image.load('assets\img\Chess_rdt60.png')
black_rook = pygame.transform.scale(black_rook, (80, 80))
black_rook_small = pygame.transform.scale(black_rook, (40, 40))
black_pawn = pygame.image.load('assets\img\Chess_pdt60.png')
black_pawn = pygame.transform.scale(black_pawn, (65, 65))
black_pawn_small = pygame.transform.scale(black_pawn, (40, 40))

white_images = [white_pawn, white_queen, white_king, white_horse, white_rook, white_bishop]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_horse_small, white_rook_small, white_bishop_small]
black_images = [black_pawn, black_queen, black_king, black_horse, black_rook, black_bishop]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_horse_small, black_rook_small, black_bishop_small]
piece_list = ['pawn', 'queen', 'king', 'horse', 'rook', 'bishop']

counter = 0
winner = ''
game_over = False
white_ep = (100, 100)
black_ep = (100, 100)