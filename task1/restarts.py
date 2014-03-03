"""Greedy hill climbing with sideways moves and restarts
Petrousov Ioannis University of Western Macedonia
Department of Informatics and Telecommunication
"""
from numpy.random import randint
from numpy import zeros
import sys
from termcolor import colored
from pieces_class import *

############################################# function space ##################################################
def find_collisions(chessboard):
    total_collisions = 0
    for r in range(8): #gia oles tis grammes
        for c in range(8): #gia oles tis steiles
            if chessboard[r][c] == 'Q':
                queen_position = r,c #dhmiourgei tuple poy periexei to position thw twrinis vasilissas
                #print 'queen at ',r,c
                collisions_found = queen_search(queen_position, chessboard)
                total_collisions = total_collisions + collisions_found

            elif chessboard[r][c] == 'K':
                knight_position = r,c
                #print 'knight at ',r,c
                collisions_found = knight_search(knight_position, chessboard)
                total_collisions = total_collisions + collisions_found
    return total_collisions



def queen_search(queen_position, chessboard): #vriskei oles tis sygkrouseis an eisai se vasilissa
    #print 'searching queen'
    #create nupmy array with 1 and 0 to use to collision find bellow
    #collision_board = zeros((8,8), int)
    #gia ka8e stoixeio sto chessboard 8a valoume 1 sto collision_board
    """for i in range(queen_position[0], 8):
        for j in range(queen_position[1], 8):
            if chessboard[i][j] != 0:
                collision_board[i][j] = 1"""
    collision_counter = 0
    #testing up search for K only
    #print '############up'
    for r in range(queen_position[0]-1,-1,-1): 
        if chessboard[r][queen_position[1]] == 'K':
     #       print 'collides with ',r, queen_position[1]
            collision_counter = collision_counter + 1
            break
        elif chessboard[r][queen_position[1]] == 'Q':
            break
    #right search
    #print '##############right'
    for c in range(queen_position[1]+1, 8): 
        if chessboard[queen_position[0]][c] != 0:
      #      print 'collides with ',queen_position[0], c
            collision_counter = collision_counter + 1
            break
    #down right search
    #print '###############right ','down'
    for r,c in zip( range(queen_position[0]+1, 8), range(queen_position[1]+1, 8)): #This function returns a list of tuples
        if chessboard[r][c] != 0:
        #    print 'collides with ',r,c
            collision_counter = collision_counter + 1
            break
    # down search
    #print '################down'
    for r in range(queen_position[0]+1, 8):
        if chessboard[r][queen_position[1]]:
         #   print 'collides with ',r,queen_position[1]
            collision_counter = collision_counter + 1
            break
    #down left search
    #print '###################left down'
    for r,c in zip(range(queen_position[0]+1,8), range(queen_position[1]-1,-1,-1)):
        if chessboard[r][c] != 0:
          #  print 'collides with ',r,c
            collision_counter = collision_counter + 1
            break
#testing this move, queen will search left for K only
    #print '##############left'
    for c in range(queen_position[1]-1,-1,-1):
        if chessboard[queen_position[0]][c] == 'K':
            collision_counter = collision_counter + 1
           # print 'collides with knight ',queen_position[0],c
            break
        elif chessboard[queen_position[0]][c] == 'Q':
            break
    return collision_counter


def knight_search(knight_position, chessboard): #vrisei les tis sygkrouseis an eisai se knight
    collision_counter = 0
    #down right
    #print '########## down right'
    for r,c in zip( range(knight_position[0]+1, 8), range(knight_position[1]+1, 8)): #This function returns a list of tuples
        if chessboard[r][c] != 0:
            collision_counter = collision_counter + 1
       #     print 'collides with ',r,c
            break
    #down left search
    #print '######## down left'
    for r,c in zip(range(knight_position[0]+1,8), range(knight_position[1]-1,-1,-1)):
        if chessboard[r][c] != 0:
            collision_counter = collision_counter + 1
        #    print 'collides with ',r,c
            break
    return collision_counter

