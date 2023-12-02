
f = open("day1-2/input.txt", "r")

sum = 0
for line in f:
  nums = ""
  for i in range(len(line)):
    if line[i].isdigit():
      nums += line[i]
      break
    elif line[i:i+4] == "zero":
      nums += "0"
      break
    elif line[i:i+3] == "one":
      nums += "1"
      break
    elif line[i:i+3] == "two":
      nums += "2"
      break
    elif line[i:i+5] == "three":
      nums += "3"
      break
    elif line[i:i+4] == "four":
      nums += "4"
      break
    elif line[i:i+4] == "five":
      nums += "5"
      break
    elif line[i:i+3] == "six":
      nums += "6"
      break
    elif line[i:i+5] == "seven":
      nums += "7"
      break
    elif line[i:i+5] == "eight":
      nums += "8"
      break
    elif line[i:i+4] == "nine":
      nums += "9"
      break
    
  for i, char in reversed(list(enumerate(line))):
    if char.isdigit():
      nums += char
      break
    elif line[i-4:i] == "zero":
      nums += "0"
      break
    elif line[i-3:i] == "one":
      nums += "1"
      break
    elif line[i-3:i] == "two":
      nums += "2"
      break
    elif line[i-5:i] == "three":
      nums += "3"
      break
    elif line[i-4:i] == "four":
      nums += "4"
      break
    elif line[i-4:i] == "five":
      nums += "5"
      break
    elif line[i-3:i] == "six":
      nums += "6"
      break
    elif line[i-5:i] == "seven":
      nums += "7"
      break
    elif line[i-5:i] == "eight":
      nums += "8"
      break
    elif line[i-4:i] == "nine":
      nums += "9"
      break
  sum += int(nums)
print(sum)
    


