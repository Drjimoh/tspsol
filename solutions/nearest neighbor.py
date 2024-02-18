import numpy as np
from graph_parser import read_city_data, to_array
import time

# Given distance matrix

filepath = input(r"Enter the file path to your graph:").strip()
distance_matrix = to_array(read_city_data(filepath))


# Number of cities
num_cities = len(distance_matrix)

# Nearest Neighbor Algorithm function
def nearest_neighbor_algorithm(start_city):
    unvisited_cities = set(range(num_cities))
    unvisited_cities.remove(start_city)
    current_city = start_city
    tour = [start_city]

    while unvisited_cities:
        nearest_city = min(unvisited_cities, key=lambda city: distance_matrix[current_city][city])
        tour.append(nearest_city)
        unvisited_cities.remove(nearest_city)
        current_city = nearest_city

    # Return to the starting city to complete the tour
    tour.append(start_city)

    return tour

start_time = time.time()
# Test the algorithm starting from city 0
start_city = 0
optimal_tour = nearest_neighbor_algorithm(start_city)

# Calculate total distance of the tour
total_distance = sum(distance_matrix[optimal_tour[i]][optimal_tour[i + 1]] for i in range(len(optimal_tour) - 1))
# Calculate duration
duration = time.time() - start_time

# Print the optimal tour and its total distance
print("Optimal Tour:", optimal_tour)
print("Total Distance:", total_distance)
print("Duration:", duration, "seconds")

file_name = f"S{total_distance}_kovabor.sol"

# Write the optimal tour to the file
with open(file_name, "w") as file:
    for node in optimal_tour:
        file.write(str(node) + " ")

print(f"output file saved as {file_name}")
