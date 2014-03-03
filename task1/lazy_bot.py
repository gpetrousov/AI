"""lazy bot to try them all"""
import restarts as skroutz_restarts #with restarts
import sideways as skroutz_sideways #with sideways moves
import stochastic as skroutz_stochastic #with stochastic choices
from random import randint
from copy import deepcopy

total_moves1 = total_moves2 = total_moves3 = 0
solved2 = False
solved3 = False
no_of_restarts = 0

number_of_pieces = input('enter number of pieces ') #number of queens and officers
sideways_moves = input('enter sideways moves ') #number of sideways moves
no_of_restarts = input('enter restart numbers ')#restarts and stochastic
no_of_repeats = input('enter repeats number ') #for stochastic only
no_of_instances = input('enter number of instances to be solved ')

instances = deepcopy(no_of_instances)
no_of_restarts_stochastic = deepcopy(no_of_restarts)
original_restarts = deepcopy(no_of_restarts)
total_collisions1 = 0
collisions1 = 0
total_collisions2 = 0
collisions2 = 0
collisions3 = 0
total_collisions3 = 0
total_solutions1 = total_solutions2 = total_solutions3 = 0

while no_of_instances != 0:
    moves1 = moves2 = moves3 = collisions1 = collisions2 = collisions3 = 0
    solved3 = solved2 = aa = False

    chessboard = [[0 for i in range(8) ] for i in range(8)] #lets say that this is the initial chessboard filled with zeros
    #REMINDER TO MAKE CHECKS IN CASE OF LARGE OR NEGATIVE INPUTS
    for i in range(number_of_pieces): #put the queens on the board
        posx = randint(0,7)
        posy = randint(0,7)
        while chessboard[posx][posy] != 0:
            posx = randint(0,7)
            posy = randint(0,7)
        chessboard[posx][posy] = 'Q'
    print 'done puttin queens'
    #print chessboard
    for i in range(number_of_pieces): #put the knights on the board
        posx = randint(0,7)
        posy = randint(0,7)
        while chessboard[posx][posy] != 0:
            posx = randint(0,7)
            posy = randint(0,7)
        chessboard[posx][posy] = 'K'
    print 'done putting knights'
    ############DONE####################

    #call greedy hill climb with sideways moves first
    moves1, collisions1, aa = skroutz_sideways.main(deepcopy(chessboard), sideways_moves)
    total_moves1 = total_moves1 + moves1
    total_collisions1 = total_collisions1 + collisions1
    if aa == True:
        total_solutions1 = total_solutions1 + 1
    #call greedy hill climb with restarts
    while solved2 == False and no_of_restarts != 0:
        solved2, moves2, collisions2 = skroutz_restarts.main(deepcopy(chessboard), sideways_moves)         
        no_of_restarts = no_of_restarts - 1
        total_moves2 = total_moves2 + moves2
        total_collisions2 = total_collisions2 + collisions2
        if solved2 == True:
            total_solutions2 = total_solutions2 + 1
    #call greedy hill climb with stochastic choices
    while solved3 == False and no_of_restarts_stochastic !=1:
        solved3, moves3, collisions3 = skroutz_stochastic.main(deepcopy(chessboard), sideways_moves, no_of_repeats)
        no_of_restarts_stochastic = no_of_restarts_stochastic - 1
        total_collisions3 = total_collisions3 + collisions3
        total_moves3 = total_moves3 + moves3
        if solved3 == True:
            total_solutions3 = total_solutions3 + 1
    no_of_restarts = original_restarts
    no_of_restarts_stochastic = original_restarts
    no_of_instances = no_of_instances - 1
print 'RESULTS'
print '\naverage moves1 %.2f'%(total_moves1/float(instances))
print 'average collisions1 %.2f'%(total_collisions1/float(instances))
print 'total solutions1 ',total_solutions1

print '\naverage moves2 %.2f'%(total_moves2/float(instances))
print 'average collisions2 %.2f'%(total_collisions2/float(instances))
print 'total solutions2 ',total_solutions2

print '\naverage moves3 %.2f'%(total_moves3/float(instances))
print 'average collisions3 %.2f'%(total_collisions3/float(instances))
print 'total solutions3 ',total_solutions3
