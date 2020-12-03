import re

def main():
  f = open("./02input", 'r')
  line = f.readline()

  lowest_numbers = []
  highest_numbers = []
  characters = []
  passwords = []

  # Loop through all lines
  while line:
    # deconstruct line into elements for lists
    decimals = re.findall(r'\d+', line)
    lowest_numbers.append(int(decimals[0]))
    highest_numbers.append(int(decimals[1]))
    characters.append(re.search(r'[a-z]', line).group())
    passwords.append(re.sub('\n',"",re.split(": ", line)[1]))

    # Next line
    line = f.readline()

  # Assert if arrays are of same length
  assert len(passwords) == len(lowest_numbers)
  assert len(passwords) == len(highest_numbers)
  assert len(passwords) == len(characters)

  # Count correct passwords
  correct_passwords = 0
  for i in range(len(passwords)):
    amt = passwords[i].count(characters[i])
    if (lowest_numbers[i] <= amt <= highest_numbers[i]):
      correct_passwords += 1

  print(correct_passwords)

if __name__ == "__main__":
    main()
