import pygame
import pygame_gui
from moves import *
import tkinter as tk
from tkinter import messagebox
import copy
pygame.init()

screen=pygame.display.set_mode((600,700),pygame.SRCALPHA)
timer=pygame.time.Clock()
font = pygame.font.SysFont("Arial",18)
run=True
selected_figure=None
size_of_square=100

UiManager=pygame_gui.UIManager((600,700))
ButtonManager=pygame_gui.UIManager((600,700))


UsernameInputFirst=pygame_gui.elements.UITextEntryLine(pygame.Rect(200,250,200,50),initial_text="White player",manager=UiManager,object_id="#username_one")
UsernameInputSecond=pygame_gui.elements.UITextEntryLine(pygame.Rect(200,310,200,50),initial_text="Black player",manager=UiManager,object_id="#username_second")


button_knight=pygame_gui.elements.UIButton(pygame.Rect((200, 260), (100, 50)),text="Knight",manager=ButtonManager)
button_rook=pygame_gui.elements.UIButton(pygame.Rect((200, 310), (100, 50)),text="Rook",manager=ButtonManager)
button_queen=pygame_gui.elements.UIButton(pygame.Rect((310, 260), (100, 50)),text="Queen",manager=ButtonManager)
button_bishop=pygame_gui.elements.UIButton(pygame.Rect((310, 310), (100, 50)),text="Bishop",manager=ButtonManager)


username_1="Player 1"
username_2="Player 2"

white_player_result=[0,0,0,0,0,0]

white_possible_moves_for_check=[]

black_possible_moves_for_check=[]

black_player_result=[0,0,0,0,0,0]

knight_num_start_w=3
rook_num_start_w=3
queen_num_start_w=1
bishop_num_start_w=3

knight_num_start_b=3
rook_num_start_b=3
queen_num_start_b=1
bishop_num_start_b=3


small_figures=["pawn","rook","knight","bishop","queen","king"]
turn=1 #0 is black

transparent_blue=(0, 0, 255, 128)

root=None


def restart():
    global white_player_result, black_player_result
    global white_possible_moves_for_check, black_possible_moves_for_check
    global white_figures_positions
    
    global black_figures_position
    global white_figures,black_figures
    global white_figure_list, black_figure_list
    global white_figures_moves, black_figures_moves
    global check_white, check_black
    global opponent_figures_w, opponent_figures_b
    global rook_left_white_moved, rook_left_black_moved
    global rook_right_white_moved, rook_right_black_moved
    global white_king_moved, black_king_moved
    global turn, last_moved_pawn
    
    
    white_player_result=[0,0,0,0,0,0]
    black_player_result=[0,0,0,0,0,0]
    
    white_possible_moves_for_check=[]
    black_possible_moves_for_check=[]
    
    white_figures_pos=[(0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1),
                         (0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0)]
    
    
    black_figures_pos=[(0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6),(7,6),
                         (0,7),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7)]
    
    
    for i in range(0,len(black_figures_pos)):
        black_figures_position[i]=black_figures_pos[i]
        white_figures_positions[i]=white_figures_pos[i]
    
    white_figures=[white_pawn,white_pawn,white_pawn,white_pawn,white_pawn,white_pawn,white_pawn,white_pawn,
               white_rook,white_knight,white_bishop,white_queen,white_king,white_bishop,white_knight,white_rook]

    black_figures=[black_pawn,black_pawn,black_pawn,black_pawn,black_pawn,black_pawn,black_pawn,black_pawn,
               black_rook,black_knight,black_bishop,black_king,black_queen,black_bishop,black_knight,black_rook]
    
    
    white_figure_list=["pawn1","pawn2","pawn3","pawn4","pawn5","pawn6","pawn7","pawn8",
                   "rook1","knight1","bishop1","queen","king","bishop2","knight2","rook2"]
    
    black_figure_list=["pawn1","pawn2","pawn3","pawn4","pawn5","pawn6","pawn7","pawn8",
                   "rook1","knight1","bishop1","king","queen","bishop2","knight2","rook2"]

    
    white_figures_moves={}
    black_figures_moves={}
    
    check_white=False
    check_black=False
    
    opponent_figures_w=[]
    opponent_figures_b=[]
    
    rook_left_white_moved=False
    rook_left_black_moved=False
    
    rook_right_white_moved=False
    rook_right_black_moved=False
    
    white_king_moved=False
    black_king_moved=False
    
    turn=1
    last_moved_pawn=(-1,-1)
    
    init_moves()


