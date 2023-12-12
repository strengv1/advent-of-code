f = open("day4-1/input.txt", "r")

sum = 0
for x, line in enumerate(f):
  line = line.split(": ")[1].strip()
  parts = line.split(" | ")

  winningNumbers = parts[0].split(" ")
  winningNumbers = [i for i in winningNumbers if i]

  myNumbers = parts[1].split(" ")
  myNumbers = list(filter(None, myNumbers))

  points = 0
  for num in winningNumbers:
    if num in myNumbers:
      points = 1 if points == 0 else points*2

  sum += points

print(sum)
  
      



    
  