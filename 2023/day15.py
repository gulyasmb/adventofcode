def main():
    init_sequence = read_input("15")

    # Part one
    val_sums = 0
    for step in init_sequence:
        val_sums += calculate_hash(step)
    print(val_sums)

    # Part two
    boxes = [{} for _ in range(256)]
    for step in init_sequence:
        perform_step(step, boxes)
    focusing_power = calculate_focusing_power(boxes)
    print(focusing_power)

def calculate_hash(step):
    current_val = 0
    for char in step:
        current_val = ((current_val + ord(char)) * 17) % 256
    return(current_val)

def perform_step(step, boxes):
    if "-" in step:
        label = step.split("-")[0]
        box_id = calculate_hash(label)
        if label in boxes[box_id]:
            del boxes[box_id][label]
    if "=" in step:
        label = step.split("=")[0]
        focal_length = int(step.split("=")[1])
        box_id = calculate_hash(label)
        boxes[box_id][label] = focal_length

def calculate_focusing_power(boxes):
    focusing_power = 0
    for box_id in range(len(boxes)):
        lense_values = list(boxes[box_id].values())
        for lense_id in range(len(lense_values)):
            focusing_power += (box_id + 1) * (lense_id + 1) * lense_values[lense_id]
    return focusing_power

def read_input(filename):
    input = open("2023\inputs\inputday" + filename + ".txt", "r")
    init_sequence  = input.read().split(",")
    return init_sequence

if __name__ == "__main__":
    main()