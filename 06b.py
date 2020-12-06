def main():
  f = open("06input", 'r')
  line = f.readline()

  groups = []
  groupindex = 0

  while line:
    groups.append(line.rstrip())
    while ((line != '\n') and line):
      for given in groups[groupindex]:
        if given not in line:
          groups[groupindex] = groups[groupindex].replace(given,'')
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