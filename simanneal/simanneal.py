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


def read_params():
    case = sys.argv[2] if len(sys.argv) >= 3 else "Z"
    t_max = int(sys.argv[3]) if len(
        sys.argv) >= 4 else random.uniform(10, 100)
    k = float(sys.argv[4]) if len(sys.argv) >= 5 else 0.95
    kt = int(sys.argv[5]) if len(sys.argv) >= 6 else random.uniform(20, 25)
    t_min = int(sys.argv[6]) if len(
        sys.argv) >= 7 else random.uniform(5, 10)

    print(f'case: {case}')
    print(f'max temperature: {t_max}')
    print(f'min temperature: {t_min}')
    print(f'annealing ratio: {k}')
    print(f'number of iterations: {kt}')
    print('calculating...')

    return t_max, t_min, k, kt


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


def criterion(current_route_length, best_route_length, current_neighbour, best_neighbour, T):
    if random.uniform(0, 1) < np.exp((current_route_length - best_route_length)/T):
        current_route_length = best_route_length
        current_neighbour = best_neighbour

    return current_route_length, current_neighbour


def get_best_neighbour(tsp, neighbours, T):
    best_route_length = get_route_length(tsp, neighbours[0])
    best_neighbour = neighbours[0]
    for neighbour in neighbours:
        current_route_length = get_route_length(tsp, neighbour)
        if current_route_length < best_route_length:
            best_route_length = current_route_length
            best_neighbour = neighbour
        else:
            best_route_length, best_neighbour = criterion(
                current_route_length, best_route_length, neighbour, best_neighbour, T)
    return best_neighbour, best_route_length


def simanneal():
    coordenates = read_file()
    t_max, t_min, annealing_ratio, n_iterations = read_params()
    tsp_matrix = generate_tsp_matrix(coordenates)

    current_route_length = np.Infinity

    descending_t = t_max

    while descending_t > t_min:
        iterations = 0

        current_solution = generate_random_solution(tsp_matrix)
        current_route_length = get_route_length(tsp_matrix, current_solution)
        neighbours = get_neighbours(current_solution)
        best_neighbour, best_neighbour_route_length = get_best_neighbour(
            tsp_matrix, neighbours, descending_t)

        while best_neighbour_route_length < current_route_length and iterations < n_iterations:
            current_solution = best_neighbour
            current_route_length = best_neighbour_route_length
            neighbours = get_neighbours(current_solution)
            best_neighbour, best_neighbour_route_length = get_best_neighbour(
                tsp_matrix, neighbours, descending_t)
            iterations += 1

        descending_t = annealing_ratio*descending_t

    return current_route_length


print(f'best solution cost: {simanneal()}')
