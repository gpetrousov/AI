from random import randint

class queen():
    def __init__(self, row, col):
        self.initial_position = [row, col]
        self.piece = 'Q'
        self.possible_collisions = []
        self.possible_moves = []
        self.final_collisions = [] #this is just a test attr
        self.final_position = [] #only testing this one

    def choose_random_move(self):
        least_collisions_num = []
        least_collisions_move = []
        #print 'queen ',self.initial_position,' possible moves ', self.possible_moves,'\nwith collisions ',self.possible_collisions
            #all possible movies found. Now have to choose the best move for this queen
            #now follows a procedure to find the best move out of all available moves
        if len(self.possible_collisions) == 0: #no smallest collisions found
            return

        smallest_collision_number = min(self.possible_collisions)
        #print 'smallest collision num ',smallest_collision_number
        #gather all smallest
        least_collisions_num = []
        least_collisions_move = []
        for i in range(len(self.possible_collisions)):
         #   print 'i=',i
            if self.possible_collisions[i] == smallest_collision_number:
          #      print 'storing'
                least_collisions_num.append(self.possible_collisions[i])
                least_collisions_move.append(self.possible_moves[i])
                #print 'num ',least_collisions_num, 'move ',least_collisions_move

        rand_final = randint(0,len(least_collisions_num)-1)
        self.final_position = least_collisions_move[rand_final]
        self.final_collisions = least_collisions_num[rand_final]
        
    def clean_stats(self):
        self.final_position = []
        self.final_collisions = []
        self.possible_moves = []
        self.possible_collisions = []


class knight():
    def __init__(self, row, col):
        self.initial_position = [row, col]
        self.piece = 'K'
        self.possible_collisions = []
        self.possible_moves = []
        self.final_position = [] #only testing this one

    def choose_random_move(self):
        least_collisions_num = []
        least_collisions_move = []
        #print 'knight ',self.initial_position,' possible moves ', self.possible_moves,'\nwith collisions ',self.possible_collisions
            #all possible movies found. Now have to choose the best move for this queen
            #now follows a procedure to find the best move out of all available moves
        if len(self.possible_collisions) == 0: #no smallest collisions found
            return

        smallest_collision_number = min(self.possible_collisions)
#        print 'smallest collision num ',smallest_collision_number
        #gather all smallest
        least_collisions_num = []
        least_collisions_move = []
        for i in range(len(self.possible_collisions)):
 #           print 'i=',i
            if self.possible_collisions[i] == smallest_collision_number:
  #              print 'storing'
                least_collisions_num.append(self.possible_collisions[i])
                least_collisions_move.append(self.possible_moves[i])
                #print 'num ',least_collisions_num, 'move ',least_collisions_move

        rand_final = randint(0,len(least_collisions_num)-1)
        self.final_position = least_collisions_move[rand_final]
        self.final_collisions = least_collisions_num[rand_final]
        
    def clean_stats(self):
        self.final_position = []
        self.final_collisions = []
        self.possible_moves = []
        self.possible_collisions = []
