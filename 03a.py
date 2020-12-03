import math

def main():
  f = open("03input", 'r')
  rows = f.read().splitlines()

  encountered_trees = [0,0,0,0,0]

  for i in range(1, len(rows)):
    if (rows[i][i%len(rows[i])] == "#"):
      encountered_trees[0] += 1
    
    if (rows[i][i*3%len(rows[i])] == "#"):
      encountered_trees[1] += 1
    
    if (rows[i][i*5%len(rows[i])] == "#"):
      encountered_trees[2] += 1
    
    if (rows[i][i*7%len(rows[i])] == "#"):
      encountered_trees[3] += 1
    
    if (i <= math.floor((len(rows)/2))):
      if (rows[i*2][i%len(rows[i])] == "#"):
        encountered_trees[4] += 1

  total_trees = 1
  for trees in encountered_trees:
    total_trees *= trees
  
  print(total_trees)
  
if __name__ == "__main__":
    main()