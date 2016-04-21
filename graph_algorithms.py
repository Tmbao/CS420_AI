from heapq import heappush, heappop
from collections import deque


def _trace(source, target, trace):
    path = []
    node = target
    while node is not source:
        prev = trace[node]
        path.append((prev, node))
        node = prev
    res = path[::-1]
    return res

class AstarAlgorithm(object):
    def __init__(self, heuristic_func):
        self.heuristic_func = heuristic_func

    def get_path(self, graph, source, target, weight_tag='len'):
        # dictionary of distance from source
        distance    = [float('inf')] * graph.number_of_nodes()
        trace       = [None] * graph.number_of_nodes()

        # open set and closed set
        openset     = []
        closedset   = [False] * graph.number_of_nodes()

        # put the source in open set
        distance[source] = 0
        heappush(openset, (distance[source] + self.heuristic_func(source, target), source))

        while len(openset) > 0:
            # get the top element of the heap
            (cur_hcost, cur_node) = heappop(openset)
            cur_dist = distance[cur_node]

            # check whether we went to this node
            if closedset[cur_node]:
                continue

            # check whether we have reached the target
            if cur_node == target:
                # TODO: return the path from source to garget
                return cur_dist, _trace(source, target, trace)

            # add the current node into closed set
            closedset[cur_node] = True
            
            # iterate adjacent nodes
            for edge in graph.edges(cur_node, data=True):
                (_, next_node, attr_dict) = edge

                if closedset[next_node] is False:
                    if distance[next_node] > cur_dist + attr_dict[weight_tag]:
                        distance[next_node] = cur_dist + attr_dict[weight_tag]
                        trace[next_node] = cur_node
                        heappush(openset, (distance[next_node] + self.heuristic_func(next_node, target), next_node))

        return None, None

class DFSAlgorithm(object):
    def _dfs(self, graph, source, target, weight_tag='len'):
        if source == target:
            return True

        for edge in graph.edges(source, data=True):
                (_, next_node, attr_dict) = edge

                if self.distance[next_node] == float('inf'):
                    self.distance[next_node] = self.distance[source] + attr_dict[weight_tag]
                    self.trace[next_node] = source
                    if self._dfs(graph, next_node, target, weight_tag):
                        return True

        return False

    def get_path(self, graph, source, target, weight_tag='len'):
        # In this algorithm, distance also plays the role of closedset
        self.distance    = [float('inf')] * graph.number_of_nodes()
        self.trace       = [0] * graph.number_of_nodes()

        self.distance[source] = 0
        if self._dfs(graph, source, target, weight_tag):
            return self.distance[target], _trace(source, target, self.trace)
        else:
            return None, None


class HillClimbingAlgorithm(object):
    def _greedy_dfs(self, graph, source, target, weight_tag='len'):
        if source == target:
            return True

        openset = []
        for edge in graph.edges(source, data=True):
                (_, next_node, attr_dict) = edge
                openset.append((next_node, self.distance[source] + attr_dict[weight_tag]))

        openset = sorted(openset, key=lambda x: x[1])
        for next_node, next_dist in openset:
            if self.distance[next_node] == float('inf'):
                self.distance[next_node] = next_dist
                self.trace[next_node] = source
                if self._greedy_dfs(graph, next_node, target, weight_tag):
                    return True

        return False

    def get_path(self, graph, source, target, weight_tag='len'):
        # In this algorithm, distance also plays the role of closedset
        self.distance    = [float('inf')] * graph.number_of_nodes()
        self.trace       = [None] * graph.number_of_nodes()

        self.distance[source] = 0
        if self._greedy_dfs(graph, source, target, weight_tag):
            return self.distance[target], _trace(source, target, self.trace)
        else:
            return None, None    