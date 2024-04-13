import os

def part1():
  user_input = input("请输入你的文件路径: ")
  if not os.path.exists(user_input):
      print("文件不存在")
      exit(0)
  total = 2020
  f = open(user_input)
  numbers = set()
  for line in f:
    line = line.strip().replace("\n", "").replace("\r", "")
    num = int(line)
    diff = total - num 
    if diff in numbers:
      print(diff * num)
    else:
      numbers.add(num)
  return 0

def part2():
  user_input = input("请输入你的文件路径: ")
  if not os.path.exists(user_input):
    print("文件不存在")
    exit(0)
  f = open(user_input)
  numbers = list()
  for line in f:
    line = line.strip().replace("\n", "").replace("\r", "")
    numbers.append(int(line))
    numbers.sort()
  for start in range(0, len(numbers)):
    mid = start + 1
    end = len(numbers) - 1
    while mid < end:
      sum = numbers[start] + numbers[mid] + numbers[end]
      if sum == 2020:
        print(numbers[start] * numbers[mid] * numbers[end])
        break
      elif sum < 2020:
        mid += 1
      else:
        end -= 1

def main():
  user_input = input("你想知道哪一部分的答案(可选1,2,all): ")
  if user_input == "1":
    part1()
  elif user_input == "2":
    part2()
  elif user_input == "all":
    part1()
    part2()
  else:
    print("错误的选择,成功退出...")
  
if __name__ == "__main__":
  main()