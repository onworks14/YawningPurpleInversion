import re

# Condition: only 12 red cubes, 13 green cubes, and 14 blue cubes?
def part_1(input_string):
    game_subset = input_string.split(":")[1].split(";")

    for val in game_subset:
        pattern = re.compile(r'(\d+)\s+([a-zA-Z]+)')
        matches = pattern.findall(val)

        # Iterate over the matches and check conditions
        for match in matches:
            number = int(match[0])
            color = match[1]

            # Check conditions for each color-value pair
            if (color == "red" and number > 12) or \
               (color == "green" and number > 13) or \
               (color == "blue" and number > 14):
                return False

    return True

def part_2(input_string):
    game_subset = input_string.split(":")[1].split(";")
    red = 0
    blue = 0
    green = 0
    for val in game_subset:
        pattern = re.compile(r'(\d+)\s+([a-zA-Z]+)')
        matches = pattern.findall(val)

        # Iterate over the matches and check conditions
        for match in matches:
            number = int(match[0])
            color = match[1]
            if color == "red" and red < number:
                red = number
            if color == "blue" and blue < number:
                blue = number
            if color == "green" and green < number:
                green = number

    return red * blue * green

def main():
    # For this problem, we will read one line at a time from the input file and process it
    try:
        with open("game_records.txt", "r") as file:
            sum_part1 = 0
            power_part2 = 0

            for line_number, line in enumerate(file, start=1):
                if part_1(line):
                    sum_part1 += line_number
                power_number = part_2(line)
                power_part2 += power_number

            print(f"Part_1: {sum_part1}")
            print(f"Part_2: {power_part2}")

    except FileNotFoundError:
        print("Error opening file: File not found")

if __name__ == "__main__":
    main()
