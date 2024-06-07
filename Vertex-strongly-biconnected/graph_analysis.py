import networkx as nx

def read_directed_graph(file_path):
    G = nx.DiGraph()
    with open(file_path) as file:
        for line in file:
            u, v = map(int, line.split())
            G.add_edge(u, v)
    return G

def is_strongly_connected(G):
    return nx.is_strongly_connected(G)

def make_undirected(G):
    return G.to_undirected()

def is_junction(G):
    for node in G.nodes:
        G_copy = G.copy()
        G_copy.remove_node(node)
        if not nx.is_biconnected(G_copy):
            return False
    return True

def test_directed_graph(file_path):
    G = read_directed_graph(file_path)
    
    if is_strongly_connected(G):
        print("Directed statement is powerful communication")
    else:
        print("The directive statement does not have a strong connection")
    
    G_undirected = make_undirected(G)
    
    if is_junction(G_undirected):
        print("An undirected statement is free of disjunctions.")
    else:
        print("The undirected statement contains articulated nodes")


SNAP_datasets = ["file1.txt", "file2.txt", "file3.txt"]
SNAP_directory = "path/to/SNAP/datasets/SNAP Datasets/"

for dataset in SNAP_datasets:
    file_path = SNAP_directory + dataset
    print("Read file:", file_path)
    test_directed_graph(file_path)
    print("---------------------")