import networkx as nx
import matplotlib.pyplot as plt
import scipy

matrix = scipy.io.mmread("networks\socfb-Reed98_ER.mtx")

    # convert the matrix to a NetworkX graph
G = nx.from_scipy_sparse_array(matrix)

# 1. Degree Distribution
degrees = [d for n, d in G.degree()]
plt.figure()
plt.hist(degrees, bins=range(1, max(degrees)+2), edgecolor='black')
plt.title("Degree Distribution")
plt.xlabel("Degree")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# 2. Clustering Coefficient Distribution
clustering_coeffs = list(nx.clustering(G).values())
plt.figure()
plt.hist(clustering_coeffs, bins=10, edgecolor='black')
plt.title("Clustering Coefficient Distribution")
plt.xlabel("Clustering Coefficient")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# 3. Betweenness Centrality Distribution
betweenness = list(nx.betweenness_centrality(G).values())
plt.figure()
plt.hist(betweenness, bins=10, edgecolor='black')
plt.title("Betweenness Centrality Distribution")
plt.xlabel("Betweenness Centrality")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# 4. Connected Components Size Distribution
component_sizes = [len(c) for c in nx.connected_components(G)]
plt.figure()
plt.hist(component_sizes, bins=range(1, max(component_sizes)+2), edgecolor='black', align='left')
plt.title("Connected Components Size Distribution")
plt.xlabel("Component Size")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

