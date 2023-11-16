from figures import *
import copy 
def add_moves_for_white_rook_king_queen(figure,king):
    global check_black
    global check_white
    possible_moves=[]
    for i in range(1,8):
            current_pos=(white_figures_positions[figure][0],white_figures_positions[figure][1]+i)
            if current_pos[1]<8 and current_pos not in white_figures_positions:
                if king: 
                    if check_white and not resolves_check_white(figure,current_pos,king):
                        break
                if (check_white and resolves_check_white(figure,current_pos,king)) or not check_white:
                    possible_moves.append(current_pos)
                if current_pos in black_figures_position:
                    break
            else:
                break
            if king:
                break
    for i in range(1,8):
        current_pos=(white_figures_positions[figure][0]+i,white_figures_positions[figure][1])
        if current_pos[0]<8 and current_pos not in white_figures_positions:
            if king:
                if check_white and not resolves_check_white(figure,current_pos,king):
                    break
            if (check_white and resolves_check_white(figure,current_pos,king)) or not check_white:
                possible_moves.append(current_pos)
            if current_pos in black_figures_position:
                break
        else:
            break
        if king:
            break
    for i in range(1,8):
        current_pos=(white_figures_positions[figure][0],white_figures_positions[figure][1]-i)
        if current_pos[1]>=0 and current_pos not in white_figures_positions:
            if king:
                if check_white and not resolves_check_white(figure,current_pos,king):
                    break
            if (check_white and resolves_check_white(figure,current_pos,king)) or not check_white:
                possible_moves.append(current_pos)
            if current_pos in black_figures_position:
                break
        else:
            break
        if king:
            break
    for i in range(1,8):
        current_pos=(white_figures_positions[figure][0]-i,white_figures_positions[figure][1])
        if current_pos[0]>=0 and current_pos not in white_figures_positions:
            if king:
                if check_white and not resolves_check_white(figure,current_pos,king):
                    break
            if (check_white and resolves_check_white(figure,current_pos,king)) or not check_white:
                possible_moves.append(current_pos)
            if current_pos in black_figures_position:
                break
        else:
            break
        if king:
            break
    return possible_moves


def add_moves_for_black_rook_king_queen(figure,king):
    possible_moves=[]
    for i in range(1,8):
        current_pos=(black_figures_position[figure][0],black_figures_position[figure][1]+i)
        if current_pos[1]<8 and current_pos not in black_figures_position:
            if king:
                if check_black and not resolves_check_black(figure,current_pos,king):
                    break
            if (check_black and resolves_check_black(figure,current_pos,king)) or not check_black:
                possible_moves.append(current_pos)
            if current_pos in white_figures_positions:
                break
        else:
            break
        if king:
            break
    for i in range(1,8):
        current_pos=(black_figures_position[figure][0]+i,black_figures_position[figure][1])
        if current_pos[0]<8 and current_pos not in black_figures_position:
            if king:
                if check_black and not resolves_check_black(figure,current_pos,king):
                    break
            if (check_black and resolves_check_black(figure,current_pos,king)) or not check_black:
                possible_moves.append(current_pos)
            if current_pos in white_figures_positions:
                break
        else:
            break
        if king:
            break
    for i in range(1,8):
        current_pos=(black_figures_position[figure][0],black_figures_position[figure][1]-i)
        if current_pos[1]>=0 and current_pos not in black_figures_position:
            if king:
                if check_black and not resolves_check_black(figure,current_pos,king):
                    break
            if (check_black and resolves_check_black(figure,current_pos,king)) or not check_black:
                possible_moves.append(current_pos)
            if current_pos in white_figures_positions:
                break
        else:
            break
        if king:
            break
    for i in range(1,8):
        current_pos=(black_figures_position[figure][0]-i,black_figures_position[figure][1])
        if current_pos[0]>=0 and current_pos not in black_figures_position:
            if king:
                if check_black and not resolves_check_black(figure,current_pos,king):
                    break
            if (check_black and resolves_check_black(figure,current_pos,king)) or not check_black:
                possible_moves.append(current_pos)
            if current_pos in white_figures_positions:
                break
        else:
            break
        if king:
            break
    return possible_moves

