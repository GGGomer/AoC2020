
def main():
  f = open("09/09input", 'r')

  numbers = []
  
  line = f.readline()
  while line:
    numbers.append(int(line.rstrip()))

    line = f.readline()
  
  target = 2089807806 #use 09a to find target
  # target = 127 #use 09a to find target
  sequence_found = False

  current_index = 0
  for start in numbers: 
    if not sequence_found:
      if not current_index == len(numbers) -1:
        total = start
        added_numbers = [start]
        add_index = current_index +1
        while total < target:
          total += numbers[add_index]
          added_numbers.append(numbers[add_index])
          add_index +=1
        if total == target:
          sequence_found = True
          added_numbers.sort()
          print(added_numbers[0] + added_numbers[len(added_numbers)-1])



      current_index += 1
if __name__ == "__main__":
    main()