import numpy as np
import sys
import random


def euclidean(a, b):
    temp = a-b
    return np.sqrt(np.dot(temp.T, temp))


def read_file():
    coordenates = []
    with open(sys.argv[1]) as f:
        lines = f.readlines()
        for i in range(len(lines)):
            line = lines[i].split(' ')
            if len(line) > 0:
                filtered = list(filter(None, line))
                coord = [filtered[0], filtered[1], filtered[2].strip('\n')]
                coordenates.append(coord)
    return coordenates


def generate_tsp_matrix(coordenates):
    tsp_matrix = []
    for i in range(len(coordenates)):
        euclideans_by_node = [None] * len(coordenates)
        node_1 = np.array((float(coordenates[i][1]), float(coordenates[i][2])))
        for j in range(len(coordenates)):
            if int(coordenates[i][0]) == int(coordenates[j][0]):
                euclideans_by_node[j] = 0
            else:
                node_2 = np.array(
                    (float(coordenates[j][1]), float(coordenates[j][2])))
                dist = euclidean(node_1, node_2)
                euclideans_by_node[j] = dist
        tsp_matrix.append(euclideans_by_node)
    return tsp_matrix


def generate_random_solution(tsp):
    cities = list(range(len(tsp)))
    solution = []

    for i in range(len(tsp)):
        randomCity = cities[random.randint(0, len(cities) - 1)]
        solution.append(randomCity)
        cities.remove(randomCity)

    return solution


def get_route_length(tsp, solution):  # função de avaliação
    routeLength = 0
    for i in range(len(solution)):
        routeLength += tsp[solution[i - 1]][solution[i]]
    return routeLength


def get_neighbours(solution):
    neighbours = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbour = solution.copy()
            neighbour[i] = solution[j]
            neighbour[j] = solution[i]
            neighbours.append(neighbour)
    return neighbours


def get_best_neighbour(tsp, neighbours):
    best_route_length = get_route_length(tsp, neighbours[0])
    best_neighbour = neighbours[0]
    for neighbour in neighbours:
        current_route_length = get_route_length(tsp, neighbour)
        if current_route_length < best_route_length:
            best_route_length = current_route_length
            best_neighbour = neighbour
    return best_neighbour, best_route_length


def hill_climbing():
    coordenates = read_file()

    print('calculating...')

    tsp_matrix = generate_tsp_matrix(coordenates)
    current_solution = generate_random_solution(tsp_matrix)
    current_route_length = get_route_length(tsp_matrix, current_solution)
    neighbours = get_neighbours(current_solution)
    best_neighbour, best_neighbour_route_length = get_best_neighbour(
        tsp_matrix, neighbours)

    while best_neighbour_route_length < current_route_length:
        current_solution = best_neighbour
        current_route_length = best_neighbour_route_length
        neighbours = get_neighbours(current_solution)
        best_neighbour, best_neighbour_route_length = get_best_neighbour(
            tsp_matrix, neighbours)

    return current_route_length


print(f'best solution cost: {hill_climbing()}')