def queen_move(chessboard, current_collisions_number, queens, queen_coor):
    #print 'moving queen'
    chessboard[queen_coor[0]][queen_coor[1]] = 0 #delete from original position
    for q in range(len(queens)):
        if queens[q].initial_position == queen_coor:
            qp = q
    #print '##########up'
    for up in range(queens[qp].initial_position[0]-1, -1, -1): #for every up move of queen
        if chessboard[up][queens[qp].initial_position[1]] == 0: #an mporeis na pas panw kai den peftei se allo kommati
            chessboard[up][queens[qp].initial_position[1]] = 'Q' #move one up
            #print_search(chessboard),
            collisions_found = find_collisions(chessboard)   #have to store it
            #print 'collisions found=',collisions_found
            chessboard[up][queens[qp].initial_position[1]] = 0 #delete the move
            if collisions_found <= current_collisions_number: # if the collisions found is less than current
                #initial_position = queen_position[0], queen_position[1] #store initla position of queen
                queens[qp].possible_collisions.append(collisions_found)
                queens[qp].possible_moves.append([up, queens[qp].initial_position[1]]) #store final position of queen
        elif chessboard[up][queens[qp].initial_position[1]] != 0: #8a spasei an pesei se allo kommati
            break
#    print '\n###########up right '
    for up,right in zip(range(queens[qp].initial_position[0]-1, -1, -1), range(queens[qp].initial_position[1]+1, 8)):
        if chessboard[up][right] == 0:
            chessboard[up][right] = 'Q'
           # print_search(chessboard),
            collisions_found = find_collisions(chessboard)
 #           print 'collisions=',collisions_found
            chessboard[up][right] = 0
            if collisions_found <= current_collisions_number:
                queens[qp].possible_collisions.append(collisions_found)
                queens[qp].possible_moves.append([up, right]) #store final position of queen
        elif chessboard[up][right] != 0: #8a spasei an pesei se allo kommati
            break
  #  print '\n###########right '
    for right in range(queens[qp].initial_position[1]+1, 8):
        if chessboard[queens[qp].initial_position[0]][right] == 0:
            chessboard[queens[qp].initial_position[0]][right] = 'Q'
            collisions_found = find_collisions(chessboard)
            #print_search(chessboard),
   #         print 'collisions=',collisions_found
            chessboard[queens[qp].initial_position[0]][right] = 0
            if collisions_found <= current_collisions_number:
                queens[qp].possible_collisions.append(collisions_found)
                queens[qp].possible_moves.append([queens[qp].initial_position[0], right]) #store final position of queen
        elif chessboard[queens[qp].initial_position[0]][right] != 0: #8a spasei an pesei se allo kommati
            break
    #print '\n############down right'
    for down, right in zip(range(queens[qp].initial_position[0]+1, 8), range(queens[qp].initial_position[1]+1, 8)):
        if chessboard[down][right] == 0:
            chessboard[down][right] = 'Q'
            collisions_found = find_collisions(chessboard)
            #print_search(chessboard),
     #       print 'collisions=',collisions_found
            chessboard[down][right] = 0
            if collisions_found <= current_collisions_number:
                queens[qp].possible_collisions.append(collisions_found)
                queens[qp].possible_moves.append([down, right]) #store final position of queen
        elif chessboard[down][right] != 0:
            break
    #print '\n##############down'
    for down in range(queens[qp].initial_position[0]+1, 8):
        if chessboard[down][queens[qp].initial_position[1]] == 0:
            chessboard[down][queens[qp].initial_position[1]] = 'Q'
            collisions_found = find_collisions(chessboard)
            #print_search(chessboard),
     #       print 'collisions=',collisions_found
            chessboard[down][queens[qp].initial_position[1]] = 0
            if collisions_found <= current_collisions_number:
                queens[qp].possible_collisions.append(collisions_found)
                queens[qp].possible_moves.append([down, queens[qp].initial_position[1]]) #store final position of queen
        elif chessboard[down][queens[qp].initial_position[1]] != 0:
            break
