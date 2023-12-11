input = open("2023\inputday11.txt", "r")
map = [list(line) for line in input.read().split("\n")]

def get_expansion_data(map):
    expansion_data = {"empty_rows": [],
                      "empty_columns": []}
    for i in range(len(map)):
        empty = True
        for element in map[i]:
            if element == "#":
                empty = False
                break
        if empty:
            expansion_data["empty_rows"].append(i)
    for j in range(len(map[0])):
        empty = True
        for i in range(len(map)):
            if map[i][j] == "#":
                empty = False
                break
        if empty:
            expansion_data["empty_columns"].append(j)
    return expansion_data

def find_galaxies(map):
    galaxies = []
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "#":
                galaxies.append({"x": j,
                                 "y": i})
    return galaxies

def find_galaxy_distances(galaxies, expansion_data, expansion_rate):
    galaxy_distances = 0
    for i in range(len(galaxies) - 1):
        for j in range(i + 1, len(galaxies)):
            galaxy_distances += abs(galaxies[j]["x"] - galaxies[i]["x"]) + abs(galaxies[j]["y"] - galaxies[i]["y"])
            for row_index in expansion_data["empty_rows"]:
                if row_index in list(range(min(galaxies[j]["y"], galaxies[i]["y"]), max(galaxies[j]["y"], galaxies[i]["y"]))):
                    galaxy_distances += expansion_rate
            for column_index in expansion_data["empty_columns"]:
                if column_index in list(range(min(galaxies[j]["x"], galaxies[i]["x"]), max(galaxies[j]["x"], galaxies[i]["x"]))):
                    galaxy_distances += expansion_rate
    return galaxy_distances

def main():
    # Part one
    expansion_data = get_expansion_data(map)
    galaxies = find_galaxies(map)
    galaxy_distances = find_galaxy_distances(galaxies, expansion_data, 1)
    print(galaxy_distances)

    # Part two
    galaxy_distances = find_galaxy_distances(galaxies, expansion_data, 999999)
    print(galaxy_distances)

main()