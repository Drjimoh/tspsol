# Add necessary imports
import numpy as np
from graph_parser import read_city_data, to_array
import time

# Given distance matrix


filepath = input(r"Enter the file path to your graph:").strip()
distance_matrix = to_array(read_city_data(filepath))

# Number of cities
num_cities = len(distance_matrix)
start_time = time.time()

# Define parameters
population_size = 10
mutation_rate = 0.3
num_generations = 100

# Function to calculate total distance of a tour
def calculate_distance(tour):
    total_distance = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    return total_distance

# Initialize population
population = [np.random.permutation(num_cities).tolist() for _ in range(population_size)]

# Main loop
for generation in range(num_generations):
    # Evaluate fitness of each tour
    fitness_scores = [1 / calculate_distance(tour) for tour in population]
    total_fitness = sum(fitness_scores)

    # Selection
    selected_indices = np.random.choice(range(population_size), size=population_size, replace=True, p=[score / total_fitness for score in fitness_scores])

    # Crossover and mutation
    new_population = []
    for i in range(0, population_size, 2):
        parent1, parent2 = population[selected_indices[i]], population[selected_indices[i + 1]]
        crossover_point = np.random.randint(1, num_cities)
        child1 = parent1[:crossover_point] + [city for city in parent2 if city not in parent1[:crossover_point]]
        child2 = parent2[:crossover_point] + [city for city in parent1 if city not in parent2[:crossover_point]]

        # Mutation
        if np.random.rand() < mutation_rate:
            swap_indices = np.random.choice(range(1, num_cities), size=2, replace=False)
            child1[swap_indices[0]], child1[swap_indices[1]] = child1[swap_indices[1]], child1[swap_indices[0]]
            child2[swap_indices[0]], child2[swap_indices[1]] = child2[swap_indices[1]], child2[swap_indices[0]]

        new_population.extend([child1, child2])

    population = new_population

# Find the best tour
best_tour = min(population, key=calculate_distance)
best_distance = calculate_distance(best_tour)
# Calculate duration
duration = time.time() - start_time
print("Duration:", duration, "seconds")
# Print the best tour and its total distance
print("Best Tour:", best_tour)
print("Total Distance:", best_distance)
