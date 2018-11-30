count = 0;
for i in range (len(input)):
  if(i == len(input) - 1):
    if(input[i] == input[0]):
      count += int(input[i]);
  elif(input[i] == input[i+1]):
    count += int(input[i]);
print(count);

#part 2
i2 = input + input;
count = 0;
for i in range (len(input)):
  if(i2[i] == i2[i + int(len(input)/2)]):
    count += int(i2[i]);
print(count);