def change_pawn_to_queen(index,white):
    global white_figure_list,black_figure_list
    global white_figures,black_figures
    global queen_num_start_b,queen_num_start_w
    if white:
        white_figure_list[index]="queen"+str(queen_num_start_w)
        white_figures[index]=white_queen
        queen_num_start_w+=1
    else:
        black_figure_list[index]="queen"+str(queen_num_start_b)
        black_figures[index]=black_queen
        queen_num_start_b+=1
    
        
def change_pawn_to_rook(index,white):
    global white_figure_list,black_figure_list
    global white_figures,black_figures
    global rook_num_start_b,rook_num_start_w
    if white:
        white_figure_list[index]="rook"+str(rook_num_start_w)
        white_figures[index]=white_rook
        rook_num_start_w+=1
    else:
        black_figure_list[index]="rook"+str(rook_num_start_b)
        black_figures[index]=black_rook
        rook_num_start_b+=1
  
    
        
        
def change_pawn_to_knight(index,white):
    global white_figure_list,black_figure_list
    global white_figures,black_figures
    global knight_num_start_b,knight_num_start_w
    if white:
        white_figure_list[index]="knight"+str(knight_num_start_w)
        white_figures[index]=white_knight
        knight_num_start_w+=1
    else:
        black_figure_list[index]="knight"+str(knight_num_start_b)
        black_figures[index]=black_knight
        knight_num_start_b+=1

    
        
        
def change_pawn_to_bishop(index,white):
    global white_figure_list,black_figure_list
    global white_figures,black_figures
    global bishop_num_start_b,bishop_num_start_w
    if white:
        white_figure_list[index]="bishop"+str(bishop_num_start_w)
        white_figures[index]=white_bishop
        bishop_num_start_w+=1
    else:
        black_figure_list[index]="bishop"+str(bishop_num_start_b)
        black_figures[index]=black_bishop
        bishop_num_start_b+=1


def change_pawn(index,white):
    global white_figures_moves,black_figures_moves
    if white:
        white_figures_moves[white_figure_list[index]]=[]
    else:
        black_figures_moves[black_figure_list[index]]=[]
        
    font = pygame.font.SysFont("Times New Roman",19)
    screen.fill("black",(180,200,250,200))
    text=font.render("Pick new role for pawn:",True,"white")
    screen.blit(text,(180,220))
    
    ButtonManager.draw_ui(screen)
    
    UI_refresh=timer.tick(60)/20000
    
    while True:
        for events in pygame.event.get():
            if events.type==pygame.QUIT:
                pygame.quit()
            if events.type==pygame_gui.UI_BUTTON_PRESSED:
                if button_knight.check_pressed():
                    change_pawn_to_knight(index,white)
                    return
                elif button_bishop.check_pressed():
                    change_pawn_to_bishop(index,white)
                    return
                elif button_queen.check_pressed():
                    change_pawn_to_queen(index,white)
                    return
                elif button_rook.check_pressed():
                    change_pawn_to_rook(index,white)
                    return
                
            ButtonManager.process_events(events)
            
        ButtonManager.update(UI_refresh)
        
        screen.fill("black",(180,200,250,200))
        screen.fill("saddlebrown",(190,210,230,180))
        text=font.render("Pick new role for pawn:",True,"white")
        screen.blit(text,(200,220))
        
        
        ButtonManager.draw_ui(screen)
        
        pygame.display.update()

def init_moves():
    for i in range(len(white_figure_list)):
        white_figures_moves[white_figure_list[i]]=set()
        white_figures_moves[white_figure_list[i]]=set(possible_moves_for_white(i))
        if white_figure_list[i]=="king":
            index_king=black_figure_list.index("king")
            black_figures_moves["king"]=set()
            black_figures_moves["king"]=set(possible_moves_for_black(index_king))
            continue
        elif white_figure_list[i]=="queen":
            index_queen=black_figure_list.index("queen")
            black_figures_moves["queen"]=set()
            black_figures_moves["queen"]=set(possible_moves_for_black(index_queen))
            continue
        black_figures_moves[black_figure_list[i]]=set()
        black_figures_moves[black_figure_list[i]]=set(possible_moves_for_black(i))
        


def refresh_moves(position):
    for figure in white_figures_moves:
        if position in white_figures_moves[figure]:
            white_figures_moves[figure]=set(possible_moves_for_white(white_figure_list.index(figure)))
    for figure in black_figures_moves:
        if position in black_figures_moves[figure]:
            black_figures_moves[figure]=set(possible_moves_for_black(black_figure_list.index(figure)))


