import random
import math

cities = {
    'A': (0, 0),
    'B': (1, 3),
    'C': (4, 3),
    'D': (6, 1),
    'E': (3, 0)
}

def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def total_distance(route):
    return sum(distance(cities[route[i]], cities[route[i+1]]) for i in range(len(route) - 1)) + distance(cities[route[-1]], cities[route[0]])

def initial_route():
    route = list(cities.keys())
    random.shuffle(route)
    return route

def hill_climbing(route):
    current_route = route
    current_distance = total_distance(current_route)

    while True:
        neighbors = generate_neighbors(current_route)
        next_route = min(neighbors, key=total_distance)
        next_distance = total_distance(next_route)

        if next_distance < current_distance:
            current_route = next_route
            current_distance = next_distance
        else:
            break

    return current_route, current_distance

def generate_neighbors(route):
    neighbors = []
    for i in range(len(route)):
        for j in range(i + 1, len(route)):
            neighbor = route[:]
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors

initial = initial_route()
print("Initial route:", initial)
print("Initial distance:", total_distance(initial))

optimal_route, optimal_distance = hill_climbing(initial)
print("Optimal route:", optimal_route)
print("Optimal distance:", optimal_distance)
