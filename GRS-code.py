import math

def haversine_distance(lat1, lon1, lat2, lon2, R=6371):
    """Calculate great-circle distance between two points."""
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    return 2 * R * math.asin(math.sqrt(a))

def calculate_grs_cycle_completion(year, origin_year=-13015, total_cycle_duration=15440):
    """Calculate GRS cycle completion percentage."""
    elapsed_time = year - origin_year
    return (elapsed_time / total_cycle_duration) * 100

# Node data
nodes = [
    {"name": "Egyptian Origin", "year": -13015, "lat": 29.9792, "lon": 31.1342},
    {"name": "Sumerian Emergence", "year": -4000, "lat": 32.0, "lon": 44.5},
    {"name": "Giza Peak", "year": -2500, "lat": 29.9792, "lon": 31.1342},
    {"name": "Exodus Transfer", "year": -1300, "lat": 30.0, "lon": 33.0},
    {"name": "Harappa Emergence", "year": -2600, "lat": 30.6333, "lon": 72.8667},
    {"name": "Rome Foundation", "year": -753, "lat": 41.9028, "lon": 12.4964},
    {"name": "Rome Fall", "year": 476, "lat": 41.9028, "lon": 12.4964},
    {"name": "Islamic Expansion", "year": 622, "lat": 24.0, "lon": 39.0},
    {"name": "Crusades", "year": 1096, "lat": 31.7683, "lon": 35.2137},
    {"name": "Ottoman Expansion", "year": 1450, "lat": 41.0082, "lon": 28.9784},
    {"name": "Gaza Crisis", "year": 2025, "lat": 31.5204, "lon": 34.4647}
]

# Calculate distances and cycle percentages
giza = (29.9792, 31.1342)
data = [
    {"node": node["name"], "year": node["year"], 
     "distance": haversine_distance(node["lat"], node["lon"], *giza), 
     "cycle_percent": calculate_grs_cycle_completion(node["year"])}
    for node in nodes
]

# Example output
for d in data:
    print(f"{d['node']}: Distance {d['distance']:.1f} km, Cycle {d['cycle_percent']:.2f}%")