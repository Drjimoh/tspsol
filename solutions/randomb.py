import random

def generate_initial_population(population_size, cities):
  population = []
  for _ in range(population_size):
    visited = list(range(len(cities)))
    random.shuffle(visited)
    population.append(visited)
  return population

def crossover(parent1, parent2):
  crossover_point = random.randint(1, len(parent1) - 2)
  child1 = parent1[:crossover_point] + parent2[crossover_point:]
  child2 = parent2[:crossover_point] + parent1[crossover_point:]
  return child1, child2

def mutate(chromosome, mutation_rate):
  for i in range(len(chromosome)):
    if random.random() < mutation_rate:
      j = random.randint(0, len(chromosome) - 1)
      chromosome[i], chromosome[j] = chromosome[j], chromosome[i]
  return chromosome

def fitness(chromosome, distances):
  total_distance = sum(distances[i][j] for i, j in zip(chromosome, chromosome[1:] + [chromosome[0]]))
  return 1 / total_distance

def genetic_tsp(cities, distances, population_size, iterations, mutation_rate):
  population = generate_initial_population(population_size, cities)
  for _ in range(iterations):
    # Selection
    new_population = []
    for _ in range(population_size):
      parent1 = tournament_selection(population, fitness)
      parent2 = tournament_selection(population)
