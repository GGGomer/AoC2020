import re
def main():
  f = open("05input", 'r')
  boarding_passes = f.read().splitlines()

  # Get seat_id's for all boarding passes
  seat_ids = []
  
  for boarding_pass in boarding_passes:

    row = calculate_sequence_value(decode_sequence('F', 'B', boarding_pass))
    column = calculate_sequence_value(decode_sequence('L', 'R', boarding_pass))
    seat_id = row*8+column
    seat_ids.append(seat_id)

  # Look for my seat
  my_seat_id = 0

  seat_ids.sort()

  for i in range(len(seat_ids)-1):
    if (seat_ids[i+1] != seat_ids[i]+1): my_seat_id = seat_ids[i]+1
  
  print(my_seat_id)


def decode_sequence(char_lower, char_higher, sequence):

  clean_sequence = re.sub(r"[^"+re.escape(char_lower)+re.escape(char_higher)+"]", '', sequence)
  new_sequence = []

  for character in clean_sequence:
    if character == char_lower:
      new_sequence.append(False)
    elif character == char_higher:
      new_sequence.append(True)
  return new_sequence


def calculate_sequence_value(sequence):
  sequence_value = 0
  
  if sequence[0]:
    sequence_value = 2**(len(sequence)-1)
  
  cut_sequence = sequence[1:]
  if cut_sequence:
    sequence_value += calculate_sequence_value(cut_sequence)

  return sequence_value
    

if __name__ == "__main__":
    main()