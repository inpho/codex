"""
Taxonomy alignment.

Input: 2 taxonomies
Output: Networkx DiGraph

Taxonomy merge
Input: 2 taxonomies, DiGraph
Output: 1 taxonomy
"""

import networkx as nx

def empty_alignment(taxonomy_1, taxonomy_2, rename=('t1_', 't2_'):
    alignment_graph = nx.union(taxonomy_1, taxonomy_2, rename=rename)
    alignment_graph.remove_edges_from(alignment_graph.edges())
    return alignment_graph

def merge(taxonomy_1, taxonomy_2, alignment_graph, rename=('t1_', 't2_'):
    union_graph = nx.union(taxonomy_1, taxonomy_2, rename=rename)
    merge_graph = nx.compose(union_graph, alignment_graph)

    # reduction of merge_graph

    return merge_graph

