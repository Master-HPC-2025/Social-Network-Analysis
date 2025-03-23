import os
import networkx as nx
import scipy.io

def compute_and_display_eigenvector_centrality(G, graph_name):
# -------------------------------------------
# Eigenvector centrality reflects not just the number
# of connections a node has, but how important those
# neighbors are. High values indicate influence.
#
# Note: Computation may fail to converge on large or
# complex networks — we handle that with a try/except block.
# -------------------------------------------

    print(f"\n=== {graph_name} ===")
    
    try:
        # Compute eigenvector centrality (uses power iteration)
        eigenvector = nx.eigenvector_centrality(G, max_iter=1000)

        # Sort nodes by centrality in descending order
        ev_sorted = sorted(eigenvector.items(), key=lambda item: item[1], reverse=True)

        print("Top 5 nodes by Eigenvector Centrality:")
        for i in range(5):
            node, centrality = ev_sorted[i]
            print(f"Node {node}: {centrality:.4f}")

    # Handle non-convergence or errors
    except nx.NetworkXError as e:
        print(f"⚠️ Could not compute eigenvector centrality for {graph_name}: {e}")

def read_graph(file_path):
    
    matrix = scipy.io.mmread(file_path)
    G = nx.from_scipy_sparse_array(matrix)
    mapping = {node: i for i, node in enumerate(G.nodes())}
    return nx.relabel_nodes(G, mapping)

network_dir = "./networks"
for file in os.scandir(network_dir):
    if file.name.endswith(".mtx"):
        G = read_graph(file.path)
        compute_and_display_eigenvector_centrality(G, file.name)
