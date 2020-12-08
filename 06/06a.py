def main():
  f = open("06input", 'r')
  line = f.readline()

  groups = []
  groupindex = 0

  while line:
    groups.append(line.rstrip())
    while ((line != '\n') and line):
      for char in line:
        if char not in groups[groupindex] and char != '\n':
          groups[groupindex] += char
      line = f.readline()
    groupindex += 1
    line=f.readline()

  total = 0
  for group in groups:
    total += len(group)
  print(total)
      
  f.close()

if __name__ == "__main__":
    main()