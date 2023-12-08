from itertools import tee

f = open("day3-1/input.txt", "r")

iterator1, iterator2 = tee(f)
next(iterator2)
sum = 0
prevLine = None
for x, line in enumerate(iterator1):
  try:
    next_line = next(iterator2)
  except StopIteration:
    next_line = None
  y = 0
  while y < len(line):
    if not line[y].isdigit():
      y += 1
      continue
    
    start_idx = y
    while y < len(line):
      if line[y].isdigit():
        y += 1
      else:
        end_idx = y
        break
    else:
        end_idx = len(line)

    number = line[start_idx:end_idx]
    
    # Sides dont have symbols
    left = line[start_idx-1]=="." or start_idx==0
    right = end_idx == len(line)-1 or line[end_idx]=="." 
    # Top doesn't have symbols
    top = prevLine==None or not any(char != '.' for char in prevLine[max(0,start_idx-1) : min(len(line)-1,end_idx+1)])
    # Bottom doesn't have symbols
    bot = next_line==None or not any(char != '.' for char in next_line[max(0,start_idx-1) : min(len(line)-1,end_idx+1)])

    if not (left and right and top and bot):
      sum += int(number)
  prevLine = line
      


print(sum)



    
  