def add_moves_for_white_bishop_king_queen(figure,king):
    possible_moves=[]
    for i in range(1,8):
            current_pos=(white_figures_positions[figure][0]+i,white_figures_positions[figure][1]+i)
            if current_pos[1]<8 and current_pos[0]<8 and current_pos not in white_figures_positions:
                if king:
                    if check_white and not resolves_check_white(figure,current_pos,king):
                        break
                if (check_white and resolves_check_white(figure,current_pos,king)) or not check_white:
                    possible_moves.append(current_pos)
                if current_pos in black_figures_position:
                    break
            else:
                break
            if king:
                break
    for i in range(1,8):
        current_pos=(white_figures_positions[figure][0]-i,white_figures_positions[figure][1]-i)
        if current_pos[0]>=0 and current_pos[1]>=0 and current_pos not in white_figures_positions:
            if king:
                if check_white and not resolves_check_white(figure,current_pos,king):
                    break
            if (check_white and resolves_check_white(figure,current_pos,king)) or not check_white:
                possible_moves.append(current_pos)
            if current_pos in black_figures_position:
                break
        else:
            break
        if king:
            break
    for i in range(1,8):
        current_pos=(white_figures_positions[figure][0]+i,white_figures_positions[figure][1]-i)
        if current_pos[1]>=0 and current_pos[0]<8 and current_pos not in white_figures_positions:
            if king:
                if check_white and not resolves_check_white(figure,current_pos,king):
                    break
            if (check_white and resolves_check_white(figure,current_pos,king)) or not check_white:
                possible_moves.append(current_pos)
            if current_pos in black_figures_position:
                break
        else:
            break
        if king:
            break
    for i in range(1,8):
        current_pos=(white_figures_positions[figure][0]-i,white_figures_positions[figure][1]+i)
        if current_pos[0]>=0 and current_pos[1]<8 and current_pos not in white_figures_positions:
            if king:
                if check_white and not resolves_check_white(figure,current_pos,king):
                    break
            if (check_white and resolves_check_white(figure,current_pos,king)) or not check_white:
                possible_moves.append(current_pos)
            if current_pos in black_figures_position:
                break
        else:
            break
        if king:
            break
    return possible_moves

def add_moves_for_black_bishop_king_queen(figure,king):
    possible_moves=[]
    for i in range(1,8):
        current_pos=(black_figures_position[figure][0]+i,black_figures_position[figure][1]+i)
        if current_pos[1]<8 and current_pos[0]<8 and current_pos not in black_figures_position:
            if king:
                if check_black and not resolves_check_black(figure,current_pos,king):
                    break
            if (check_black and resolves_check_black(figure,current_pos,king)) or not check_black:
                possible_moves.append(current_pos)
            if current_pos in white_figures_positions:
                break
        else:
            break
        if king:
            break
    for i in range(1,8):
        current_pos=(black_figures_position[figure][0]-i,black_figures_position[figure][1]-i)
        if current_pos[0]>=0 and current_pos[1]>=0 and current_pos not in black_figures_position:
            if king:
                if check_black and not resolves_check_black(figure,current_pos,king):
                    break
            if (check_black and resolves_check_black(figure,current_pos,king)) or not check_black:
                possible_moves.append(current_pos)
            if current_pos in white_figures_positions:
                break
        else:
            break
        if king:
            break
    for i in range(1,8):
        current_pos=(black_figures_position[figure][0]+i,black_figures_position[figure][1]-i)
        if current_pos[1]>=0 and current_pos[0]<8 and current_pos not in black_figures_position:
            if king:
                if check_black and not resolves_check_black(figure,current_pos,king):
                    break
            if (check_black and resolves_check_black(figure,current_pos,king)) or not check_black:
                possible_moves.append(current_pos)
            if current_pos in white_figures_positions:
                break
        else:
            break
        if king:
            break
    for i in range(1,8):
        current_pos=(black_figures_position[figure][0]-i,black_figures_position[figure][1]+i)
        if current_pos[0]>=0 and current_pos[1]<8 and current_pos not in black_figures_position:
            if king:
                if check_black and not resolves_check_black(figure,current_pos,king):
                    break
            if (check_black and resolves_check_black(figure,current_pos,king)) or not check_black:
                possible_moves.append(current_pos)
            if current_pos in white_figures_positions:
                break
        else:
            break
        if king:
            break
    return possible_moves




