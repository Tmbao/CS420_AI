from random import randint
import math

import demo

algorithms = ['Astar', 'BFS', 'UCS']

def generate_input(n_vertice, n_edge, file_name):
    vertices = []
    for i in range(n_vertice):
        vertices.append((i, i, randint(0, 1000), randint(0, 1000)))

    edges = {}
    for i in range(1, n_vertice):
        u = randint(0, i - 1)
        v = i
        edges[(v, u)] = edges[(u, v)] = math.sqrt((vertices[u][2] - vertices[v][2]) ** 2 + (vertices[u][3] - vertices[v][3]) ** 2) * 10 # * randint(2, 100)

    for i in range(n_vertice, n_edge + 1):
        while True:
            u = randint(0, n_vertice - 1)
            v = randint(0, n_vertice - 1)
            if u != v and (u, v) not in edges:
                break
        edges[(v, u)] = edges[(u, v)] = math.sqrt((vertices[u][2] - vertices[v][2]) ** 2 + (vertices[u][3] - vertices[v][3]) ** 2) * 10 # * randint(2, 100)

    with open(file_name, 'w') as file:
        file.write('{}\n'.format(n_vertice))
        for i in range(n_vertice):
            file.write('{} {} {} {}\n'.format(*vertices[i]))
        file.write('{}\n'.format(n_edge * 2))
        for (u, v) in edges.keys():
            file.write('{} {} {}\n'.format(u, v, edges[(u, v)]))
        file.write('{} {}'.format(randint(0, n_vertice - 1), randint(0, n_vertice - 1)))


n_test = 10
for test_id in range(n_test):
    print '\n---\nTEST {}'.format(test_id)
    n_vertice = randint(800, 1000)
    n_edge = n_vertice * 2
    print '#vertices = {}, #edges = {}'.format(n_vertice, n_edge)
    generate_input(n_vertice, n_edge, 'temp.txt')

    for algorithm in algorithms:
        demo.demo(algorithm, 'temp.txt', None)
