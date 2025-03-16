import networkx as nx
import scipy.io
import numpy as np

# Load the MTX file
mtx_file_path = "your_file.mtx"  # Replace with your actual file path
matrix = scipy.io.mmread(mtx_file_path)

# Convert the matrix to a NetworkX graph
G = nx.from_scipy_sparse_array(matrix)

def print_properties():

    # Degree of a Node: The number of edges connected to a node.
    # Interpretation: A node's degree represents how many friends a person has on facebook; so we calculate:
    #  - the lowest number of friends
    #  - the highest number of friends
    #  - the average number of friends
    degrees = [d for _, d in G.degree()]
    min_degree = np.min(degrees)
    max_degree = np.max(degrees)
    avg_degree = np.mean(degrees)

    # Connected Component: A group of nodes that are connected by paths.
    # The connected components can indicate if the network is one big cluster or composed of small ones.
    # Interpretation: Groups of friends isolated or interconnected.
    connected_components = list(nx.connected_components(G))
    num_connected_components = len(connected_components)
    largest_component_size = max(len(c) for c in connected_components)

    # Diameter: longest unique path.
    # Interpretation: the longest "friendship chain" connecting two users.
    largest_cc = G.subgraph(max(connected_components, key=len))
    diameter = nx.diameter(largest_cc) if nx.is_connected(largest_cc) else None

    # Clustering Coefficient: Measures how tightly connected a node’s neighbors are.
    # Interpretation: How interconnected are on average the users. High clustering means high interaction between the friends of an user.
    avg_clustering = nx.average_clustering(G)

    # Shortest path: minimum number of edges required to travel from one node to another.
    # Interpretation: The degree of separation between two users measured in friendships. 
    shortest_paths = dict(nx.all_pairs_shortest_path_length(largest_cc))
    avg_shortest_path_length = np.mean([dist for paths in shortest_paths.values() for dist in paths.values()])

    # Print results
    print("Network Properties:")
    print(f"Min Degree: {min_degree}")
    print(f"Max Degree: {max_degree}")
    print(f"Average Degree: {avg_degree}")
    print(f"Number of Connected Components: {num_connected_components}")
    print(f"Largest Component Size: {largest_component_size}")
    print(f"Diameter (of largest component): {diameter}")
    print(f"Average Clustering Coefficient: {avg_clustering}")
    print(f"Average Shortest Path Length: {avg_shortest_path_length}")
