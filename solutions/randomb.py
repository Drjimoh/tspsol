import itertools
from graph_parser import read_city_data, to_array
import time
import concurrent.futures

# Function to calculate the total distance of a tour
def calculate_tour_distance(tour):
    total_distance = 0
    for i in range(num_cities - 1):
        total_distance += distance_matrix[tour[i]][tour[i+1]]
    total_distance += distance_matrix[tour[-1]][tour[0]]  # Return to starting city
    return total_distance

# Define function for parallel processing
def calculate_permutation_distance(permutation):
    distance = calculate_tour_distance(permutation)
    return distance

if __name__ == "__main__":
    # Given distance matrix
    filepath = input(r"Enter the file path to your graph:").strip()
    distance_matrix = to_array(read_city_data(filepath))

    # Number of cities
    num_cities = len(distance_matrix)

    # Generate all possible permutations of cities
    all_permutations = itertools.permutations(range(num_cities))

    # Initialize minimum distance and corresponding tour
    min_distance = float('inf')
    optimal_tour = None

    start_time = time.time()
    total_permutations = 0

    # Parallel processing using ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for i, permutation in enumerate(all_permutations, start=1):
            # Calculate permutation distance
            distance = calculate_tour_distance(permutation)

            # Update minimum distance and corresponding tour
            if distance < min_distance:
                min_distance = distance
                optimal_tour = permutation

            # Print progress report
            if i % 1000 == 0:  # Adjust as needed
                print(f"Progress: {i} permutations processed")

    # Calculate duration
    duration = time.time() - start_time

    # Print the optimal tour and its total distance
    print("Optimal Tour:", optimal_tour)
    print("Total Distance:", min_distance)
    print("Total Permutations:", i)
    print("Duration:", duration, "seconds")
