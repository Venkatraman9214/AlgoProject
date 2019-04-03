import networkx as nx
import numpy as np
#import matplotlib
#1 call MST
#2 assign each edge of MST with a weight of ceil{(eucledean distance)/Physcal Range between the nodes -1
#3 check if cost is less than B --> minimum cost returned will give minimum number of nodes for the network.
#4 If value greater than B, delete the edges arbitrarily

M=5
weight= 3
G=nx.cycle_graph(4)

tupxy =('0,0','1,1','2,2','3,3')
G.add_edge(0,3,weight=2)
T= nx.minimum_spanning_tree(G)
print(T.edges(data=True))

print (tupxy[0]);
for i in tupxy and G:
    cordlist= (tupxy[i],G[i])
    print (cordlist[1])

#nx.draw(G)