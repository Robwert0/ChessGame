import pygame

pygame.init()

WIDTH = 1000
HEIGHT = 900

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Two player Chess')
font = pygame.font.Font('freesansbold.ttf', 20)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
fps = 60

# game variables and images
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
               'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), 
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]

black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
               'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), 
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

captured_pieces_white = []
captured_pieces_black = []

# 0-white turn no selection, 1-white turn piece selection, 2-black turn no selection, 3- black turn piece selection
turn_step = 0
selection = float('inf')
valid_moves = []

# load in game piece images(queen, king, rook, bishop, knight, pawn)
# black pieces
black_queen = pygame.image.load(r'E:\Projects\Chess_game\assets\images\black queen.png')
black_queen = pygame.transform.scale(black_queen, (80, 80))
black_queen_small = pygame.transform.scale(black_queen, (45, 45))
black_bishop = pygame.image.load(r'E:\Projects\Chess_game\assets\images\black bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (80, 80))
black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))
black_king = pygame.image.load(r'E:\Projects\Chess_game\assets\images\black king.png')
black_king = pygame.transform.scale(black_king, (80, 80))
black_king_small = pygame.transform.scale(black_king, (45, 45))
black_knight = pygame.image.load(r'E:\Projects\Chess_game\assets\images\black knight.png')
black_knight = pygame.transform.scale(black_knight, (80, 80))
black_knight_small = pygame.transform.scale(black_knight, (45, 45))
black_pawn = pygame.image.load(r'E:\Projects\Chess_game\assets\images\black pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (65, 65))
black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))
black_rook = pygame.image.load(r'E:\Projects\Chess_game\assets\images\black rook.png')
black_rook = pygame.transform.scale(black_rook, (80, 80))
black_rook_small = pygame.transform.scale(black_rook, (45, 45))

#white pieces
white_queen = pygame.image.load(r'E:\Projects\Chess_game\assets\images\white queen.png')
white_queen = pygame.transform.scale(white_queen, (80, 80))
white_queen_small = pygame.transform.scale(white_queen, (45, 45))
white_bishop = pygame.image.load(r'E:\Projects\Chess_game\assets\images\white bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (80, 80))
white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))
white_king = pygame.image.load(r'E:\Projects\Chess_game\assets\images\white king.png')
white_king = pygame.transform.scale(white_king, (80, 80))
white_king_small = pygame.transform.scale(white_king, (45, 45))
white_knight = pygame.image.load(r'E:\Projects\Chess_game\assets\images\white knight.png')
white_knight = pygame.transform.scale(white_knight, (80, 80))
white_knight_small = pygame.transform.scale(white_knight, (45, 45))
white_pawn = pygame.image.load(r'E:\Projects\Chess_game\assets\images\white pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (65, 65))
white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))
white_rook = pygame.image.load(r'E:\Projects\Chess_game\assets\images\white rook.png')
white_rook = pygame.transform.scale(white_rook, (80, 80))
white_rook_small = pygame.transform.scale(white_rook, (45, 45))

white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small, white_rook_small, white_bishop_small]
black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small, black_rook_small, black_bishop_small]

piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']
# Check variables



#draw game main board
def draw_board():
    for i in range(32):
        colum = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, 'grey90', [600 - (colum * 200), row * 100, 100, 100])
            pygame.draw.rect(screen, 'burlywood4', [700 - (colum * 200), row * 100, 100, 100])
        else:
            pygame.draw.rect(screen, 'burlywood4', [600 - (colum * 200), row * 100, 100, 100])
            pygame.draw.rect(screen, 'grey90', [700 - (colum * 200), row * 100, 100, 100])

        pygame.draw.rect(screen, 'grey93', [0, 800, WIDTH, 100])
        pygame.draw.rect(screen, 'gold', [0, 800, WIDTH, 100], 5)
        pygame.draw.rect(screen, 'gold', [800, 0, 200, HEIGHT], 5)

        status_text =['White: Select a pice to Move', 'White: Select a Destinatio!', 
                      'Black: Select a pice to Move', 'Black: Select a Destinatio!']
        screen.blit(big_font.render(status_text[turn_step], True, 'black'), (20, 820))
        for i in range(9):
            pygame.draw.line(screen, 'black', (0, 100*i), (800, 100*i), 2)
            pygame.draw.line(screen, 'black', (100*i, 0), (100*i, 800), 2)

#draw pieces onto board
def draw_pieces():
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == 'pawn':
            screen.blit(white_pawn, (white_locations[i][0] * 100 + 22, white_locations[i][1] * 100 + 30))
        else:
            screen.blit(white_images[index], (white_locations[i][0] * 100 + 10, white_locations[i][1] * 100 + 10))

    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        if black_pieces[i] == 'pawn':
            screen.blit(black_pawn, (black_locations[i][0] * 100 + 22, black_locations[i][1] * 100 + 30))
        else:
            screen.blit(black_images[index], (black_locations[i][0] * 100 + 10, black_locations[i][1] * 100 + 10))
        


# main game loop
run = True
while run:
    timer.tick(fps)
    screen.fill('grey93')
    draw_board()
    draw_pieces()
    #event handeling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()
pygame.quit()
