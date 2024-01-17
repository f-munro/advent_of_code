# Advent of Code 2022
# Day 10

cycles = {}
register_x = 1
cycle = 0

def addx(v):
  global cycle
  global register_x

  cycle += 1
  # 'addx' instruction begins execution,
  # taking 2 cycles.

  # first cycle:
  cycles[cycle] = register_x

  cycle += 1
  # second cycle:
  cycles[cycle] = register_x

  # instruction finishes execution:
  register_x += v
  

with open("input.txt") as f:
    lines = f.read().splitlines()

for line in lines:
  operation = line.split(" ")
  if operation[0] == "addx":
    v = int(operation[1])
    addx(v)
  else:
    cycle += 1
    # 'noop' instruction begins execution
    cycles[cycle] = register_x
    # 'noop' instruction finishes execution


def signal_strength():
  x = 20
  sum = 0
  while x < 221:
    sum += x * cycles[x]
    x += 40
  return sum


print(f"Sum of signal strengths: {signal_strength()}")

