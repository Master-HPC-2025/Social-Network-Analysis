import os
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import scipy.io

import networkx as nx
import scipy.io
import matplotlib.pyplot as plt
import networkx.algorithms.community as nx_comm

def read_matrix_market_graph(file_path):
    """ Reads an MTX file and converts it into a NetworkX graph with relabeled nodes """
    matrix = scipy.io.mmread(file_path)
    G = nx.from_scipy_sparse_array(matrix)

    # Relabel nodes to ensure continuous indexing
    mapping = {node: i for i, node in enumerate(G.nodes())}
    G = nx.relabel_nodes(G, mapping)
    
    return G

def visualize_network(G, file, layout_type="spring"):
    """Clusters the network and visualizes it with distinct colors"""
    
    # Clustering (grouping the nodes into comunities)
    communities = list(nx_comm.greedy_modularity_communities(G))
    color_map = {}
    for i, community in enumerate(communities):
        for node in community:
            color_map[node] = i
    colors = [color_map[node] for node in G.nodes()]

    layout_funcs = {
        "spring": nx.spring_layout,
        "kamada_kawai": nx.kamada_kawai_layout,
        "spectral": nx.spectral_layout,
        "shell": nx.shell_layout,
        "random": nx.random_layout,
        "planar": nx.planar_layout,
        "fruchterman_reingold": nx.fruchterman_reingold_layout
    }
    
    pos = layout_funcs.get(layout_type, nx.spring_layout)(G)

    fig = plt.figure(figsize=(10, 7))
    fig.canvas.manager.set_window_title(file.name)

    nx.draw(G, pos, node_color=colors, cmap=plt.get_cmap("tab10"), node_size=50, edge_color="gray", with_labels=False)
    plt.suptitle(f"{file.name} - {layout_type.capitalize()} Layout", fontsize=14, fontweight="bold")
    
    # plt.show()

    # Save the plots in Plots/ file.name
    # if this folder does not exists then it creates it
    directory = f"Plots/{file.name}"
    if not os.path.exists(directory):
        os.makedirs(directory)
 
    plt.savefig(f"{directory}/{file.name}-{layout_type.capitalize()} Layout.png")


for file in os.scandir("networks"): # .venv in root dir
    # load the mtx file
    matrix = scipy.io.mmread(file.path)

    # convert the matrix to a NetworkX graph
    G = nx.from_scipy_sparse_array(matrix)
    
    print(file.name)

    visualize_network(G, file, layout_type="spring")
    visualize_network(G, file, layout_type="shell")
    visualize_network(G, file, layout_type="random")
    visualize_network(G, file, layout_type="spectral")
    visualize_network(G, file, layout_type="kamada_kawai")
    visualize_network(G, file, layout_type="fruchterman_reingold")
    print(end="\n\n")