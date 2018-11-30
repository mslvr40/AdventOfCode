count = 0;
for i in range(len(input)):
  high = 0;
  low = 9999;
  for j in range(len(input[i])):
    if(input[i][j] < low):
      low = input[i][j];
    if(input[i][j] > high):
      high = input[i][j];
  count += high - low;
print(count)

#part two

count = 0;
for i in range(len(input)):
  
  for j in range(len(input[i])):
    for x in range(len(input[i])):
      if(x == j):
        continue;
      if(input[i][j] % input[i][x] == 0):
        count+= input[i][j] / input[i][x];
        break;
  
print(count)
