import heapq
import math

from graph import Node, Edge, Graph


class DijkstraAlgorithm(object):

    """
    This is an implementation of Dijkstra Shorest Path Algorithm 
    """


    @staticmethod
    def get_path(graph, node_start, node_destination):
        # The priority queue for dijkstra algorithm
        openset = []

        # We use a set to determine that a node has been visited or not 
        closeset = set()

        # We use a dictionary to store distance and track the edge going to a node 
        distance = {}
        for node in graph.adjacency_nodes:
            distance[node] = float('inf')

        trace = {}

        # We push the start node into the open set
        distance[node_start] = 0
        heapq.heappush(openset, (distance[node_start], node_start))

        while len(openset) > 0:
            current_distance, current_node = heapq.heappop(openset)
            
            if current_node in closeset:
                continue
            # Mark the current node
            closeset.add(current_node)

            if current_node is node_destination:
                path = []
                node = node_destination
                while True:
                    path.append(node)
                    if node is node_start:
                        break
                    node = trace[node].source
                return current_distance, reversed(path)
        
            # Iterate all adjacency nodes
            for edge in graph.adjacency_nodes[current_node]:
                target = edge.target

                # If this edge gets the current node to an unvisited node, we can update that node 
                if target not in closeset:
                    if distance[target] > current_distance + edge.data[Edge.LENGTH_TAG]:
                        distance[target] = current_distance + edge.data[Edge.LENGTH_TAG]
                        trace[target] = edge
                        heapq.heappush(openset, (distance[target], target))
                        
        return -1, None


class AstarAlgorithm(object):
    """
    This is an implementation of A-star algorithm
    """


    @staticmethod
    def get_path(graph, node_start, node_destination, heuristic):
        # The priority queue for A-star algorithm
        openset = []

        # We use a set to determine that a nodes has been visited or not
        closeset = set()

        # We use a dictionary to store distance and track the edge going to a node
        distance = {}
        for node in graph.adjacency_nodes:
            distance[node] = float('inf')

        trace = {}

        # We push the start node into the open set
        distance[node_start] = 0
        heapq.heappush(openset, (heuristic(node_start, node_destination), node_start))

        while len(openset) > 0:
            current_heuristic, current_node = heapq.heappop(openset)

            if current_node in closeset:
                continue
            # Mark the current node
            closeset.add(current_node)
            
            if current_node is node_destination:
                path = []
                node = node_destination
                while True:
                    path.append(node)
                    if node is node_start:
                        break
                    node = trace[node].source
                return distance[current_node], reversed(path)

            # Iterate all adjacency nodes 
            for edge in graph.adjacency_nodes[current_node]:
                target = edge.target
                
                # If this edge gets the current node to an unvisited node, we can update that node
                if target not in closeset:
                    if distance[target] > distance[current_node] + edge.data[Edge.LENGTH_TAG]:
                        distance[target] = distance[current_node] + edge.data[Edge.LENGTH_TAG]
                        trace[target] = edge
                        heapq.heappush(openset, (distance[target] + heuristic(target, node_destination), target))

        return -1, None
