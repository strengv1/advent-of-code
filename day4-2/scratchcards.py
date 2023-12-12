f = open("day4-1/input.txt", "r")

amountOfCards = 0
copies = [0] * 220

for x, line in enumerate(f):
  line = line.split(": ")[1].strip()
  parts = line.split(" | ")

  winningNumbers = parts[0].split(" ")
  winningNumbers = [i for i in winningNumbers if i]

  myNumbers = parts[1].split(" ")
  myNumbers = list(filter(None, myNumbers))

  matches = 0
  for num in winningNumbers:
    if num in myNumbers:
      matches += 1

  for i in range(matches):
    copies[1+x+i] += 1+copies[x]
  
for count in copies:
  amountOfCards += 1+count

print(amountOfCards)
  
      



    
  