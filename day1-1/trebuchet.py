
f = open("day1-1/input.txt", "r")

sum = 0
for line in f:
  nums = ""
  for char in line:
    if char.isdigit():
       nums += char
       break
    
  for char in reversed(line):
    if char.isdigit():
       nums += char
       break
  sum += int(nums)
print(sum)