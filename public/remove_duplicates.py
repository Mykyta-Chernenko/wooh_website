import json

# Function to read JSON file and return data
def read_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Function to write data to JSON file
def write_json_file(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Function to remove duplicates
def remove_duplicates(cities):
    seen = set()
    unique_cities = []
    for city in cities:
        city_country_pair = (city['city'], city['country'])
        if city_country_pair not in seen:
            seen.add(city_country_pair)
            unique_cities.append(city)
    return unique_cities

# File paths
cities_expats_file = './_cities_expats.json'
english_cities_file = './_english_cities.json'
advanced_cities_file = './_advanced_cities.json'
capital_cities = './_capital_cities.json'
output_file = './_all_cities.json'

# Read data from files
cities_expats = read_json_file(cities_expats_file)
english_cities = read_json_file(english_cities_file)
advanced_cities = read_json_file(advanced_cities_file)
capital_cities = read_json_file(capital_cities)

# Combine lists and remove duplicates
combined_cities = cities_expats + english_cities + advanced_cities + capital_cities
unique_combined_cities = remove_duplicates(combined_cities)

# Write the combined data to the output file
write_json_file(unique_combined_cities, output_file)

print(f"Combined JSON file created successfully at {output_file}")
