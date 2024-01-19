import pygame

pygame.init()
#setup
WIDTH = 675
HIGHT = 600
screen = pygame.display.set_mode([WIDTH, HIGHT])
pygame.display.set_caption('Edge Mogger')
timer = pygame.time.Clock()
fps = 60

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

white_king = pygame.image.load('assets\img\Chess_klt60.png')
white_king = pygame.transform.scale(white_king, (80, 80))
white_queen = pygame.image.load('assets\img\Chess_qlt60.png')
white_queen = pygame.transform.scale(white_queen, (80, 80))
white_bishop = pygame.image.load('assets\img\Chess_blt60.png')
white_bishop = pygame.transform.scale(white_bishop, (80, 80))
white_horse = pygame.image.load('assets\img\Chess_nlt60.png')
white_horse = pygame.transform.scale(white_horse, (80, 80))
white_rook = pygame.image.load('assets\img\Chess_rlt60.png')
white_rook = pygame.transform.scale(white_rook, (80, 80))
white_pawn = pygame.image.load('assets\img\Chess_plt60.png')
white_pawn = pygame.transform.scale(white_pawn, (65, 65))

black_king = pygame.image.load('assets\img\Chess_kdt60.png')
black_king = pygame.transform.scale(black_king, (80, 80))
black_queen = pygame.image.load('assets\img\Chess_qdt60.png')
black_queen = pygame.transform.scale(black_queen, (80, 80))
black_bishop = pygame.image.load('assets\img\Chess_bdt60.png')
black_bishop = pygame.transform.scale(black_bishop, (80, 80))
black_horse = pygame.image.load('assets\img\Chess_ndt60.png')
black_horse = pygame.transform.scale(black_horse, (80, 80))
black_rook = pygame.image.load('assets\img\Chess_rdt60.png')
black_rook = pygame.transform.scale(black_rook, (80, 80))
black_pawn = pygame.image.load('assets\img\Chess_pdt60.png')
black_pawn = pygame.transform.scale(black_pawn, (65, 65))

white_images = [white_pawn, white_queen, white_king, white_horse, white_rook, white_bishop]
black_images = [black_pawn, black_queen, black_king, black_horse, black_rook, black_bishop]
piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, 'light gray', [525 - (column * 150), row * 75, 75, 75])
        else:
            pygame.draw.rect(screen, 'light gray', [600 - (column * 150), row * 75, 75, 75])

#game
run = True
while run:
    timer.tick(fps)
    screen.fill('dark green')
    draw_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()
pygame.quit()
