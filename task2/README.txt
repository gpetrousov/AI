Graph coloring problem solved by Min-conflicts and Tabu search algorithms written in python2 by Giannis Petrousov. This was 
an essay for the class Artificial Intelligence.

The program reads the graphs from the graphs file and. The first number in the first line tells how many colors are available and
the rest of the numbers are the colors. The second line tells how many nodes are in the graph. The third line tells how many edges
there are in the graph. The rest of the lines contain the connecting nodes. For example 0 19 <> means that node 0 is connected
with node 19, the "<>" is omitted. Note that the graphs were already provided, I did not generate them. 

In the beginning random colors are given to all the nodes.

starter.py
This runs all the functions in sequential order.

minconflicts.py
Implements the Min-conflicts algorithm.

tabu.py
Implements the Tabu search algorithm.
