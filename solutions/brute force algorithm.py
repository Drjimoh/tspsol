from graph_parser import read_city_data, to_array
import itertools
import time


# Given distance matrix

filepath = input(r"Enter the file path to your graph:").strip()
distance_matrix = to_array(read_city_data(filepath))


# Number of cities
num_cities = len(distance_matrix)

# Function to calculate the total distance of a tour
def calculate_tour_distance(tour):
    total_distance = 0
    for i in range(num_cities - 1):
        total_distance += distance_matrix[tour[i]][tour[i+1]]
    total_distance += distance_matrix[tour[-1]][tour[0]]  # Return to starting city
    return total_distance

# Generate all possible permutations of cities
all_permutations = itertools.permutations(range(num_cities))

# Initialize minimum distance and corresponding tour
min_distance = float('inf')
optimal_tour = None

start_time = time.time()
total_permutations = 0



# Iterate through all permutations and calculate total distance
for i, permutation in enumerate(all_permutations, start=1):
    distance = calculate_tour_distance(permutation)
    if distance < min_distance:
        min_distance = distance
        optimal_tour = permutation

    # Print progress report
    if i % 100000 == 0:  # Adjust as needed
        print(f"Progress: {i} permutations processed")

# Calculate duration
duration = time.time() - start_time

# Print the optimal tour and its total distance
print("Optimal Tour:", optimal_tour)
print("Total Distance:", min_distance)
print("Total Permutations:", i)
print("Duration:", duration, "seconds")