def possible_moves_for_white(figure):
    global last_moved_pawn
    possible_moves=[]
    if "pawn" in white_figure_list[figure]:
        move_ahead=(white_figures_positions[figure][0],white_figures_positions[figure][1]+1)
        if move_ahead[1]<=7 and move_ahead not in white_figures_positions and move_ahead not in black_figures_position:
            if (check_white and resolves_check_white(figure,move_ahead,False)) or not check_white:
                possible_moves.append((white_figures_positions[figure][0],white_figures_positions[figure][1]+1))
        if white_figures_positions[figure][1]==1 and move_ahead not in white_figures_positions and move_ahead not in black_figures_position:
            last_moved_pawn=(white_figures_positions[figure][0],white_figures_positions[figure][1]+2)
            if (check_white and resolves_check_white(figure,last_moved_pawn,False)) or not check_white:
                possible_moves.append(last_moved_pawn)
            
        kill_move_1=(white_figures_positions[figure][0]+1,white_figures_positions[figure][1]+1)
        kill_move_2=(white_figures_positions[figure][0]-1,white_figures_positions[figure][1]+1)
        if kill_move_1 in black_figures_position or (last_moved_pawn is not None and kill_move_1==(last_moved_pawn[0],last_moved_pawn[1]+1)):
            if (check_white and resolves_check_white(figure,kill_move_1,False)) or not check_white:
                possible_moves.append(kill_move_1)
        if kill_move_2 in black_figures_position or (last_moved_pawn is not None and kill_move_2==(last_moved_pawn[0],last_moved_pawn[1]+1)):
            if (check_white and resolves_check_white(figure,kill_move_2,False)) or not check_white:
                possible_moves.append(kill_move_2)
    elif "rook" in white_figure_list[figure]:
        possible_moves=add_moves_for_white_rook_king_queen(figure,False)
    elif "knight" in white_figure_list[figure]:
        curr_pos=white_figures_positions[figure]
        for i in (-2,-1,1,2):
            if i==1 or i==-1:
                append_pos=(curr_pos[0]+i,curr_pos[1]+2)
                if 0<=append_pos[0]<8 and append_pos[1]<8 and append_pos not in white_figures_positions:
                    if (check_white and resolves_check_white(figure,append_pos,False)) or not check_white:
                        possible_moves.append(append_pos)
                append_pos=(curr_pos[0]+i,curr_pos[1]-2)
                if 0<=append_pos[0]<8 and append_pos[1]>=0 and append_pos not in white_figures_positions:
                    if (check_white and resolves_check_white(figure,append_pos,False)) or not check_white:
                        possible_moves.append(append_pos)
            else:
                append_pos=(curr_pos[0]+i,curr_pos[1]+1)
                if 0<=append_pos[0]<8 and append_pos[1]<8 and append_pos not in white_figures_positions:
                    if (check_white and resolves_check_white(figure,append_pos,False)) or not check_white:
                        possible_moves.append(append_pos)
                append_pos=(curr_pos[0]+i,curr_pos[1]-1)
                if 0<=append_pos[0]<8 and append_pos[1]>=0 and append_pos not in white_figures_positions:
                    if (check_white and resolves_check_white(figure,append_pos,False)) or not check_white:
                        possible_moves.append(append_pos)
    elif "bishop" in white_figure_list[figure]:
        possible_moves=add_moves_for_white_bishop_king_queen(figure,False)
    elif white_figure_list[figure]=="king":
        possible_moves=add_moves_for_white_rook_king_queen(figure,True)
        possible_moves+=add_moves_for_white_bishop_king_queen(figure,True)
        if not white_king_moved and not check_white:
            if not rook_left_white_moved:
                if all(pos not in black_figures_position for pos in [(1,0),(2,0),(3,0)]) and all(pos not in white_figures_positions for pos in [(1,0),(2,0),(3,0)]):
                  if not is_in_check_white((2,0)) and not is_in_check_white((1,0)) and not is_in_check_white((3,0)):
                    possible_moves.append((0,0))
            if not rook_right_white_moved:
                if all(pos not in black_figures_position for pos in [(5,0),(6,0)]) and all(pos not in white_figures_positions for pos in [(5,0),(6,0)]):
                    if not is_in_check_white((5,0)) and not is_in_check_white((6,0)):
                        possible_moves.append((7,0))
    elif "queen" in white_figure_list[figure]:
        possible_moves=add_moves_for_white_rook_king_queen(figure,False)
        possible_moves+=add_moves_for_white_bishop_king_queen(figure,False)
    white_figures_moves[white_figure_list[figure]]=set(possible_moves)
    return possible_moves
        
