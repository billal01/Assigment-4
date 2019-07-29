#!/usr/bin/env python
# coding: utf-8

# In[1]:


import networkx as xy
import matplotlib.pyplot as plo
get_ipython().run_line_magic('matplotlib', 'inline')
# the graph
F = xy.Graph()
f = xy.generators.small.krackhardt_kite_graph()
print("Nodes of Krackhardt's graph: ","\n",f.nodes(),"\n")
print("Edges of krackhardt's graph: ","\n",f.edges())
person = {2:"Billal" ,5:"Hossain", 7:"Alim", 8:"Sawpon", 9:"Luna", 6:"Karim", 4:"Edward", 1:"Kamal", 3:"Jamal", 0:"Akmaal"}
person
#we are making  the graph object here
F1 =xy.Graph()
#----------making the Edges from the graph here
# first option we begins
a1 = [(0,1), (0,2), (0,3), (0,5), (1,3), (1,4), (1,6), (2,3), (2,5), (3,4), (3,5), (3,6), (4,6), (5,6), (5,7), (6,7), (7,8), (8,9)] #second option
a1 = f.edges()
# Adding all the edges to the graph object
F1.add_edges_from(a1)
print("Edges named for network","\n" ,F1.edges())
M = xy.relabel_nodes(F1, person)
print(" Nodes named for network: ", "\n", M.nodes()) 
print(" Edges named for network: ", "\n", M.edges())
xy.draw(M, with_labels =1)
plo.show()


# In[ ]:




