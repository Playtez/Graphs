from graph import Graph
from util import Stack, Queue  # These may come in handy


def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    # PSUEDOCODE:
    # import Graph
    # iterate through the array or ancestors
    for tuple_ in ancestors:
        # make a dictionary/ or some how find a way to add connected vertex
        # how do i creat each vertex?
        # if the tuple_ is not already in the vertices
        if tuple_[0] not in g.vertices:
            # add each tyuple_[0] to graph vertex
            g.add_vertex(tuple_[0])
        if tuple_[1] not in g.vertices:
            g.add_vertex(tuple_[1])

    for linked_pair in ancestors:
        # index of 0 in each tuple would be the v1 in add_edge
        # index of 1 in same tuple would be the v2 in add egde
        # make sure all edges are added
        g.add_edge(linked_pair[0], linked_pair[1])

    all_paths = []
    # implement the vertex
    for vertex in g.vertices:
        dfs_call = g.dfs(vertex, starting_node)
        if dfs_call is not None:
            if len(dfs_call) > len(all_paths):
                all_paths = dfs_call
            elif len(dfs_call) == len(all_paths):
                if dfs_call[0] < all_paths[0]:
                    all_paths = dfs_call

    # needs to return in order to

    if len(all_paths) == 0:
        return -1

    return all_paths[0]

    # CONDITIONALS
    # if there is more than one earliest ancestor
    #   # return the min value of the nodes in question
    # if input aka start_node has no parents:
    #   # return the value of -1
