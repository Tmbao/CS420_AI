from random import randint
import math

import demo

algorithms = ['Astar', 'BFS', 'UCS']

def l2distance(x1, y1, x2, y2):
    return math.sqrt(float(x1 - x2) ** 2 + float(y1 - y2) ** 2)

def generate_tree_input(n_vertice, n_edge, file_name):
    vertices = []
    for i in range(n_vertice):
        vertices.append((i, i, randint(0, 1000), randint(0, 1000)))

    edges = {}
    for i in range(1, n_vertice):
        u = randint(0, i - 1)
        v = i
        edges[(v, u)] = edges[(u, v)] = l2distance(vertices[u][2], vertices[u][3], vertices[v][2], vertices[v][3]) * 10 # * randint(2, 100)

    for i in range(n_vertice, n_edge + 1):
        while True:
            u = randint(0, n_vertice - 1)
            v = randint(0, n_vertice - 1)
            if u != v and (u, v) not in edges:
                break
        edges[(v, u)] = edges[(u, v)] = l2distance(vertices[u][2], vertices[u][3], vertices[v][2], vertices[v][3]) * 10 # * randint(2, 100)

    with open(file_name, 'w') as file:
        file.write('{}\n'.format(n_vertice))
        for i in range(n_vertice):
            file.write('{} {} {} {}\n'.format(*vertices[i]))
        file.write('{}\n'.format(n_edge * 2))
        for (u, v) in edges.keys():
            file.write('{} {} {}\n'.format(u, v, edges[(u, v)]))
        file.write('{} {}'.format(randint(0, n_vertice - 1), randint(0, n_vertice - 1)))


def generate_grid_input(n_vertice, n_edge, file_name):
    ratio = randint(2, n_vertice / 2)
    n_row = int(math.sqrt(n_vertice * ratio)) + 1
    n_col = n_row / ratio + 1

    ci = [0, -1, 0, 1, -1, 1, -1, 1]
    cj = [-1, 0, 1, 0, -1, -1, 1, 1]

    xs = [0] * n_row
    ys = [0] * n_col

    checked = [False] * 1000000
    for i in range(n_row):
        while True:
            xs[i] = randint(0, 999999)
            if not checked[xs[i]]:
                break
        checked[xs[i]] = True
    checked = [False] * 1000000
    for j in range(n_col):
        while True:
            ys[j] = randint(0, 999999)
            if not checked[ys[j]]:
                break
        checked[ys[j]] = True

    xs = sorted(xs)
    ys = sorted(ys)
    id = {}

    vertices = []
    n_vertice = 0
    for i in range(n_row):
        for j in range(n_col):
            vertices.append((n_vertice, n_vertice, xs[i], ys[j]))
            id[(xs[i], ys[j])] = n_vertice
            n_vertice += 1

    edges = {}
    for i in range(n_row):
        for j in range(n_col):
            u = id[(xs[i], ys[j])]
            for k in range(8):
                ii = i + ci[k]
                jj = j + cj[k]
                if ii >= 0 and ii < n_row and jj >= 0 and jj < n_col:
                    v = id[(xs[ii], ys[jj])]
                    edges[(u, v)] = l2distance(vertices[u][2], vertices[u][3], vertices[v][2], vertices[v][3]) * 10 # * randint(2, 100)

    n_vertice = len(vertices)
    n_edge = len(edges)

    with open(file_name, 'w') as file:
        file.write('{}\n'.format(n_vertice))
        for i in range(n_vertice):
            file.write('{} {} {} {}\n'.format(*vertices[i]))
        file.write('{}\n'.format(n_edge))
        for (u, v) in edges.keys():
            file.write('{} {} {}\n'.format(u, v, edges[(u, v)]))
        file.write('{} {}'.format(randint(0, n_vertice - 1), randint(0, n_vertice - 1)))


n_test = 10
for test_id in range(n_test):
    print '\n---\nTEST {}'.format(test_id)
    n_vertice = randint(10000, 200000)
    n_edge = n_vertice * randint(1, (n_vertice - 1) / 2)
    print '#vertices = {}, #edges = {}'.format(n_vertice, n_edge)
    generate_grid_input(n_vertice, n_edge, 'temp.txt')

    for algorithm in algorithms:
        demo.demo(algorithm, 'temp.txt', None)
