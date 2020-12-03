import re

def main():
  f = open("./02input", 'r')
  line = f.readline()

  lowest_indices = []
  highest_indices = []
  characters = []
  passwords = []

  # Loop through all lines
  while line:
    # deconstruct line into elements for lists
    decimals = re.findall(r'\d+', line)
    lowest_indices.append(int(decimals[0]))
    highest_indices.append(int(decimals[1]))
    characters.append(re.search(r'[a-z]', line).group())
    passwords.append(re.sub('\n',"",re.split(": ", line)[1]))

    # Next line
    line = f.readline()

  # Assert if arrays are of same length
  assert len(passwords) == len(lowest_indices)
  assert len(passwords) == len(highest_indices)
  assert len(passwords) == len(characters)

  # Count correct passwords
  correct_passwords = 0
  for i in range(len(passwords)):

    if((passwords[i][lowest_indices[i]-1] == characters[i])^(passwords[i][highest_indices[i]-1] == characters[i])):
      correct_passwords += 1

  print(correct_passwords)

if __name__ == "__main__":
    main()
