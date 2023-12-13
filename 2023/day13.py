def main():
    mirror_patterns = read_input("13")
    
    # Part one
    pattern_notes_summary = 0
    for pattern in mirror_patterns:
        pattern_notes_summary += 100 * check_smudgy_mirror(pattern, smudges_on_mirror = 0)
        transposed_pattern = transpose_pattern(pattern)
        pattern_notes_summary += check_smudgy_mirror(transposed_pattern, smudges_on_mirror = 0)
    print(pattern_notes_summary)

    # Part two
    pattern_notes_summary = 0
    for pattern in mirror_patterns:
        pattern_notes_summary += 100 * check_smudgy_mirror(pattern, smudges_on_mirror = 1)
        transposed_pattern = transpose_pattern(pattern)
        pattern_notes_summary += check_smudgy_mirror(transposed_pattern, smudges_on_mirror = 1)
    print(pattern_notes_summary)

def read_input(filename):
    input = open("2023\inputs\inputday" + filename + ".txt", "r")
    records_raw  = input.read().split("\n\n")
    mirror_patterns = [pattern.split("\n") for pattern in records_raw]
    return mirror_patterns

def transpose_pattern(pattern):
    transposed_pattern = []
    for j in range(len(pattern[0])):
        new_line = ""
        for i in range(len(pattern)):
            new_line += pattern[i][j]
        transposed_pattern.append(new_line)
    return transposed_pattern

def check_smudgy_mirror(pattern, smudges_on_mirror):
    for i in range(len(pattern)-1):
        potential_smudges = 0
        a, b = i, i + 1
        while a >= 0 and b < len(pattern):
            potential_smudges += difference(pattern[a], pattern[b])
            if potential_smudges > smudges_on_mirror:
                break
            a -= 1
            b += 1
        if potential_smudges == smudges_on_mirror:
            return i + 1
    return 0

def difference(line1, line2):
    differences = 0
    for i in range(len(line1)):
        if line1[i] != line2[i]:
            differences += 1
    return differences

if __name__ == "__main__":
    main()