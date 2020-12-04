import re
import string

def main():
  # Prep array with passport dictionaries
  passports = []

  f = open("04input", 'r')
  line = f.readline()
  while (line):
    passport = {}
    while ((line != '\n') and line):
      pairs = line.split(' ')
      for pair in pairs:
        key_value = pair.split(':')
        passport[key_value[0]] = key_value[1].rstrip('\n')
      line = f.readline()
    passports.append(passport)
    line = f.readline()

  # Check all passports for valid fields
  correct_passports = 0
  for passport in passports:
    if all (k in passport for k in ("byr","iyr","eyr","hgt","hcl","ecl","pid")): #,"cid"
      # Check byr
      year_pattern = re.compile(r"\d{4}")
      byr = re.match(year_pattern, passport["byr"])
      byr = byr and (1920 <= int(passport["byr"]) <= 2002)

      # Check iyr
      iyr = re.match(year_pattern, passport["iyr"])
      iyr = iyr and (2010 <= int(passport["iyr"]) <= 2020)

      # Check eyr
      eyr = re.match(year_pattern, passport["eyr"])
      eyr = eyr and (2020 <= int(passport["eyr"]) <= 2030)

      # Check hgt
      hgt = False
      if(re.match(r"^[0-9]+(cm)$", passport["hgt"])):
        if (150 <= int(passport["hgt"].rstrip("cm")) <= 193):
          hgt = True

      elif(re.match(r"^[0-9]+(in)$", passport["hgt"])):
        if (59 <= int(passport["hgt"].rstrip("in")) <= 76):
          hgt = True

      # Check hcl
      hcl = False
      if (passport["hcl"][0] == '#'):
        hcl = re.match(r"^[a-f0-9]{6}$", passport["hcl"].lstrip('#'))

      # Check ecl
      ecl = re.match(r"amb|blu|brn|gry|grn|hzl|oth", passport["ecl"])
      
      # Check pid
      pid = False
      if (re.match(r"^[0-9]{9}$", passport["pid"])):
        pid = (int(passport["pid"])<1000000000)

      if byr and iyr and eyr and hgt and hcl and ecl and pid:
        correct_passports += 1

  print(correct_passports)

if __name__ == "__main__":
    main()