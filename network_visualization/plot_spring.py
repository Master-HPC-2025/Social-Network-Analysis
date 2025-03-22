import os
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import scipy.io

def draw_sping(G, file):
    print(file.name)
    fig=plt.figure(figsize=(8,8))
    nx.draw_spring(G, node_size=12)
    plt.show()
    #plt.savefig(f'spring_{file.name}.png')

def draw_circular(G, file):
    print(file.name)
    fig=plt.figure(figsize=(8,8))
    nx.draw_circular(G, node_size=12)
    #plt.savefig(f'spring_{file.name}.png')
    plt.show()

def draw_random(G, file):
    print(file.name)
    fig=plt.figure(figsize=(8,8))
    nx.random_layout(G)
    plt.show()
    #plt.savefig(f'spring_{file.name}.png')

def draw_spectral(G, file):
    print(file.name)
    fig=plt.figure(figsize=(8,8))
    nx.spectral_layout(G)
    plt.show()
    #plt.savefig(f'spring_{file.name}.png')

def draw_kamada_kawai(G, file):
    print(file.name)
    fig=plt.figure(figsize=(8,8))
    nx.kamada_kawai_layout(G)
    plt.show()


def draw_shell(G, file):
    print(file.name)
    fig=plt.figure(figsize=(8,8))
    nx.shell_layout(G)
    plt.show()

def draw_fruchterman_reingold(G, file):
    print(file.name)
    fig=plt.figure(figsize=(8,8))
    nx.fruchterman_reingold_layout(G)
    plt.show()

for file in os.scandir("networks"): # .venv in root dir
    # load the mtx file
    matrix = scipy.io.mmread(file.path)

    # convert the matrix to a NetworkX graph
    G = nx.from_scipy_sparse_array(matrix)
    draw_sping(G, file)
    
    print(end="\n\n")