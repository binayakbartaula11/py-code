import numpy as np
import matplotlib.pyplot as plt
from geopy.distance import geodesic

# Real GPS coordinates for each location
coordinates = [
    (27.6730, 85.3250),  # Patan Durbar Square
    (27.7000, 85.3100),  # Sundhara
    (27.6930, 85.3160),  # Tirpureshwor
    (27.7020, 85.3110),  # Newroad
    (27.7040, 85.3090),  # Kathmandu Durbar Square
    (27.6710, 85.4298)   # Bhaktapur Durbar Square
]

# Calculate the distance matrix using geodesic distance
num_locations = len(coordinates)
distances = np.zeros((num_locations, num_locations))

for i in range(num_locations):
    for j in range(num_locations):
        if i != j:
            distances[i, j] = geodesic(coordinates[i], coordinates[j]).km

# Hill Climbing Algorithm for TSP
def calculate_total_distance(route, distances):
    """Calculate the total distance of the given route."""
    total_distance = 0
    for i in range(len(route)):
        total_distance += distances[route[i], route[(i + 1) % len(route)]]
    return total_distance

def hill_climbing(distances, iterations=1000):
    """Solve TSP using Hill Climbing."""
    num_cities = len(distances)
    # Start with a random route
    current_route = np.random.permutation(num_cities)
    current_distance = calculate_total_distance(current_route, distances)
    
    for _ in range(iterations):
        # Generate two random cities to swap
        i, j = np.random.choice(num_cities, 2, replace=False)
        new_route = current_route.copy()
        new_route[i], new_route[j] = new_route[j], new_route[i]
        new_distance = calculate_total_distance(new_route, distances)
        
        # Accept the new route if it's shorter
        if new_distance < current_distance:
            current_route = new_route
            current_distance = new_distance
            
    return current_route, current_distance

# Solve TSP using Hill Climbing
best_route, best_distance = hill_climbing(distances)

# Visualization
def plot_route(coordinates, route):
    """Plot the route on a 2D plane."""
    plt.figure(figsize=(10, 8))
    ordered_coords = [coordinates[i] for i in route] + [coordinates[route[0]]]
    latitudes, longitudes = zip(*ordered_coords)
    plt.plot(longitudes, latitudes, '-o', label="Optimal Route")
    
    # Annotate points
    for i, (lat, lon) in enumerate(coordinates):
        plt.text(lon, lat, f'{i + 1}', fontsize=12, ha='right')
    
    plt.title("Traveling Salesman Problem Solution")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.legend()
    plt.grid()
    plt.show()

# Print results and plot the route
print("Optimal Route:", [i + 1 for i in best_route])  # Convert 0-indexed to 1-indexed
print("Total Distance (km):", best_distance)
plot_route(coordinates, best_route)