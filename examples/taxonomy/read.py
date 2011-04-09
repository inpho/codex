import networkx as nx

def build_graph(filename):
    f = open(filename)
    f = f.read()
    
    regex = re.compile("[ins|isa]\(i(\d+),i(\d+)\)")
    regex_class = re.compile("class\(i(\d+)\)")
    
    instances = frozenset(regex.findall(f))
    classes = frozenset(regex_class.findall(f))
    
    # create directed graph on the instances
    G = nx.DiGraph()
    G.add_edges_from(instances)

    return G
