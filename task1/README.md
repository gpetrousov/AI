## Greedy hill climbing algorithm written in python2. ##

###Usage###
Just run the lazy_bot.py and follow the prompts.

	python lazy_bot.py
Will run all the variations of the algorithm in sequential order.


###Files

**lazy_bot.py**
  
- This runs all the functions in sequential order.

**pieces_class.py**

- Contains the classes for the queens and knights.

**restarts.py**

- Greedy hill climbing with restarts.

**sideways.py**

- Greedy hill climbinb with sideways moves and restarts.
   
**stochastic.py**

- Greedy hill climbing with stochastic choices and restarts.


### How?

- In the beginning the program places in random positions the given number of queens and knights in an 8X8 chessboard.

- In each loop the move with the least number of collisions is chosen. 

- Might get stuck in local maximums.

About
=====

Author
--------------
- Original author: Giannis Petrousov
-  This was an essay for the class Artificial Intelligence.