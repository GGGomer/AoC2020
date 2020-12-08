class Rule:
  def __init__(self, color, can_contain):
    self.color = color
    self.can_contain = can_contain

def parse_line_to_rule(line):
  
  own_color_split = line.split(" bags contain ")
  color = own_color_split[0]

  can_contain = {}
  sub_bags = own_color_split[1].split(", ")
  for bag_rule in sub_bags:
    words = bag_rule.split()
    if(words[0] != "no"):
      bag_color = words[1] + " " + words[2]
      can_contain[bag_color] = int(words[0])
  return Rule(color, can_contain)

def find_rule(rule_color, rules):
  for rule in rules:
    if rule.color == rule_color:
      return rule

def can_bag_contain(color, rule, rules):
  result = False
  if rule.can_contain:
    if color in rule.can_contain:
      result = True
    else:
      for new_rule_color in rule.can_contain:
        if not result:
          new_rule = find_rule(new_rule_color, rules)
          result = can_bag_contain(color, new_rule, rules)
  return result

def calc_bags_in_bag(rule, rules):
  total = 1

  for new_rule_color in rule.can_contain:
    new_rule = find_rule(new_rule_color, rules)
    total += calc_bags_in_bag(new_rule, rules ) * rule.can_contain[new_rule_color]

  return total

def main():
  f = open("07input", 'r')
  rules = []

  line = f.readline()
  while (line):
    rules.append(parse_line_to_rule(line.rstrip()))
    line = f.readline()

  rule = find_rule("shiny gold", rules)
  print(calc_bags_in_bag(rule, rules) - 1)

if __name__ == "__main__":
    main()



  
  