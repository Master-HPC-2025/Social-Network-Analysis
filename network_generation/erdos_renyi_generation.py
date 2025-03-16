import networkx as nx
from scipy.io import mmwrite

# Parameters based on socfb-Reed98 dataset
n = 962               # Number of nodes
# Using the provided average degree of 39, the approximate number of edges:
E = int(n * 39 / 2)   # Approximately 18759 edges

# --- Create Erdős–Rényi Graph ---
# For an undirected graph, the edge probability p is given by:
#    p = (2E) / [n * (n - 1)]
p = (2 * E) / (n * (n - 1))
print(f"Erdős–Rényi model: n = {n}, E ≈ {E}, p = {p:.5f}")

G_er = nx.erdos_renyi_graph(n, p)
print(f"Created Erdős–Rényi graph with {G_er.number_of_nodes()} nodes and {G_er.number_of_edges()} edges.")

# Save the Erdős–Rényi graph as a Matrix Market (.mtx) file in pattern format (undirected, unweighted)
er_file = "networks/socfb-Reed98_ER.mtx"
mmwrite(er_file, nx.to_scipy_sparse_array(G_er), field="pattern", symmetry="symmetric")
print(f"Erdős–Rényi graph saved to '{er_file}'")
