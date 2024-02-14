import itertools
from graph_parser import read_city_data, to_array
import time


# Given distance matrix

filepath = input(r"Enter the file path to your graph:").strip()
distance_matrix = to_array(read_city_data(filepath))

# distance_matrix = [
#     [0, 3032, 25282, 99623, 209741, 410137, 541103, 905061, 1057110, 1441298, 16844],
#     [3032, 0, 10805, 67938, 162683, 342689, 463222, 803337, 946972, 1312298, 26510],
#     [25282, 10805, 0, 24596, 90162, 231817, 332606, 627812, 755489, 1085087, 60773],
#     [99623, 67938, 24596, 0, 20927, 105517, 176371, 404461, 507788, 783067, 150868],
#     [209741, 162683, 90162, 20927, 0, 35168, 78644, 247844, 328493, 553709, 269068],
#     [410137, 342689, 231817, 105517, 35168, 0, 9125, 96937, 150356, 313918, 498626],
#     [541103, 463222, 332606, 176371, 78644, 9125, 0, 47290, 85798, 216183, 638193],
#     [905061, 803337, 627812, 404461, 247844, 96937, 47290, 0, 6152, 63584, 1032927],
#     [1057110, 946972, 755489, 507788, 328493, 150356, 85798, 6152, 0, 30211, 1190097],
#     [1441298, 1312298, 1085087, 783067, 553709, 313918, 216183, 63584, 30211, 0, 1588111],
#     [16844, 26510, 60773, 150868, 269068, 498626, 638193, 1032927, 1190097, 1588111, 0]
# ]

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
