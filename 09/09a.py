
def main():
  f = open("09/09input", 'r')

  numbers = []
  
  line = f.readline()
  while line:
    numbers.append(int(line.rstrip()))

    line = f.readline()
  preamble_size = 25

  number_found = False
  
  for number_to_check in range(preamble_size, len(numbers)):
    if not number_found:
      preamble_first = number_to_check - preamble_size
      preamble_last = preamble_first + preamble_size
      
      sum_found = False
      for j in range(preamble_first, preamble_last):
        if not sum_found:
          for k in range(j+1, preamble_last):
            if not sum_found:
              if numbers[j]+numbers[k] == numbers[number_to_check]:
                sum_found = True
      if not sum_found: 
        number_found = True
        print(numbers[number_to_check])
    
if __name__ == "__main__":
    main()