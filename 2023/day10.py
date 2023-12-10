input = open("2023\inputday10.txt", "r")
map = input.read().split("\n")

def find_first_pipes():
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "S":
                pipe = [{"row": i,
                         "column": j,
                         "type": map[i][j]}]
                if map[i-1][j] in "|7F":
                    pipe.append({"row": i-1,
                                 "column": j,
                                 "type": map[i-1][j]})
                    return pipe
                if map[i+1][j] in "|LJ":
                    pipe.append({"row": i+1,
                                 "column": j,
                                 "type": map[i+1][j]})
                    return pipe
                if map[i][j-1] in "-LF":
                    pipe.append({"row": i,
                                 "column": j-1,
                                 "type": map[i][j-1]})
                    return pipe
                if map[i][j+1] in "-J7":
                    pipe.append({"row": i,
                                 "column": j+1,
                                 "type": map[i][j+1]})
                    return pipe

def find_next_pipe(pipe, map):
    if (
        (pipe[len(pipe)-1]["type"] == "|" and pipe[len(pipe)-2]["row"] == pipe[len(pipe)-1]["row"] + 1) or
        (pipe[len(pipe)-1]["type"] == "J" and pipe[len(pipe)-2]["column"] == pipe[len(pipe)-1]["column"] - 1) or
        (pipe[len(pipe)-1]["type"] == "L" and pipe[len(pipe)-2]["column"] == pipe[len(pipe)-1]["column"] + 1)
        ):
        next_pipe_element = {"row": pipe[len(pipe)-1]["row"]-1,
                        "column": pipe[len(pipe)-1]["column"],
                        "type": map[pipe[len(pipe)-1]["row"]-1][pipe[len(pipe)-1]["column"]]}
        return next_pipe_element
    if (
        (pipe[len(pipe)-1]["type"] == "|" and pipe[len(pipe)-2]["row"] == pipe[len(pipe)-1]["row"] - 1) or
        (pipe[len(pipe)-1]["type"] == "7" and pipe[len(pipe)-2]["column"] == pipe[len(pipe)-1]["column"] - 1) or
        (pipe[len(pipe)-1]["type"] == "F" and pipe[len(pipe)-2]["column"] == pipe[len(pipe)-1]["column"] + 1)
        ):
        next_pipe_element = {"row": pipe[len(pipe)-1]["row"]+1,
                        "column": pipe[len(pipe)-1]["column"],
                        "type": map[pipe[len(pipe)-1]["row"]+1][pipe[len(pipe)-1]["column"]]}
        return next_pipe_element
    if (
        (pipe[len(pipe)-1]["type"] == "-" and pipe[len(pipe)-2]["column"] == pipe[len(pipe)-1]["column"] - 1) or
        (pipe[len(pipe)-1]["type"] == "L" and pipe[len(pipe)-2]["row"] == pipe[len(pipe)-1]["row"] - 1) or
        (pipe[len(pipe)-1]["type"] == "F" and pipe[len(pipe)-2]["row"] == pipe[len(pipe)-1]["row"] + 1)
        ):
        next_pipe_element = {"row": pipe[len(pipe)-1]["row"],
                        "column": pipe[len(pipe)-1]["column"]+1,
                        "type": map[pipe[len(pipe)-1]["row"]][pipe[len(pipe)-1]["column"]+1]}
        return next_pipe_element
    if (
        (pipe[len(pipe)-1]["type"] == "-" and pipe[len(pipe)-2]["column"] == pipe[len(pipe)-1]["column"] + 1) or
        (pipe[len(pipe)-1]["type"] == "J" and pipe[len(pipe)-2]["row"] == pipe[len(pipe)-1]["row"] - 1) or
        (pipe[len(pipe)-1]["type"] == "7" and pipe[len(pipe)-2]["row"] == pipe[len(pipe)-1]["row"] + 1)
        ):
        next_pipe_element = {"row": pipe[len(pipe)-1]["row"],
                        "column": pipe[len(pipe)-1]["column"]-1,
                        "type": map[pipe[len(pipe)-1]["row"]][pipe[len(pipe)-1]["column"]-1]}
        return next_pipe_element
    next_pipe_element = {"row": pipe[len(pipe)-1]["row"],
                        "column": pipe[len(pipe)-1]["column"],
                        "type": map[pipe[len(pipe)-1]["row"]][pipe[len(pipe)-1]["column"]]}
    return next_pipe_element

def tile_in_pipe(i, j, pipe):
    for pipe_element in pipe:
        if pipe_element["row"] == i and pipe_element["column"] == j:
            return True
    return False

def main():
    # Part one
    pipe = find_first_pipes()

    while find_next_pipe(pipe, map)["type"] != "S":
        pipe.append(find_next_pipe(pipe, map))

    print(int(len(pipe)/2))

    #Part two

    # Remove "S" from map and pipe and replace with "real" pipe type
    pipe[0]["type"] = "J"
    map[pipe[0]["row"]] = map[pipe[0]["row"]].replace("S", "J")

    enclosed_tiles = 0
    for i in range(len(map)):
        inside_enclosure = False
        border_start = ""
        for j in range(len(map[i])):
            current_tile = map[i][j]
            if tile_in_pipe(i, j, pipe):
                # "S" type sequences (FJ, or L7 with optional "-"-s in between them), 
                # and "|" character change if we are inside the pipe enclosure or not
                if map[i][j] in "FL":
                    border_start = map[i][j]
                elif map[i][j] in "J7":
                    if border_start == "F" and map[i][j] == "J":
                        inside_enclosure = not inside_enclosure
                    if border_start == "L" and map[i][j] == "7":
                        inside_enclosure = not inside_enclosure
                    border_start = ""
                elif map[i][j] == "|":
                    inside_enclosure = not inside_enclosure
            else:
                if inside_enclosure:
                    enclosed_tiles += 1

    print(enclosed_tiles)

main()