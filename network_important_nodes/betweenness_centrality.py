import os
import networkx as nx
import scipy.io

def compute_and_display_betweenness_centrality(G, graph_name):
# -------------------------------------------
#  Betweenness centrality measures how often a node lies
# on the shortest paths between other nodes. High values
# indicate "bridge" nodes that can control communication
# across the network.
# -------------------------------------------

    print(f"\n=== {graph_name} ===")

    # Compute betweenness centrality for each node
    betweenness = nx.betweenness_centrality(G)

    # Sort nodes by betweenness centrality (descending)
    bc_sorted = sorted(betweenness.items(), key=lambda item: item[1], reverse=True)

    print("Top 5 nodes by Betweenness Centrality:")
    for i in range(5):
        node, centrality = bc_sorted[i]
        print(f"Node {node}: {centrality:.4f}")

def read_graph(file_path):
    
    matrix = scipy.io.mmread(file_path)
    G = nx.from_scipy_sparse_array(matrix)
    mapping = {node: i for i, node in enumerate(G.nodes())}
    return nx.relabel_nodes(G, mapping)

network_dir = "./networks"
for file in os.scandir(network_dir):
    if file.name.endswith(".mtx"):
        G = read_graph(file.path)
        compute_and_display_betweenness_centrality(G, file.name)
