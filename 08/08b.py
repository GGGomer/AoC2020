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

  nop_indices = [i for i, x in enumerate(instructions) if x == "nop"]
  jmp_indices = [i for i, x in enumerate(instructions) if x == "jmp"]

  solution_found = False
  

  for index in nop_indices:
    if not solution_found:
      new_instructions = instructions.copy()
      new_instructions[index] = "jmp"
      result = execute_program(new_instructions, instruction_values)
      if result[0]:
        solution_found = True
        print(result[1])

  for index in jmp_indices:
    if not solution_found:
      new_instructions = instructions.copy()
      new_instructions[index] = "nop"
      result = execute_program(new_instructions, instruction_values)
      if result[0]:
        solution_found = True
        print(result[1])
  
def execute_program(instructions, instruction_values):

  accumulator = 0
  visited_instructions = []

  i = 0
  while i not in visited_instructions and i < len(instructions):
    visited_instructions.append(i)
    if instructions[i] == "acc":
      accumulator += instruction_values[i]
      i += 1
    elif instructions[i] == "jmp":
      i += instruction_values[i]
    elif instructions[i] == "nop":
      i += 1

  if i == len(instructions):
    return [1, accumulator]
  else:
    return [0, accumulator]


if __name__ == "__main__":
    main()