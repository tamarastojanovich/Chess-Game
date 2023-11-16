import pygame

white_figures=[]
white_pawn=pygame.image.load('./iloveimg-resized/white_pawn.png')
white_pawn_small=pygame.image.load('./iloveimg-resized_small/white_pawn.png')
white_rook=pygame.image.load('./iloveimg-resized/rook_white.png')
white_rook_small=pygame.image.load('./iloveimg-resized_small/rook_white.png')
white_knight=pygame.image.load('./iloveimg-resized/knight_white.png')
white_knight_small=pygame.image.load('./iloveimg-resized_small/knight_white.png')
white_bishop=pygame.image.load('./iloveimg-resized/white_bishop.png')
white_bishop_small=pygame.image.load('./iloveimg-resized_small/white_bishop.png')
white_king=pygame.image.load('./iloveimg-resized/white_king.png')
white_king_small=pygame.image.load('./iloveimg-resized_small/white_king.png')
white_queen=pygame.image.load('./iloveimg-resized/white_queen.png')
white_queen_small=pygame.image.load('./iloveimg-resized_small/white_queen.png')

white_figures_positions=[(0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1),
                         (0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0)]
white_figures=[white_pawn,white_pawn,white_pawn,white_pawn,white_pawn,white_pawn,white_pawn,white_pawn,
               white_rook,white_knight,white_bishop,white_queen,white_king,white_bishop,white_knight,white_rook]

white_figures_small=[white_pawn_small,white_rook_small,white_knight_small,white_bishop_small,white_queen_small,white_king_small]

white_figure_list=["pawn1","pawn2","pawn3","pawn4","pawn5","pawn6","pawn7","pawn8",
                   "rook1","knight1","bishop1","queen","king","bishop2","knight2","rook2"]


black_pawn=pygame.image.load("./iloveimg-resized/black_pawn.png")
black_pawn_small=pygame.image.load('./iloveimg-resized_small/black_pawn.png')
black_rook=pygame.image.load("./iloveimg-resized/black_rook.png")
black_rook_small=pygame.image.load('./iloveimg-resized_small/black_rook.png')
black_knight=pygame.image.load("./iloveimg-resized/black_knight.png")
black_knight_small=pygame.image.load('./iloveimg-resized_small/black_knight.png')
black_bishop=pygame.image.load("./iloveimg-resized/black_bishop.png")
black_bishop_small=pygame.image.load('./iloveimg-resized_small/black_bishop.png')
black_king=pygame.image.load("./iloveimg-resized/black_king.png")
black_king_small=pygame.image.load('./iloveimg-resized_small/black_king.png')
black_queen=pygame.image.load("./iloveimg-resized/black_queen.png")
black_queen_small=pygame.image.load('./iloveimg-resized_small/black_queen.png')

black_figures_position=[(0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6),(7,6),
                         (0,7),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7)]


black_figures=[black_pawn,black_pawn,black_pawn,black_pawn,black_pawn,black_pawn,black_pawn,black_pawn,
               black_rook,black_knight,black_bishop,black_king,black_queen,black_bishop,black_knight,black_rook]
black_figures_small=[black_pawn_small,black_rook_small,black_knight_small,black_bishop_small,black_queen_small,black_king_small]

black_figure_list=["pawn1","pawn2","pawn3","pawn4","pawn5","pawn6","pawn7","pawn8",
                   "rook1","knight1","bishop1","king","queen","bishop2","knight2","rook2"]


last_moved_pawn=(-1,-1)

white_figures_moves={}

black_figures_moves={}

check_black=False
opponent_figures_b=[]


check_white=False
opponent_figures_w=[]

rook_left_white_moved=False
rook_right_white_moved=False
rook_left_black_moved=False
rook_right_black_moved=False
white_king_moved=False
black_king_moved=False