#    print '\n##############down left'
    for down, left in zip(range(queens[qp].initial_position[0]+1, 8), range(queens[qp].initial_position[1]-1, -1, -1 ) ):
        if chessboard[down][left] == 0:
            chessboard[down][left] = 'Q'
            collisions_found = find_collisions(chessboard)
            #print_search(chessboard),
            #print 'collisions=',collisions_found
            chessboard[down][left] = 0
            if collisions_found <= current_collisions_number:
                queens[qp].possible_collisions.append(collisions_found)
                queens[qp].possible_moves.append([down, left]) #store final position of queen
        elif chessboard[down][left] != 0 :
            break
#    print '\n#################left '
    for left in range(queens[qp].initial_position[1]-1, -1, -1 ):
        if chessboard[queens[qp].initial_position[0]][left] == 0:
            chessboard[queens[qp].initial_position[0]][left] = 'Q'
            collisions_found = find_collisions(chessboard)
            #print_search(chessboard),
            #print 'collisions=',collisions_found
            chessboard[queens[qp].initial_position[0]][left] = 0
            if collisions_found <= current_collisions_number:
                queens[qp].possible_collisions.append(collisions_found)
                queens[qp].possible_moves.append([queens[qp].initial_position[0], left])
        elif chessboard[queens[qp].initial_position[0]][left] != 0:
            break
#    print '\n############up left'
    for up, left in zip(range(queens[qp].initial_position[0]-1, -1, -1), range(queens[qp].initial_position[1]-1, -1, -1)):
        if chessboard[up][left] == 0:
            chessboard[up][left] = 'Q'
            collisions_found = find_collisions(chessboard)
 #           print_search(chessboard),
  #          print 'collisions=',collisions_found
            chessboard[up][left] = 0
            if collisions_found <= current_collisions_number:
                queens[qp].possible_collisions.append(collisions_found)
                queens[qp].possible_moves.append([up, left])
        elif chessboard[up][left] != 0:
            break
    queens[qp].choose_random_move()

def knight_move(chessboard, current_collisions_number, knights, knight_coor):
    chessboard[knight_coor[0]][knight_coor[1]] = 0 #delete from original position
    kp = -1
    for k in range(len(knights)):
        if knights[k].initial_position == knight_coor:
            kp = k
   # print '\n#############up right'
    for up,right in zip(range(knights[kp].initial_position[0]-1, -1, -1), range(knights[kp].initial_position[1]+1, 8)):
        if chessboard[up][right] == 0:
            chessboard[up][right] = 'K'
            collisions_found = find_collisions(chessboard)
     #       print_search(chessboard),
    #        print 'collisions=',collisions_found
            chessboard[up][right] = 0
            if collisions_found <= current_collisions_number:
                knights[kp].possible_collisions.append(collisions_found)
                knights[kp].possible_moves.append([up,right])
        elif chessboard[up][right] != 0:
            break
#    print '\n#############down right'
    for down, right in zip(range(knights[kp].initial_position[0]+1, 8), range(knights[kp].initial_position[1]+1, 8)):
        if chessboard[down][right] == 0:
            chessboard[down][right] = 'K'
            collisions_found = find_collisions(chessboard)
 #           print_search(chessboard),
  #          print 'collisions=',collisions_found
            chessboard[down][right] = 0
            if collisions_found <= current_collisions_number:
                knights[kp].possible_collisions.append(collisions_found)
                knights[kp].possible_moves.append([down, right])
        elif chessboard[down][right] != 0:
            break
   # print '\n############down left'
    for down, left in zip(range(knights[kp].initial_position[0]+1, 8), range(knights[kp].initial_position[1]-1, -1, -1 ) ):
        if chessboard[down][left] == 0:
            chessboard[down][left] = 'K'
            collisions_found = find_collisions(chessboard)
    #        print_search(chessboard),
     #       print 'collisions=',collisions_found
            chessboard[down][left] = 0
            if collisions_found <= current_collisions_number:
                knights[kp].possible_collisions.append(collisions_found)
                knights[kp].possible_moves.append([down, left])
        elif chessboard[down][left] != 0:
            break