def possible_moves_for_black(figure):
    global last_moved_pawn
    possible_moves=[]
    if "pawn" in black_figure_list[figure]:
        move_ahead=(black_figures_position[figure][0],black_figures_position[figure][1]-1)
        if move_ahead[1]>=0 and move_ahead not in black_figures_position and move_ahead not in white_figures_positions:
            if (check_black and resolves_check_black(figure,move_ahead,False)) or not check_black:
                possible_moves.append(move_ahead)
        if black_figures_position[figure][1]==6 and move_ahead not in white_figures_positions and move_ahead not in black_figures_position:
            last_moved_pawn=(black_figures_position[figure][0],black_figures_position[figure][1]-2)
            if (check_black and resolves_check_black(figure,last_moved_pawn,False)) or not check_black:
                possible_moves.append(last_moved_pawn)
        kill_move_1=(black_figures_position[figure][0]+1,black_figures_position[figure][1]-1)
        kill_move_2=(black_figures_position[figure][0]-1,black_figures_position[figure][1]-1)
        if kill_move_1 in white_figures_positions or kill_move_1==(last_moved_pawn[0],last_moved_pawn[1]-1):
            if (check_black and resolves_check_black(figure,kill_move_1,False)) or not check_black:
                possible_moves.append(kill_move_1)
        if kill_move_2 in white_figures_positions or kill_move_2==(last_moved_pawn[0],last_moved_pawn[1]-1):
            if (check_black and resolves_check_black(figure,kill_move_2,False)) or not check_black:
                possible_moves.append(kill_move_2)
    elif "rook" in black_figure_list[figure]:
       possible_moves=add_moves_for_black_rook_king_queen(figure,False)
    elif "knight" in black_figure_list[figure]:
        curr_pos=black_figures_position[figure]
        for i in (-2,-1,1,2):
            if i==1 or i==-1:
                append_pos=(curr_pos[0]+i,curr_pos[1]+2)
                if 0<=append_pos[0]<8 and append_pos[1]<8 and append_pos not in black_figures_position:
                    if (check_black and resolves_check_black(figure,append_pos,False)) or not check_black:
                        possible_moves.append(append_pos)
                append_pos=(curr_pos[0]+i,curr_pos[1]-2)
                if 0<=append_pos[0]<8 and append_pos[1]>=0 and append_pos not in black_figures_position:
                    if (check_black and resolves_check_black(figure,append_pos,False)) or not check_black:
                        possible_moves.append(append_pos)
            else:
                append_pos=(curr_pos[0]+i,curr_pos[1]+1)
                if 0<=append_pos[0]<8 and append_pos[1]<8 and append_pos not in black_figures_position:
                    if (check_black and resolves_check_black(figure,append_pos,False)) or not check_black:
                        possible_moves.append(append_pos)
                append_pos=(curr_pos[0]+i,curr_pos[1]-1)
                if 0<=append_pos[0]<8 and append_pos[1]>=0 and append_pos not in black_figures_position:
                    if (check_black and resolves_check_black(figure,append_pos,False)) or not check_black:
                        possible_moves.append(append_pos)
    elif "bishop" in black_figure_list[figure]:
       possible_moves=add_moves_for_black_bishop_king_queen(figure,False)
    elif black_figure_list[figure]=="king":
        possible_moves=add_moves_for_black_rook_king_queen(figure,True)
        possible_moves+=add_moves_for_black_bishop_king_queen(figure,True)
        if not black_king_moved and not check_black:
            if not rook_left_black_moved:
                if all(pos not in black_figures_position for pos in [(1,7),(2,7)]) and all(pos not in white_figures_positions for pos in [(1,7),(2,7)]):
                  if not is_in_check_black((2,7)) and not is_in_check_black(1,7):
                      possible_moves.append((0,7))
            if not rook_right_black_moved:
                if all(pos not in black_figures_position for pos in [(4,7),(5,7),(6,7)]) and all(pos not in white_figures_positions for pos in [(4,7),(5,7),(6,7)]):
                    if not is_in_check_black((5,7)) and not is_in_check_black((6,7)) and not is_in_check_black((4,7)):
                        possible_moves.append((7,7))
    elif "queen" in black_figure_list[figure]:
        possible_moves=add_moves_for_black_rook_king_queen(figure,False)
        possible_moves+=add_moves_for_black_bishop_king_queen(figure,False)
    
    black_figures_moves[black_figure_list[figure]]=set(possible_moves)
    return possible_moves      


