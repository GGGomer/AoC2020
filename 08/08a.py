def main():
  f = open("08input", 'r')
  instructions = []
  instruction_values = []

  line = f.readline()

  while line:
    split_line = line.split()
    instructions.append(split_line[0])
    instruction_values.append(int(split_line[1]))
    line = f.readline()

  accumulator = 0
  visited_instructions = []

  i = 0
  while i not in visited_instructions:
    if i > highest_instruction: highest_instruction = i
    visited_instructions.append(i)
    if instructions[i] == "acc":
      accumulator += instruction_values[i]
      i += 1
    elif instructions[i] == "jmp":
      i += instruction_values[i]
    elif instructions[i] == "nop":
      i += 1
  
  print(accumulator)

if __name__ == "__main__":
    main()