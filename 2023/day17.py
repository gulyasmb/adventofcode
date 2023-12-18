def main():
    city_map = read_input("17")
    # [print(*city_map_line, sep = "") for city_map_line in city_map]

    # Part one
    print(search_min_path_alt(city_map, 1, 3))

    # Part two
    print(search_min_path_alt(city_map, 4, 10))

def search_min_path_alt(city_map, min_straight_line, max_straight_line):
    paths = [[[0, 0, "v", 0]], [[0, 0, ">", 0]]]
    discovered_paths = {}
    dest_i = len(city_map) - 1
    dest_j = len(city_map[dest_i]) - 1
    path_sums = []
    winner_paths = []
    while paths != []:
        full_path = paths.pop(0)
        current_path = full_path[len(full_path) - 1]
        if tuple(current_path) in discovered_paths:
            path_sum = discovered_paths[tuple(current_path)]
        else:
            path_sum = 0
        i = current_path[0]
        j = current_path[1]
        
        if (i == dest_i) and (j == dest_j):
            path_sums.append(path_sum)
            winner_paths.append(full_path)
        else:
            # >
            if (
                (j < dest_j) and
                not (current_path[2] == ">" and current_path[3] == max_straight_line) and
                not (current_path[2] != ">" and current_path[3] < min_straight_line) and
                current_path[2] != "<"
                ):
                next_path = current_path.copy()
                next_path[1] = current_path[1] + 1
                if current_path[2] == ">":
                    next_path[3] = current_path[3] + 1
                else:
                    next_path[2] = ">"
                    next_path[3] = 1
                if tuple(next_path) in discovered_paths:
                    if path_sum + city_map[i][j + 1] < discovered_paths[tuple(next_path)]:
                        discovered_paths[tuple(next_path)] = path_sum + city_map[i][j + 1]
                        full_path_temp = full_path.copy()
                        full_path_temp.append(next_path.copy())
                        paths.append(full_path_temp)
                else:
                    discovered_paths[tuple(next_path)] = path_sum + city_map[i][j + 1]
                    full_path_temp = full_path.copy()
                    full_path_temp.append(next_path.copy())
                    paths.append(full_path_temp)
            # v
            if (
                (i < dest_i) and
                not (current_path[2] == "v" and current_path[3] == max_straight_line) and
                not (current_path[2] != "v" and current_path[3] < min_straight_line) and
                current_path[2] != "^"
                ):
                next_path = current_path.copy()
                next_path[0] = current_path[0] + 1
                if current_path[2] == "v":
                    next_path[3] = current_path[3] + 1
                else:
                    next_path[2] = "v"
                    next_path[3] = 1
                if tuple(next_path) in discovered_paths:
                    if path_sum + city_map[i + 1][j] < discovered_paths[tuple(next_path)]:
                        discovered_paths[tuple(next_path)] = path_sum + city_map[i + 1][j]
                        full_path_temp = full_path.copy()
                        full_path_temp.append(next_path.copy())
                        paths.append(full_path_temp)
                else:
                    discovered_paths[tuple(next_path)] = path_sum + city_map[i + 1][j]
                    full_path_temp = full_path.copy()
                    full_path_temp.append(next_path.copy())
                    paths.append(full_path_temp)
            # <
            if (
                (0 < j) and
                not (current_path[2] == "<" and current_path[3] == max_straight_line) and
                not (current_path[2] != "<" and current_path[3] < min_straight_line) and
                current_path[2] != ">"
                ):
                next_path = current_path.copy()
                next_path[1] = current_path[1] - 1
                if current_path[2] == "<":
                    next_path[3] = current_path[3] + 1
                else:
                    next_path[2] = "<"
                    next_path[3] = 1
                if tuple(next_path) in discovered_paths:
                    if path_sum + city_map[i][j - 1] < discovered_paths[tuple(next_path)]:
                        discovered_paths[tuple(next_path)] = path_sum + city_map[i][j - 1]
                        full_path_temp = full_path.copy()
                        full_path_temp.append(next_path.copy())
                        paths.append(full_path_temp)
                else:
                    discovered_paths[tuple(next_path)] = path_sum + city_map[i][j - 1]
                    full_path_temp = full_path.copy()
                    full_path_temp.append(next_path.copy())
                    paths.append(full_path_temp)
            # ^
            if (
                (0 < i) and
                not (current_path[2] == "^" and current_path[3] == max_straight_line) and
                not (current_path[2] != "^" and current_path[3] < min_straight_line) and
                current_path[2] != "v"
                ):
                next_path = current_path.copy()
                next_path[0] = current_path[0] - 1
                if current_path[2] == "^":
                    next_path[3] = current_path[3] + 1
                else:
                    next_path[2] = "^"
                    next_path[3] = 1
                if tuple(next_path) in discovered_paths:
                    if path_sum + city_map[i - 1][j] < discovered_paths[tuple(next_path)]:
                        discovered_paths[tuple(next_path)] = path_sum + city_map[i - 1][j]
                        full_path_temp = full_path.copy()
                        full_path_temp.append(next_path.copy())
                        paths.append(full_path_temp)
                else:
                    discovered_paths[tuple(next_path)] = path_sum + city_map[i - 1][j]
                    full_path_temp = full_path.copy()
                    full_path_temp.append(next_path.copy())
                    paths.append(full_path_temp)
    return min(*path_sums)

def read_input(filename):
    input = open("2023\inputs\inputday" + filename + ".txt", "r")
    city_map = [list(map(int, list(line))) for line in input.read().split("\n")]
    return city_map

if __name__ == "__main__":
    main()