def resolves_check_black(fig,pos,king):
    global black_figures_position
    global check_black
    temp_pos=copy.deepcopy(black_figures_position)
    for figure in opponent_figures_b:
        if king:
            if pos not in white_figures_moves[figure]:
                continue
            else:
                return False
        if pos in white_figures_moves[figure]:
            black_figures_position[fig]=pos
            possible_moves_for_white(white_figure_list.index(figure))
            check_if_in_check_black(None)
            if not check_black:
                black_figures_position=temp_pos
                possible_moves_for_white(white_figure_list.index(figure))
                check_if_in_check_black(None)
                return True
            black_figures_position=temp_pos
            possible_moves_for_white(white_figure_list.index(figure))
            check_if_in_check_black(None)
        elif pos==white_figures_positions[white_figure_list.index(figure)]:
            return True
    if king:
        return True
    return False

def resolves_check_white(fig,pos,king):
    global white_figures_positions
    global check_white
    temp_pos=copy.deepcopy(white_figures_positions)
    for figure in opponent_figures_w:
        if king:
            if pos not in black_figures_moves[figure]:
                continue
            else:
                return False
        elif pos in black_figures_moves[figure]:
            white_figures_positions[fig]=pos
            possible_moves_for_black(black_figure_list.index(figure))
            check_if_in_check_white(None)
            if not check_white:
                white_figures_positions=temp_pos
                possible_moves_for_black(black_figure_list.index(figure))
                check_if_in_check_white(None)
                
                return True
            white_figures_positions=temp_pos
            possible_moves_for_black(black_figure_list.index(figure))
            check_if_in_check_white(None)
            
        elif pos==black_figure_list[black_figure_list.index(figure)]:
            return True
    if king:
        return True
    return False
def check_if_in_check_white(pos):
    global opponent_figures_w
    global check_white
    opponent_figures_w=[]
    if pos is None:
        pos=white_figures_positions[white_figure_list.index("king")]
    for figure in black_figures_moves:
        if pos in black_figures_moves[figure]:
            check_white=True
            opponent_figures_w.append(figure)
    if len(opponent_figures_w)>0: return True
    check_white=False
    return False

def check_if_in_check_black(pos):
    global opponent_figures_b
    global check_black
    opponent_figures_b=[]
    if pos is None:
        pos=black_figures_position[black_figure_list.index("king")]
    for figure in white_figures_moves:
        if pos in white_figures_moves[figure]:
            check_black=True
            opponent_figures_b.append(figure)
            
    if len(opponent_figures_b)>0:
        return True
    check_black=False
    return False
    
def is_in_check_black(pos):
    for figure in white_figure_list:
        if pos in white_figures_moves[figure]:
            return True
    return False

    
def is_in_check_white(pos):
    for figure in black_figure_list:
        if pos in black_figures_moves[figure]:
            return True
    return False
