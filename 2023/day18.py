def main():
    dig_plan = read_input("18")
    # [print(dig_plan_step, sep = "") for dig_plan_step in dig_plan]

    # Part one
    dig_site = create_dig_site_edge(dig_plan)
    dig_interior(dig_site)
    # [print(*dig_site_line, sep= "") for dig_site_line in dig_site]
    # output = open("2023\outputday" + "18" + ".txt", "w")
    # output.writelines(["".join(dig_site_line) + "\n" for dig_site_line in dig_site])
    print(sum(1 for tile in sum(dig_site, []) if tile != "."))

def create_dig_site_edge(dig_plan):
    dig_site = [["#"]]
    i, j = 0, 0
    for step_id in range(len(dig_plan)):
        if step_id == len(dig_plan) -1:
            next_step_id = 0
        else:
            next_step_id = step_id + 1
        for k in range(dig_plan[step_id]["meters"]):
            if dig_plan[step_id]["dir"] == "D":
                i += 1
                if i == len(dig_site):
                    dig_site.append(["."] * len(dig_site[0]))
                if k == dig_plan[step_id]["meters"] - 1:
                    if dig_plan[next_step_id]["dir"] == "R":
                        dig_site[i][j] = "L"
                    else:
                        dig_site[i][j] = "J"
                else:
                    dig_site[i][j] = "|"
            elif dig_plan[step_id]["dir"] == "U":
                i -= 1
                if i == -1:
                    dig_site.insert(0, ["."] * len(dig_site[0]))
                    i = 0
                if k == dig_plan[step_id]["meters"] - 1:
                    if dig_plan[next_step_id]["dir"] == "R":
                        dig_site[i][j] = "F"
                    else:
                        dig_site[i][j] = "7"
                else:
                    dig_site[i][j] = "|"
            elif dig_plan[step_id]["dir"] == "R":
                j += 1
                if j == len(dig_site[0]):
                    [dig_site_line.append(".") for dig_site_line in dig_site]
                if k == dig_plan[step_id]["meters"] - 1:
                    if dig_plan[next_step_id]["dir"] == "D":
                        dig_site[i][j] = "7"
                    else:
                        dig_site[i][j] = "J"
                else:
                    dig_site[i][j] = "-"
            elif dig_plan[step_id]["dir"] == "L":
                j -= 1
                if j == -1:
                    [dig_site_line.insert(0, ".") for dig_site_line in dig_site]
                    j = 0
                if k == dig_plan[step_id]["meters"] - 1:
                    if dig_plan[next_step_id]["dir"] == "D":
                        dig_site[i][j] = "F"
                    else:
                        dig_site[i][j] = "L"
                else:
                    dig_site[i][j] = "-"
    return dig_site

# Day 10 algorithm copied
def dig_interior(dig_site):
    for i in range(len(dig_site)):
        inside_enclosure = False
        border_start = ""
        for j in range(len(dig_site[i])):
            current_tile = dig_site[i][j]
            if current_tile != ".":
                # "S" type sequences (FJ, or L7 with optional "-"-s in between them), 
                # and "|" character change if we are inside the pipe enclosure or not
                if dig_site[i][j] in "FL":
                    border_start = dig_site[i][j]
                elif dig_site[i][j] in "J7":
                    if border_start == "F" and dig_site[i][j] == "J":
                        inside_enclosure = not inside_enclosure
                    if border_start == "L" and dig_site[i][j] == "7":
                        inside_enclosure = not inside_enclosure
                    border_start = ""
                elif dig_site[i][j] == "|":
                    inside_enclosure = not inside_enclosure
            else:
                if inside_enclosure:
                    dig_site[i][j] = "#"

def read_input(filename):
    input = open("2023\inputs\inputday" + filename + ".txt", "r")
    dig_plan_raw = [line.split(" ") for line in input.read().split("\n")]
    dig_plan = []
    for dig_plan_step in dig_plan_raw:
        dig_plan.append({"dir": dig_plan_step[0],
                         "meters": int(dig_plan_step[1]),
                         "color": dig_plan_step[2]})
    return dig_plan

if __name__ == "__main__":
    main()