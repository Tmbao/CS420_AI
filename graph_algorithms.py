from heapq import heappush, heappop
from collections import deque


def _trace(source, target, trace):
    path = []
    node = target
    while node != source:
        prev = trace[node]
        path.append((prev, node))
        node = prev
    res = path[::-1]
    return res


class UCSAlgorithm(object):
    def get_path(self, graph, source, target, weight_tag='len', verbose=False):
        # dictionary of distance from source
        distance    = [float('inf')] * graph.number_of_nodes()
        trace       = [None] * graph.number_of_nodes()

        # open set and closed set
        openset     = []
        closedset   = [False] * graph.number_of_nodes()

        # put the source in open set
        distance[source] = 0
        heappush(openset, (distance[source], source))

        n_loops = 0

        while len(openset) > 0:
            n_loops += 1
            # get the top element of the heap
            (cur_dist, cur_node) = heappop(openset)

            # check whether we went to this node
            if closedset[cur_node]:
                continue

            # check whether we have reached the target
            if cur_node == target:
                # TODO: return the path from source to garget
                if verbose:
                    print 'Number of loops: {}'.format(n_loops)
                return cur_dist, _trace(source, target, trace)

            # add the current node into closed set
            closedset[cur_node] = True
            
            # iterate adjacent nodes
            for edge in graph.edges(cur_node, data=True):
                (_, next_node, attr_dict) = edge

                if closedset[next_node] == False:
                    if distance[next_node] > cur_dist + attr_dict[weight_tag]:
                        distance[next_node] = cur_dist + attr_dict[weight_tag]
                        trace[next_node] = cur_node
                        heappush(openset, (distance[next_node], next_node))

        return None, None


class AstarAlgorithm(object):
    def __init__(self, heuristic_func):
        self.heuristic_func = heuristic_func

    def get_path(self, graph, source, target, weight_tag='len', verbose=False):
        # dictionary of distance from source
        distance    = [float('inf')] * graph.number_of_nodes()
        trace       = [None] * graph.number_of_nodes()

        # open set and closed set
        openset     = []
        closedset   = [False] * graph.number_of_nodes()

        # put the source in open set
        distance[source] = 0
        heappush(openset, (distance[source] + self.heuristic_func(source, target), source))

        n_loops = 0

        while len(openset) > 0:
            n_loops += 1
            # get the top element of the heap
            (cur_hcost, cur_node) = heappop(openset)
            cur_dist = distance[cur_node]

            # check whether we went to this node
            if closedset[cur_node]:
                continue

            # check whether we have reached the target
            if cur_node == target:
                # TODO: return the path from source to garget
                if verbose:
                    print 'Number of loops: {}'.format(n_loops)
                return cur_dist, _trace(source, target, trace)

            # add the current node into closed set
            closedset[cur_node] = True
            
            # iterate adjacent nodes
            for edge in graph.edges(cur_node, data=True):
                (_, next_node, attr_dict) = edge

                if closedset[next_node] == False:
                    if distance[next_node] > cur_dist + attr_dict[weight_tag]:
                        distance[next_node] = cur_dist + attr_dict[weight_tag]
                        trace[next_node] = cur_node
                        heappush(openset, (distance[next_node] + self.heuristic_func(next_node, target), next_node))

        return None, None


class BFSAlgorithm(object):
    def get_path(self, graph, source, target, weight_tag='len', verbose=False):
        # In this algorithm, distance also plays the role of closedset
        distance    = [float('inf')] * graph.number_of_nodes()
        openset     = deque()
        trace       = [None] * graph.number_of_nodes()

        distance[source] = 0
        openset.append(source)

        n_loops = 0

        while len(openset) > 0:
            n_loops += 1

            cur_node = openset.popleft()
            cur_dist = distance[cur_node]

            if cur_node == target:
                if verbose:
                    print 'Number of loops: {}'.format(n_loops)
                return cur_dist, _trace(source, target, trace)

            for edge in graph.edges(cur_node, data=True):
                (_, next_node, attr_dict) = edge

                if distance[next_node] == float('inf'):
                    distance[next_node] = cur_dist + attr_dict[weight_tag]
                    trace[next_node] = cur_node
                    openset.append(next_node)

        return None, None
