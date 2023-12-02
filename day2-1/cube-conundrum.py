import re

f = open("day2-1/input.txt", "r")

numberpattern = re.compile(r'\d{1,3}')

sum = 0
for line in f:
  isPossible = True
  id = int(numberpattern.findall(line)[0])

  line = line.split(": ")[1]

  parts = line.split("; ")
  print(id,"parts:", parts)
  for part in parts:
    numberColor = part.split(", ")

    for x in numberColor:
      number = int(numberpattern.findall(x)[0])
      if "red" in x:
        isPossible = number <= 12
      elif "green" in x:
        isPossible = number <= 13
      elif "blue" in x:
        isPossible = number <= 14
      if not isPossible:
        break

    if not isPossible:
      print("not possible!")
      break  
  if isPossible:
    sum += id

print(sum)



    
  