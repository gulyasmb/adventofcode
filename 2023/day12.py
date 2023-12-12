def main():
    hot_spring_map, damage_data = read_input("12")

    # Part one
    sum_of_arrangements = count_arrangements(hot_spring_map, damage_data)
    print(sum_of_arrangements)

    # Part two
    unfold(hot_spring_map, damage_data)
    sum_of_arrangements = count_arrangements(hot_spring_map, damage_data)
    print(sum_of_arrangements)

def read_input(filename):
    input = open("2023\inputs\inputday" + filename + ".txt", "r")
    records_raw  = input.read().split("\n")
    hot_spring_map = [line.split(" ")[0] for line in records_raw]
    damage_data = [list(map(int, line.split(" ")[1].split(","))) for line in records_raw]
    return hot_spring_map, damage_data

def unfold(hot_spring_map, damage_data):
    for i in range(len(hot_spring_map)):
        hot_spring_map[i] = 4 * (hot_spring_map[i] + "?") + hot_spring_map[i]
        damage_data[i] += 4 * damage_data[i]

def count_arrangements(hot_spring_map, damage_data):
    sum_of_arrangements = 0
    for i in range(len(hot_spring_map)):
        # Add a good spring at the beginning and at the end of the row
        # for the algorithm to work properly. This way, it is quaranteed, 
        # that the row starts and ends with good springs. This does not
        # change the number permutations of a row.
        sum_of_good_springs = len(hot_spring_map[i]) - sum(damage_data[i]) + 2
        num_of_good_spring_seqs = len(damage_data[i]) + 1
        sum_of_arrangements += permutations(sum_of_good_springs,
                                            num_of_good_spring_seqs,
                                            damage_data[i],
                                            "." + hot_spring_map[i] + ".",
                                            {})
    return sum_of_arrangements

def permutations(sum_of_good_springs,
                 num_of_good_spring_seqs,
                 damage_data_row,
                 hot_spring_row,
                 calculated_permutations):

    # If this exact hot spring layout was already calculated, return its corresponding value
    permutation_id = str(sum_of_good_springs) + "_" + str(num_of_good_spring_seqs)
    if permutation_id in calculated_permutations:
        return calculated_permutations[permutation_id]
    
    if num_of_good_spring_seqs == 1:
        # Only one sequence of good springs remains at the end
        if "#" in hot_spring_row:
            calculated_permutations[permutation_id] = 0
            return 0
        else:
            calculated_permutations[permutation_id] = 1
            return 1
    else:
        num_of_permutations = 0
        # Remove one set of good springs and then one set of damaged springs from the whole row
        for first_good_spring_seq_length in range(1, sum_of_good_springs - num_of_good_spring_seqs + 2):
            start_of_sequence = first_good_spring_seq_length * "." + damage_data_row[0] * "#"
            arrangement_possible = True
            for i in range(len(start_of_sequence)):
                if (
                    (start_of_sequence[i] == "#" and hot_spring_row[i] == ".") or
                    (start_of_sequence[i] == "." and hot_spring_row[i] == "#")
                    ):
                    arrangement_possible = False
                    break
            if arrangement_possible:
                # If this part of the row is possible, calculate the permutations of the remaining part of the row
                num_of_permutations += permutations(sum_of_good_springs - first_good_spring_seq_length,
                                                    num_of_good_spring_seqs - 1,
                                                    damage_data_row[1:],
                                                    hot_spring_row[(first_good_spring_seq_length + damage_data_row[0]):],
                                                    calculated_permutations)
        calculated_permutations[permutation_id] = num_of_permutations
        return num_of_permutations

main()