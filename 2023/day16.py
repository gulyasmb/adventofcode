def main():
    grid = read_input("16")

    # Part one
    beams = [[0, -1, ">"]]
    print(energized_tiles_of_beam_config(grid, beams))
    
    # Part two
    beam_config_results = []
    for i in range(len(grid)):
        beams = [[i, -1, ">"]]
        beam_config_results.append(energized_tiles_of_beam_config(grid, beams))
        beams = [[i, len(grid), "<"]]
        beam_config_results.append(energized_tiles_of_beam_config(grid, beams))
        beams = [[-1, i, "v"]]
        beam_config_results.append(energized_tiles_of_beam_config(grid, beams))
        beams = [[i, len(grid), "^"]]
        beam_config_results.append(energized_tiles_of_beam_config(grid, beams))
    print(max(beam_config_results))

def energized_tiles_of_beam_config(grid, beams):
    light_grid = [[""] * len(grid_line) for grid_line in grid]

    while beams != []:
        for beam in beams:
            # Step beam forward
            dir = beam[2]
            if dir == ">":
                beam[1] += 1
            elif dir == "<":
                beam[1] -= 1
            elif dir == "^":
                beam[0] -= 1
            elif dir == "v":
                beam[0] += 1
            i = beam[0]
            j = beam[1]
            
            # Remove beam if outside borders
            if not ((0 <= i < len(grid)) and (0 <= j < len(grid))):
                beams.remove(beam)
            else:
                # Redirect beam in case of mirrors
                if grid[i][j] == "\\":
                    if dir == ">":
                        dir = "v"
                    elif dir == "<":
                        dir = "^"
                    elif dir == "v":
                        dir = ">"
                    elif dir == "^":
                        dir = "<"
                elif grid[i][j] == "/":
                    if dir == ">":
                        dir = "^"
                    elif dir == "<":
                        dir = "v"
                    elif dir == "v":
                        dir = "<"
                    elif dir == "^":
                        dir = ">"
                # Split beams in case of splitters
                elif grid[i][j] == "-":
                    if dir in "^v":
                        dir = ">"
                        if "<" not in light_grid[i][j]:
                            beams.append([i, j, "<"])
                            light_grid[i][j] += "<"
                elif grid[i][j] == "|":
                    if dir in "<>":
                        dir = "^"
                        if "v" not in light_grid[i][j]:
                            beams.append([i, j, "v"])
                            light_grid[i][j] += "v"
                # Update light grid
                if dir not in light_grid[i][j]:
                    light_grid[i][j] += dir
                    beam[2] = dir
                else:
                    beams.remove(beam)
    
    # Return the number of energized (not empty) tiles from the light grid
    return sum(1 for tile in sum(light_grid, []) if tile != "")

def read_input(filename):
    input = open("2023\inputs\inputday" + filename + ".txt", "r")
    grid = [list(line) for line in input.read().split("\n")]
    return grid

if __name__ == "__main__":
    main()