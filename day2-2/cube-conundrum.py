import re

f = open("day2-1/input.txt", "r")

numberpattern = re.compile(r'\d{1,3}')

sum = 0
for line in f:
  id = int(numberpattern.findall(line)[0])
  line = line.split(": ")[1]
  parts = line.split("; ")

  maxBlue = 0
  maxGreen = 0
  maxRed = 0

  for part in parts:
    part = part.split(", ")

    for x in part:
      number = int(numberpattern.findall(x)[0])
      
      if "red" in x:
        if maxRed < number:
          maxRed = number
      elif "green" in x:
        if maxGreen < number:
          maxGreen = number
      elif "blue" in x:
        if maxBlue < number:
          maxBlue = number
  sum += maxBlue*maxGreen*maxRed
print(sum)



    
  