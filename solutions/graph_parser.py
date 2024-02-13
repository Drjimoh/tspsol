import numpy as np



def read_city_data(filename):
    with open(filename, "r+") as f:
        city_data_lines = f.readlines()
        # Remove any potential whitespace at the end of each line
        city_data_lines = [line.strip() for line in city_data_lines]

    city_data_list = []
    for line in city_data_lines:
        # Assuming each line starts with the city index and then has distances
        city_data_list.append([int(x) for x in line.split()])

    return city_data_list

# read graph file
# filename = r"C:\Users\waliu\Documents\clients\KO\TSP Assignment new\data\Size10.graph"  # Replace with your actual file name
# data = read_city_data(filename)

# print(data)

def to_array(data):
    # Convert the data to a NumPy array
    # Convert the data to a NumPy array
    data_array = np.array(data, dtype=object)

    # Get the size of the data array
    size = len(data_array)

    # Initialize the distance matrix with zeros
    distance_matrix = np.zeros((size, size))

    # Fill in the upper triangular part of the distance matrix
    for i in range(size):
        for j in range(i + 1, size):
            distance_matrix[i][j] = data_array[j][i]  # Corrected index for mirror values
            distance_matrix[j][i] = distance_matrix[i][j] 

    return distance_matrix


