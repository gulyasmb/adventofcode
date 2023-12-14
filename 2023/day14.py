def main():
    # Part one
    platform = read_input("14")
    tilt_platform(platform, "north")
    load = calculate_load(platform)
    print(load)

    # Part two
    platform = read_input("14")
    platform_history = []
    while True:
        tilt_cycle(platform)
        if platform in platform_history:
            initial_cycle_start = platform_history.index(platform)
            cycle_length = len(platform_history) - initial_cycle_start
            final_cycle_equivalent = (1000000000 - initial_cycle_start)%cycle_length + initial_cycle_start - 1
            break
        platform_history.append([line.copy() for line in platform])
    load = calculate_load(platform_history[final_cycle_equivalent])
    print(load)

def read_input(filename):
    input = open("2023\inputs\inputday" + filename + ".txt", "r")
    platform_raw  = input.read().split("\n")
    platform = [list(line) for line in platform_raw]
    return platform

def tilt_cycle(platform):
    tilt_platform(platform, "north")
    tilt_platform(platform, "west")
    tilt_platform(platform, "south")
    tilt_platform(platform, "east")

def tilt_platform(platform, direction):
    if direction == "north" or direction == "south":
        if direction == "north":
            column_range = range(len(platform))
            increment = 1
        elif direction == "south":
            column_range = list(reversed(range(len(platform))))
            increment = -1
        for j in range(len(platform[0])):
            sliding_possible = False
            for i in column_range:
                if platform[i][j] == "." and not sliding_possible:
                    sliding_possible = True
                    place_to_fill = i
                elif platform[i][j] == "#":
                    sliding_possible = False
                elif platform[i][j] == "O" and sliding_possible:
                        platform[place_to_fill][j] = "O"
                        platform[i][j] = "."
                        place_to_fill += increment
    elif direction == "east" or direction == "west":
        if direction == "west":
            row_range = range(len(platform[0]))
            increment = 1
        elif direction == "east":
            row_range = list(reversed(range(len(platform[0]))))
            increment = -1
        for i in range(len(platform)):
            sliding_possible = False
            for j in row_range:
                if platform[i][j] == "." and not sliding_possible:
                    sliding_possible = True
                    place_to_fill = j
                elif platform[i][j] == "#":
                    sliding_possible = False
                elif platform[i][j] == "O" and sliding_possible:
                        platform[i][place_to_fill] = "O"
                        platform[i][j] = "."
                        place_to_fill += increment

def calculate_load(platform):
    load = 0
    for i in range(len(platform)):
        for j in range(len(platform[i])):
            if platform[i][j] == "O":
                load += len(platform) - i
    return load

if __name__ == "__main__":
    main()