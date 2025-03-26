import os
import networkx as nx
import scipy.io

def compute_and_display_closeness_centrality(G, graph_name):   
# -------------------------------------------
# Closeness centrality indicates how close a node is
# to all other nodes in the network — useful for identifying
# nodes that can quickly spread or access information.
# -------------------------------------------

    print(f"\n=== {graph_name} ===")

    # Compute closeness centrality for each node
    closeness = nx.closeness_centrality(G)

    # Sort nodes in descending order of centrality
    cc_sorted = sorted(closeness.items(), key=lambda item: item[1], reverse=True)

    print("Top 5 nodes by Closeness Centrality:")
    for i in range(5):
        node, centrality = cc_sorted[i]
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
        compute_and_display_closeness_centrality(G, file.name)
