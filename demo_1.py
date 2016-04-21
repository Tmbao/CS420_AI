import sys
import math
import networkx as nx
import timeit

from graph_algorithms import *
import graph_drawer

token_id = None
tokens = None


def demo(run_algorithm, input_nodes, input_edges, source, target, output_image_file):
    global token_id
    global tokens

    def read_entire_file(file_name):
        with open(file_name, 'r') as file:
            content = file.read()
        return content.split()

    tokens = read_entire_file(input_nodes)
    token_id = -1

    def next_token():
        global token_id
        global tokens

        token_id += 1
        if token_id < len(tokens):
            return tokens[token_id]
        else:
            return None

    graph = nx.Graph()

    id = {}
    names = []
    n_vertices = 0
    hf = []
    while token_id + 1 < len(tokens):
        node_name = next_token()
        names.append(node_name)
        id[node_name] = n_vertices
        hf.append(float(next_token()))
        n_vertices += 1

        graph.add_node(id[node_name], name=node_name)

    tokens = read_entire_file(input_edges)
    token_id = -1

    # add edges
    while token_id + 1 < len(tokens):
        u = id[next_token()]
        v = id[next_token()]
        c = float(next_token())

        graph.add_edge(u, v, len=c)
        graph.add_edge(v, u, len=c)

    source = id[source]
    target = id[target]

    attr_name = nx.get_node_attributes(graph, 'name')

    print 'Running {} algorithm'.format(run_algorithm)
    start_time = timeit.default_timer()

    if run_algorithm == 'Astar':
        def heuristic_hardcoded(cur_node, target):
            return hf[cur_node]

        algo = AstarAlgorithm(heuristic_func=heuristic_hardcoded)
    elif run_algorithm == 'HillClimbing':
        algo = HillClimbingAlgorithm()
    elif run_algorithm == 'DFS':
        algo = DFSAlgorithm()

    distance, path = algo.get_path(graph, source, target)
    finish_time = timeit.default_timer()

    print 'Finished in {}'.format(finish_time - start_time)
    if distance is None:
        print 'The path does not exist!'
    else:
        print 'Found distance: {}'.format(distance)
        print 'Path: '
        print names[source],
        for edge in path:
            (u, v) = edge
            print '-> {}'.format(names[v]),
        # if output_image_file:
            # graph_drawer.plot(output_image_file, graph, source, target, path)
            # print 'Visualization image was written to {}'.format(output_image_file)

if __name__ == "__main__":
    run_algorithm = 'Astar'
    output_image_file = None

    argc = len(sys.argv)
    if argc >= 2:
        run_algorithm = sys.argv[1]
    if argc >= 3:
        input_nodes = sys.argv[2]
    if argc >= 4:
        input_edges = sys.argv[3]
    if argc >= 5:
        source = sys.argv[4]
    if argc >= 6:
        target = sys.argv[5]
    if argc >= 7:
        output_image_file = sys.argv[6]

    demo(run_algorithm, input_nodes, input_edges, source, target, output_image_file)
