import os
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import scipy.io


G1 = nx.read_edgelist


for file in os.scandir("networks"): # .venv in root dir
    # load the mtx file
    matrix = scipy.io.mmread(file.path)

    # convert the matrix to a NetworkX graph
    G = nx.from_scipy_sparse_array(matrix)

    # calculate
    print(file.name)
    fig=plt.figure(figsize=(8,8))
    nx.draw_spring(G, node_size=40)
    plt.show()
    
    print(end="\n\n")