def get_usernames():
    global username_1, username_2
    font = pygame.font.SysFont("Times New Roman",19)
    font_enter=pygame.font.SysFont("Times New Roman",19)
    font_enter.set_italic(True)
    screen.fill("black",(180,200,250,200))
    text=font.render("Enter players' names:",True,"white")
    screen.blit(text,(200,220))
    
    text=font_enter.render("Press ENTER to continue",True,"azure4")
    screen.blit(text,(200,350))
    
    UiManager.draw_ui(screen)
    
    UI_refresh=timer.tick(60)/20000
    while True:

        for events in pygame.event.get():
            if events.type==pygame.QUIT:
                pygame.quit()
            if events.type==pygame_gui.UI_TEXT_ENTRY_FINISHED:
                username_1=UsernameInputFirst.get_text()
                username_2=UsernameInputSecond.get_text()
                
                return
            UiManager.process_events(events)
            
        UiManager.update(UI_refresh)
        
        screen.fill("black",(180,200,250,200))
        screen.fill("saddlebrown",(190,210,230,180))
        text=font.render("Enter players' names:",True,"white")
        screen.blit(text,(200,220))
        
        text=font_enter.render("Press ENTER to continue",True,"azure4")
        screen.blit(text,(200,360))
        
        UiManager.draw_ui(screen)
        
        pygame.display.update()
        
def draw_board():
    screen.fill("saddlebrown",(0,0,600,600))
    screen.fill("white",(18,18,565,565))
    font = pygame.font.SysFont("Times New Roman",19)
    font.set_bold(True)
    for row in range(8):
        text=font.render(chr(49+row),True,"white")
        screen.blit(text,(3,row*70+50))
        text=font.render(chr(65+row),True,"white")
        screen.blit(text,(50+row*70,8*70+19))
        for column in range(8):
            row_=row%2
            column_=column%2
            if (row_==0 and column_==1) or (row_==1 and column_==0):
                pygame.draw.rect(screen,'#8B4513',(row*70+20,column*70+20,70,70))
            else:
                pygame.draw.rect(screen,'white',(row*70+20,column*70+20,70,70))
    

    
def draw_figures():
    for i in range(16):
        if white_figures_positions[i] !=(-1,-1):
            screen.blit(white_figures[i],(white_figures_positions[i][0]*70+35,white_figures_positions[i][1]*70+25))
        if black_figures_position[i] !=(-1,-1):
            screen.blit(black_figures[i],(black_figures_position[i][0]*70+35,black_figures_position[i][1]*70+25))
            
def update_results():
    
    if turn==0:
        screen.fill('peru',(0,70*8+40,600,50))
        pygame.draw.line(screen,'white',(0,70*8+39),(600,70*8+39),2)
        pygame.draw.line(screen,'white',(0,70*8+89),(600,70*8+89),2)
        screen.fill('#8B4513',(0,70*8+50+40,600,50))
        pygame.draw.line(screen,'white',(0,70*8+89+50),(600,70*8+89+50),2)
        
    else:
        screen.fill('#8B4513',(0,70*8+40,600,50))
        pygame.draw.line(screen,'white',(0,70*8+39),(600,70*8+39),2)
        
        pygame.draw.line(screen,'white',(0,70*8+89),(600,70*8+89),2)
        screen.fill('peru',(0,70*8+50+40,600,50))
        pygame.draw.line(screen,'white',(0,70*8+89+50),(600,70*8+89+50),2)
        
    text=font.render(username_2,True,(0,0,0))
    screen.blit(text,(10,70*8+15+40))
    text=font.render(username_1,True,(255,255,255))
    screen.blit(text,(10,70*8+65+40))
    for i in range(6):
        screen.blit(white_figures_small[i],(90+i*80,70*8+10+35))
        text=font.render(""+str(black_player_result[i]),True,(255,255,255))
        screen.blit(text,(140+i*80,70*8+15+40))
        screen.blit(black_figures_small[i],(90+i*80,70*8+60+35))
        text=font.render(""+str(white_player_result[i]),True,(255,255,255))
        screen.blit(text,(140+i*80,70*8+65+40))
        
def mark_possible_moves(pos_list):
    for pos in pos_list:
        transparent_rect = pygame.Surface((70, 70), pygame.SRCALPHA)
        pygame.draw.rect(transparent_rect, transparent_blue, (0, 0, 70, 70))

        screen.blit(transparent_rect, (pos[0]*70+20, pos[1]*70+20))
    pygame.display.flip()
    
screen.fill('grey')
timer.tick(60)

