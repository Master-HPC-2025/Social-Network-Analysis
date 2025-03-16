import networkx as nx
from scipy.io import mmwrite

# Parameters based on socfb-Reed98 dataset
n = 962               # Number of nodes
# Using the provided average degree of 39, the approximate number of edges:
E = int(n * 39 / 2)   # Approximately 18759 edges

# --- Create Barabási–Albert Graph ---
# In the BA model, each new node attaches to m existing nodes.
# BA graphs have an average degree ≈ 2*m, so we choose m ≈ 20.
m = 20
G_ba = nx.barabasi_albert_graph(n, m)
print(f"Created Barabási–Albert graph with {G_ba.number_of_nodes()} nodes and {G_ba.number_of_edges()} edges.")

# Save the Barabási–Albert graph as a Matrix Market (.mtx) file in pattern format (undirected, unweighted)
ba_file = "networks/socfb-Reed98_BA.mtx"
mmwrite(ba_file, nx.to_scipy_sparse_array(G_ba), field="pattern", symmetry="symmetric")
print(f"Barabási–Albert graph saved to '{ba_file}'")
