import os
import networkx as nx
import scipy.io

def compute_and_display_degree_centrality(G, graph_name): 
# -------------------------------------------
# Degree centrality measures how many direct connections
# a node has — useful for identifying popular or active nodes.
# -------------------------------------------

    print(f"\n=== {graph_name} ===")

    # Compute degree centrality for each node
    degree_centrality = nx.degree_centrality(G)

    # Sort nodes in descending order of centrality
    dc_sorted = sorted(degree_centrality.items(), key=lambda item: item[1], reverse=True)

    print("Top 5 nodes by Degree Centrality:")
    for i in range(5):
        node, centrality = dc_sorted[i]
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
        compute_and_display_degree_centrality(G, file.name)
