def main():
  f = open("./01input", "r")
  input_list = []
  line = f.readline()
  while line:
    input_list.append(int(line))
    line = f.readline()
  f.close()
  print(input_list)

  firstindex = 0

  while (firstindex != len(input_list)):
      secondindex = firstindex +1

      while (secondindex != len(input_list)):

        thirdindex = secondindex +1
        while (thirdindex !=len(input_list)):
          if (input_list[firstindex] + input_list[secondindex] + input_list[thirdindex]!= 2020):
            thirdindex +=1 
          else:
            print(input_list[firstindex] * input_list[secondindex] * input_list[thirdindex])
            break
        secondindex += 1
      firstindex += 1

if __name__ == "__main__":
    main()