#    print '\n#############up left '
    for up, left in zip(range(knights[kp].initial_position[0]-1, -1, -1), range(knights[kp].initial_position[1]-1, -1, -1)):
        if chessboard[up][left] == 0:
            chessboard[up][left] = 'K'
            collisions_found = find_collisions(chessboard)
 #           print_search(chessboard),
  #          print 'collisions=',collisions_found
            chessboard[up][left] = 0
            if collisions_found <= current_collisions_number:
                knights[kp].possible_collisions.append(collisions_found)
                knights[kp].possible_moves.append([up, left])
        elif chessboard[up][left] != 0:
            break
    knights[kp].choose_random_move()

def choose_one(queens, knights, total_collisions):
    tmp_move_q = []
    tmp_move_k = []
    tmp_pos_q = []
    tmp_pos_k = []
    for q in range(len(queens)):
        if queens[q].final_collisions < total_collisions:
            tmp_move_q.append(queens[q].final_position)
            tmp_pos_q.append(queens[q].initial_position)
    for k in range(len(knights)):
        if knights[k] < total_collisions:
            tmp_move_k.append(knights[k].final_position)
            tmp_pos_k.append(knights[k].initial_position)
    if len(tmp_move_q) > 0 and len(tmp_move_k) == 0: #queen move found
        rnd = randint(0, len(tmp_move_q)-1)
        return tmp_move_q[rnd], tmp_pos_q[rnd]
    elif len(tmp_move_k) > 0 and len(tmp_move_q) == 0: #knight move found
        rnd = randint(0, len(tmp_move_k)-1)
        return tmp_move_k[rnd], tmp_pos_k[rnd]
    elif len(tmp_move_q) > 0 and len(tmp_move_k) > 0:
        if randint(0,1) == 0: #random of random of random
            rnd = randint(0, len(tmp_move_q)-1)
            return tmp_move_q[rnd], tmp_pos_q[rnd]
        else:
            rnd = randint(0, len(tmp_move_k)-1)
            return tmp_move_k[rnd], tmp_pos_k[rnd]
    #equal collisions
    if len(tmp_move_q)==0 and len(tmp_move_k)==0:
        for q in range(len(queens)):
            if queens[q] == current_collisions_number:
                tmp_move_q.append(queens[q].final_position)
        for k in range(len(knights)):
            if knights[k] == current_collisions_number:
                tmp_move_k.append(knights[k].final_position)
    if len(tmp_move_q) > 0 and len(tmp_move_k) == 0: #queen move found
        rnd = randint(0, len(tmp_move_q)-1)
        return tmp_move_q[rnd], tmp_pos_q[rnd]
    elif len(tmp_move_k) > 0 and len(tmp_move_q) == 0: #knight move found
        rnd = randint(0, len(tmp_move_k)-1)
        return tmp_move_k[rnd], tmp_pos_k[rnd]
    elif len(tmp_move_q) > 0 and len(tmp_move_k) > 0:
        if randint(0,1) == 0: #random of random of random
            rnd = randint(0, len(tmp_move_q)-1)
            return tmp_move_q[rnd], tmp_pos_q[rnd]
        else:
            rnd = randint(0, len(tmp_move_k)-1)
            return tmp_move_k[rnd], tmp_pos_k[rnd]
    #no smaller or equal collisions moves found
    #so you are in local minimum. Optimal found
    #TERMINATING
    if len(tmp_move_q) == 0 and len(tmp_move_k) == 0:
        print 'minimum found\n#########TERMINATING########'
        sys.exit()

def update(move_from, move_to, knights, queens, chessboard):
    for k in range(len(knights)):
        if knights[k].initial_position == move_from:
   #         print 'move k to ',move_to
            knights[k].initial_position = move_to
            chessboard[move_from[0]][move_from[1]] = 0
            chessboard[move_to[0]][move_to[1]] = 'K'
            break
    for q in range(len(queens)):
        if queens[q].initial_position == move_from:
    #        print 'move q to ',move_to
            queens[q].initial_position = move_to
            chessboard[move_from[0]][move_from[1]] = 0
            chessboard[move_to[0]][move_to[1]] = 'Q'
            break
    return chessboard

def cleanup(queens, knights):
    for q in range(len(queens)):
        queens[q].clean_stats()
    for k in range(len(knights)):
        knights[k].clean_stats()
    return queens, knights

