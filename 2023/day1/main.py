import re


# Part 1 Logic
def part1():
  with open('calibration.txt', 'r', encoding='utf-8') as file:
    text = file.read()
  lines = text.strip().split("\n")
  calibration_values = [calculate_calibration_value(line) for line in lines]
  return sum(calibration_values)


def calculate_calibration_value(line):
  first_digit = re.search(r'\d', line)
  last_digit = re.search(r'\d(?=[^\d]*$)', line)
  if first_digit and last_digit:
    return int(first_digit.group() + last_digit.group())
  else:
    return 0


# Part 2 Logic
letters = [
    'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'
]


def part2():
  with open('calibration.txt', 'r') as input:
    digits = []
    for line in input:
      number = ''
      word = ''
      for ch in line:
        if ch.isdigit():
          number += ch
        elif ch.isalpha():
          word += ch
          for i in letters:
            if i in word:
              if i == 'one' or i == 'three' or i == 'five' or i == 'nine':
                number += str(letters.index(i) + 1)
                word = 'e'
              elif i == 'eight':
                number += str(letters.index(i) + 1)
                word = 't'
              elif i == 'two':
                number += str(letters.index(i) + 1)
                word = 'o'
              elif i == 'seven':
                number += str(letters.index(i) + 1)
                word = 'n'
              else:
                number += str(letters.index(i) + 1)
                word = ''
      digits.append(number)
    digits_int = []
    for num in digits:
      if len(num) == 2:
        digits_int.append(int(num))
      elif len(num) < 2 and len(num) > 0:
        num = num[0] + num[0]
        digits_int.append(int(num))
      elif len(num) > 2:
        num = num[0] + num[-1]
        digits_int.append(int(num))
    return sum(digits_int)


# Main function to execute both parts and print the results
def main():
  part1_result = part1()
  part2_result = part2()
  print(f"Part 1's result: {part1_result}")
  print(f"Part 2's result: {part2_result}")


# Execute the main function
if __name__ == "__main__":
  main()
