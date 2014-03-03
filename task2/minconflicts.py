"""min-conflicts compiled by Giannis Petrousov"""

import os
import copy
import random

def main():
    no_restarts = input("enter number of restarts ")
    no_repeats = input("enter number of repeats ")
    for filez in os.listdir('graphs'):
        #print os.listdir('graphs')
        print 'solving ', filez
        connection_graph, color_graph, max_color = create_graphs(filez) #will create the original graph
        for restarts in range(0, no_restarts):
            print 'initial color_graph ', color_graph
            rt = solve(no_repeats, connection_graph, color_graph, max_color)
            if( rt == True):
                print 'solved'
                break
            elif(rt == False):
                print 'NOT solved'
            else:
                print 'has no idea'
            #if(restarts < (no_repeats - 1)):
            #    print restarts
            #    print 'restarting'
        #break#this is just a test case, remove to test all filez

def find_total_collisions(connection_graph, color_graph):
    no_collisions = 0
    colliding = list()
    for node in range(len(color_graph) - 1):
        for j in range(node + 1, len(color_graph)):
            #print 'node=',node,'j=',j,'link=',connection_graph[node][j],'colornode=',color_graph[node],'colorJ=',color_graph[j]
            if(connection_graph[node][j] == 1):
                if(color_graph[node] == color_graph[j]):
                    no_collisions += 1
                    #print 'node ', node, 'collides with ',j
                    colliding.append(node) #nodes that collide
    return no_collisions, colliding

def solve(no_repeats, connection_graph, color_graph, max_color):#function that controls the solution progress
    no_changes = 0
    for repeats in range(0, no_repeats):
        no_total_collisions, colliding_nodes = find_total_collisions(connection_graph, color_graph)
        print 'no_total_collisions ', no_total_collisions
        if(no_total_collisions == 0):
            print 'solution found'
            return True
        #else try to solve it
        random_node = colliding_nodes[random.randint(0, len(colliding_nodes) - 1)] #choose random node
        print 'random_node ', random_node

        #t_conn_graph = deepcopy(connection_graph)
        t_colr_graph = copy.deepcopy(color_graph)
        for all_colors in range(0, max_color): #try every possible color
            print 'all_colors ', all_colors
            t_colr_graph[random_node] = all_colors #change its color
            t_no_collisions, colliding_nodes = find_total_collisions(connection_graph, t_colr_graph)
            print 't_no_collisions ', t_no_collisions
            if(t_no_collisions < no_total_collisions):
                no_total_collisions = t_no_collisions #new collisions number
                no_changes += 1
                color_graph = copy.deepcopy(t_colr_graph)
                if(no_total_collisions == 0):
                    print 'final color graph ', color_graph
                    print 'final collisions ', find_total_collisions(connection_graph, color_graph)[0]
                    print 'changes ',no_changes
                    return True
        if(repeats + 1 == no_repeats):
            print 'changes ',no_changes
            print 'best solution\n',color_graph
            return False
        
def create_graphs(filez): #create the original graph
    fd = open('graphs/'+filez, 'r')
    max_color = int(fd.readline().split().pop(0)) #get colors
    #print 'max color ', max_color
    size = fd.readline() #returns tuple
    #print 'size ', size
    connection_graph = [[-1 for i in range(int(size))] for i in range(int(size))] #just another way to declare list 
    color_graph = list(-1 for i in range(int(size)))
    fd.readline() #miss the next one
    for l in fd:
        #print int(l.split()[0]), int(l.split()[1])
        connection_graph[int(l.split()[0])][int(l.split()[1])] = 1 #there is connection
    for i in range(len(color_graph)):
        color_graph[i] = random.randint(0, max_color) #input random color 
    return connection_graph, color_graph, max_color

if __name__ == '__main__':
    main()
