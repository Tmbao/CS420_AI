import sys
import math
import networkx as nx
import timeit

from graph_algorithms import *
import graph_drawer

token_id = None
tokens = None


def demo(run_algorithm, input_file, output_image_file):
    global token_id
    global tokens

    def read_entire_file(file_name):
        with open(file_name, 'r') as file:
            content = file.read()
        return content.split()

    tokens = read_entire_file(input_file)
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

    # add nodes
    n_nodes = int(next_token())
    for i in range(n_nodes):
        node_id = int(next_token())
        node_name = next_token()
        node_lat = int(next_token())
        node_lng = int(next_token())

        graph.add_node(node_id, name=node_name, lat=node_lat, lng=node_lng)

    # add edges
    n_edges = int(next_token())
    for i in range(n_edges):
        u = int(next_token())
        v = int(next_token())
        c = float(next_token())

        graph.add_edge(u, v, len=c)

    source = int(next_token())
    target = int(next_token())

    attr_lat = nx.get_node_attributes(graph, 'lat')
    attr_lng = nx.get_node_attributes(graph, 'lng')
    attr_name = nx.get_node_attributes(graph, 'name')

    print 'Running {} algorithm'.format(run_algorithm)
    start_time = timeit.default_timer()

    if run_algorithm == 'Astar':
        def heuristic_l2_func(cur_node, target):
            return math.sqrt((attr_lat[cur_node] - attr_lat[target]) ** 2 + (attr_lng[cur_node] - attr_lng[target]) ** 2)

        def heuristic_l1_func(cur_node, target):
            return abs(attr_lat[cur_node] - attr_lat[target]) + abs(attr_lng[cur_node] - attr_lng[target])

        algo = AstarAlgorithm(heuristic_func=heuristic_l1_func)
    elif run_algorithm == 'UCS':
        algo = UCSAlgorithm()
    elif run_algorithm == 'BFS':
        algo = BFSAlgorithm()

    distance, path = algo.get_path(graph, source, target)
    finish_time = timeit.default_timer()

    print 'Finished in {}'.format(finish_time - start_time)
    if distance is None:
        print 'The path does not exist!'
    else:
        print 'Found distance: {}'.format(distance)
        # print 'Path: {}'.format(path)
        if output_image_file:
            graph_drawer.plot(output_image_file, graph, source, target, path)
            print 'Visualization image was written to {}'.format(output_image_file)

if __name__ == "__main__":
    run_algorithm = 'Astar'
    input_file = 'demo_map.txt'
    output_image_file = 'demo.png'

    argc = len(sys.argv)
    if argc >= 2:
        run_algorithm = sys.argv[1]
    if argc >= 3:
        input_file = sys.argv[2]
    if argc >= 4:
        output_image_file = sys.argv[3]
    demo(run_algorithm, input_file, output_image_file)
