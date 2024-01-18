# Advent of Code 2022
# Day 10

cycles = {}
register_x = 1
cycle = 0
screen = ""
pixel_pos = 0
ROW_LENGTH = 40

def draw_pixel(register_x):
  global pixel_pos
  
  sprite_location = [register_x - 1, register_x, register_x + 1]
  if pixel_pos in sprite_location:
    pixel = '#'
  else:
    pixel = "."

  if pixel_pos >= 39:
    pixel_pos = 0
  else:
    pixel_pos += 1
  return pixel
  

with open("input.txt") as f:
    lines = f.read().splitlines()

for line in lines:
  op = line.split(" ")
  if op[0] == "addx":
    v = int(op[1])
    cycle += 1

    # Instruction begins execution,
    # taking 2 cycles

    # first cycle:
    cycles[cycle] = register_x
    screen += draw_pixel(register_x)

    cycle += 1

    # second cycle:
    cycles[cycle] = register_x
    screen = screen + draw_pixel(register_x)
    # instruction finishes execution:
    register_x += v
    
    
  else:
    cycle += 1
    # 'noop' instruction begins execution
    cycles[cycle] = register_x
    # 'noop' instruction finishes execution
    screen = screen + draw_pixel(register_x)


def signal_strength():
  x = 20
  sum = 0
  while x < 221:
    sum += x * cycles[x]
    x += 40
  return sum


print(f"Sum of signal strengths: {signal_strength()}\n")

# print the screen row by row
for i in range(0, len(screen), ROW_LENGTH):
  x = i
  print(screen[x:x+ROW_LENGTH])