init_moves()
draw_board()   
draw_figures()
update_results()
get_usernames()
while run:
    draw_board()   
    draw_figures()
    update_results()

    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            run=False
        if e.type==pygame.MOUSEBUTTONDOWN:
            x_coord=e.pos[0]//70
            y_coord=e.pos[1]//70
            pos=(x_coord,y_coord)
            if pos in white_figures_positions and turn:
                index=white_figures_positions.index(pos)
                possible_moves=possible_moves_for_white(index)
                mark_possible_moves(possible_moves)
                clicked=False
                while not clicked:
                    for e in pygame.event.get():
                        if e.type==pygame.MOUSEBUTTONDOWN:
                            x_coord=e.pos[0]//70
                            y_coord=e.pos[1]//70
                            pos=(x_coord,y_coord)
                            if pos in possible_moves:
                                white_figures_positions[index]=pos
                                if white_figure_list[index]=="rook1":
                                    rook_left_white_moved=True
                                elif white_figure_list[index]=="rook2":
                                    rook_right_white_moved=True
                                elif white_figure_list[index]=="king":
                                    white_king_moved=True
                                    if pos==white_figures_positions[white_figure_list.index("rook1")]:
                                        pos_of_rook1=white_figures_positions[white_figure_list.index("rook1")]
                                        white_figures_positions[index]=(pos_of_rook1[0]+2,pos_of_rook1[1])
                                        white_figures_positions[white_figure_list.index("rook1")]=(pos_of_rook1[0]+3,pos_of_rook1[1])
                                    elif pos==white_figures_positions[white_figure_list.index("rook2")]:
                                        pos_of_rook2=white_figures_positions[white_figure_list.index("rook2")]
                                        white_figures_positions[index]=(pos_of_rook2[0]-1,pos_of_rook2[1])
                                        white_figures_positions[white_figure_list.index("rook2")]=(pos_of_rook2[0]-2,pos_of_rook2[1])
                                if pos in black_figures_position:
                                    figure=black_figures_position.index(pos)
                                    black_figures_position[figure]=(-1,-1)
                                    name_of_figure=black_figure_list[figure]
                                    black_figures_moves[name_of_figure]=[]
                                    if name_of_figure== "king" or name_of_figure=="queen":
                                        result=small_figures.index(name_of_figure)
                                        if name_of_figure=="king":
                                            font_winner=pygame.font.SysFont("Times New Roman",40)
                                            font_winner.set_bold(True)
                                            screen.fill("white",(80,170,450,210))
                                            screen.fill("peru",(85,175,440,200))
                                            text=font_winner.render(username_1+" WINS!",True,"springgreen")
                                            screen.blit(text,(100,200))
                                            
                                            text=font_winner.render("PRESS   ENTER   FOR",True,"springgreen")
                                            screen.blit(text,(100,250))
                                            
                                            text=font_winner.render("A   REMATCH!",True,"springgreen")
                                            screen.blit(text,(100,300))
                                            pygame.display.update()
                                            restarted=False
                                            while not restarted:
                                                for e in pygame.event.get():
                                                    if e.type==pygame.QUIT:
                                                        pygame.quit()
                                                    if e.type==pygame.KEYDOWN:
                                                        if e.key==pygame.K_RETURN or e.key==pygame.K_KP_ENTER:
                                                            restart()
                                                            restarted=True
                                                            clicked=True
                                                            break
                                            break
                                    else:
                                        name_of_figure=name_of_figure.rstrip(name_of_figure[-1])
                                        result=small_figures.index(name_of_figure)
                                    white_player_result[result]+=1
                                    if pos!=last_moved_pawn:
                                        last_moved_pawn=(-1,-1)
                                elif pos==(last_moved_pawn[0],last_moved_pawn[1]+1) and last_moved_pawn in black_figures_position:
                                    figure=black_figures_position.index(last_moved_pawn)
                                    black_figures_position[figure]=(-1,-1)
                                    name_of_figure=black_figure_list[figure]
                                    black_figures_moves[name_of_figure]=[]
                                    if name_of_figure== "king" or name_of_figure=="queen":
                                        result=small_figures.index(name_of_figure)
                                    else:
                                        name_of_figure=name_of_figure.rstrip(name_of_figure[-1])
                                        result=small_figures.index(name_of_figure)
                                        
                                    white_player_result[result]+=1
                                    if pos!=last_moved_pawn:
                                        last_moved_pawn=(-1,-1)
                                turn=(turn+1)%2
                                if "pawn" in white_figure_list[index] and white_figures_positions[index][1]==7:
                                    change_pawn(index,True)
                                white_figures_moves[white_figure_list[index]]=set(possible_moves_for_white(index))
                                refresh_moves(pos)
                                check_if_in_check_black(None)
                                check_if_in_check_white(None)
                            clicked=True
                            
                            break
                        elif e.type==pygame.QUIT:
                            pygame.quit()
                            break
            elif pos in black_figures_position and not turn:
                index=black_figures_position.index(pos)
                possible_moves=possible_moves_for_black(index)
                mark_possible_moves(possible_moves)
                clicked=False
                while not clicked:
                    for e in pygame.event.get():
                        if e.type==pygame.MOUSEBUTTONDOWN:
                            x_coord=e.pos[0]//70
                            y_coord=e.pos[1]//70
                            pos=(x_coord,y_coord)
                            if pos in possible_moves:
                                black_figures_position[index]=pos
                                if black_figure_list[index]=="rook1":
                                    rook_left_black_moved=True
                                elif black_figure_list[index]=="rook2":
                                    rook_right_black_moved=True
                                elif black_figure_list[index]=="king":
                                    black_king_moved=True
                                    if pos==black_figures_position[black_figure_list.index("rook1")]:
                                        pos_of_rook1=black_figures_position[black_figure_list.index("rook1")]
                                        black_figures_position[index]=(pos_of_rook1[0]+1,pos_of_rook1[1])
                                        black_figures_position[black_figure_list.index("rook1")]=(pos_of_rook1[0]+2,pos_of_rook1[1])
                                    elif pos==black_figures_position[black_figure_list.index("rook2")]:
                                        pos_of_rook2=black_figures_position[black_figure_list.index("rook2")]
                                        black_figures_position[index]=(pos_of_rook2[0]-2,pos_of_rook2[1])
                                        black_figures_position[black_figure_list.index("rook2")]=(pos_of_rook2[0]-3,pos_of_rook2[1])
                                if pos in white_figures_positions:
                                    figure=white_figures_positions.index(pos)
                                    white_figures_positions[figure]=(-1,-1)
                                    name_of_figure=white_figure_list[figure]
                                    white_figures_moves[name_of_figure]=[]
                                    if name_of_figure== "king" or name_of_figure=="queen":
                                        result=small_figures.index(name_of_figure)
                                        if name_of_figure=="king":
                                            font_winner=pygame.font.SysFont("Times New Roman",40)
                                            font_winner.set_bold(True)
                                            screen.fill("white",(80,170,450,210))
                                            screen.fill("peru",(85,175,440,200))
                                            text=font_winner.render(username_1+" WINS!",True,"springgreen")
                                            screen.blit(text,(100,200))
                                            
                                            text=font_winner.render("PRESS   ENTER   FOR",True,"springgreen")
                                            screen.blit(text,(100,250))
                                            
                                            text=font_winner.render("A   REMATCH!",True,"springgreen")
                                            screen.blit(text,(100,300))
                                            pygame.display.update()
                                            restarted=False
                                            while not restarted:
                                                for e in pygame.event.get():
                                                    if e.type==pygame.QUIT:
                                                        pygame.quit()
                                                    if e.type==pygame.KEYDOWN:
                                                        if e.key==pygame.K_RETURN or e.key==pygame.K_KP_ENTER:
                                                            restart()
                                                            restarted=True
                                                            clicked=True
                                                            break
                                            break
                                    else:
                                        name_of_figure=name_of_figure.rstrip(name_of_figure[-1])
                                        result=small_figures.index(name_of_figure)
                                    black_player_result[result]+=1
                                    if pos!=last_moved_pawn:
                                        last_moved_pawn=(-1,-1)
                                
                                elif pos==(last_moved_pawn[0],last_moved_pawn[1]-1) and last_moved_pawn in white_figures_positions:
                                    figure=white_figures_positions.index(last_moved_pawn)
                                    white_figures_positions[figure]=(-1,-1)
                                    name_of_figure=white_figure_list[figure]
                                    white_figures_moves[name_of_figure]=[]
                                    if name_of_figure== "king" or name_of_figure=="queen":
                                        result=small_figures.index(name_of_figure)
                                    else:
                                        name_of_figure=name_of_figure.rstrip(name_of_figure[-1])
                                        result=small_figures.index(name_of_figure)
                                        
                                    black_player_result[result]+=1
                                    if pos!=last_moved_pawn:
                                        last_moved_pawn=(-1,-1)
                                turn=(turn+1)%2
                                if "pawn" in black_figure_list[index] and black_figures_position[index][1]==0:
                                    change_pawn(index,False)
                                black_figures_moves[black_figure_list[index]]=set(possible_moves_for_black(index))
                                refresh_moves(pos)
                                check_if_in_check_white(None)
                                check_if_in_check_black(None)
                            clicked=True
                            break
                        elif e.type==pygame.QUIT:
                            pygame.quit()
                            break
            
            
    pygame.display.flip()