def print_board(chessboard):
    for i in range(8):
        for j in range(8):
            if chessboard[i][j] == 'Q':
                print colored(chessboard[i][j], 'green', 'on_blue', ['bold']),
                #print chessboard[i][j],
            elif chessboard[i][j] == 'K':
                print colored(chessboard[i][j], 'red', 'on_white', ['bold']),
                #print chessboard[i][j],
            else:
                print chessboard[i][j],
            if j==7:
                print ' '

def print_search(chessboard):
    for i in range(8):
        for j in range(8):
            if chessboard[i][j] == 'Q':
                #print colored(chessboard[i][j], 'green', 'on_blue', ['bold']),
                print chessboard[i][j],
            elif chessboard[i][j] == 'K':
                #print colored(chessboard[i][j], 'red', 'on_white', ['bold']),
                print chessboard[i][j],
            else:
                print chessboard[i][j],
            if j==7:
                print ' '
    print ''
#    return ','

#################################################################################################
#remind me to make this a main function if i'm not bored
def main(chessboard, sideways_moves):
    print 'GREEDY HILL CLIMB WITH RESTARTS'
    queens = []
    knights = []
    no_of_moves = 0
    for i in range(8): #create the queen instanse and learn initial position
        for j in range(8):
            if chessboard[i][j] == 'Q':
                queens.append(queen(i,j))
            elif chessboard[i][j] == 'K':
                knights.append(knight(i,j))


    #compute collisions number here
    current_collisions_number = find_collisions(chessboard)

    if current_collisions_number == 0:
        print 'solution found'
        sys.exit()
    #everything works until here DO NOT TOUCH
    print 'initial collisions number ',current_collisions_number
    print_board(chessboard)
    print '\n\nbegin pocess\n'


    solution_flag = False

    while solution_flag != True:
        no_of_moves = no_of_moves + 1
        for i in range(8):
            for j in range(8):
                if chessboard[i][j] == 'Q':
                    #print '\nprocessing queen position ',i,j
                    queen_move(chessboard, current_collisions_number, queens, [i,j]) #that or use global in function
                    chessboard[i][j] = 'Q'
                    #print '\noptimal position for queen \n', final_queen_position[0],final_queen_position[1]
                    #print_board(chessboard)

                elif chessboard[i][j] == 'K':
                    #print '\nprocessing knight position ',i,j
                    knight_move(chessboard, current_collisions_number, knights, [i,j]) #or use global in function
                    chessboard[i][j] = 'K'
                    #print '\noptimal position for knight  \n',final_knight_position[0], final_knight_position[1]
                    #print_board(chessboard)

        #print 'comparing and moving'
        #make compares. now we deside which move is best and if its sideways move
        move_to, move_from = choose_one(queens, knights, current_collisions_number)
        prev_chessboard = chessboard

        ########################TEMPORARY ENTRY TO PREVENT LOCAL MINIMUMS##########################
        ########################DONT DELETE IF WORKS#########################
        if len(move_to) == 0:
            print 'no possible moves\n restarting'
            print_board(chessboard)
            print 'no of moves ',no_of_moves
            return False, no_of_moves, find_collisions(chessboard)
        ###########################################################################################

        chessboard = update(move_from, move_to, knights, queens, chessboard)
        
        new_collision_number = find_collisions(chessboard)
        if current_collisions_number == new_collision_number:
            sideways_moves = sideways_moves - 1
            if sideways_moves == -1:#out of sideways moves
                print 'out of sideways moves\n restarting'
                return False, no_of_moves, find_collisions(chessboard)
        current_collisions_number = new_collision_number
        if current_collisions_number == 0:
            print 'solved'
            solution_flag = True
        cleanup(queens, knights)
        
        #print_board(chessboard)

    print '\ni\'m tired'
    print 'final chessboard'
    print_board(chessboard)
    print '\nnumber of moves ',no_of_moves,'\nsideways moves ',sideways_moves,'\nfinal collisions ', find_collisions(chessboard)
    return True, no_of_moves, find_collisions(chessboard)
if __name__ == "__main__":
    main(chessboard, sideways_moves)
