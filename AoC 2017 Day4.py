count = 0;
for phrase in input:
  if(len(phrase.split()) == len(set(phrase.split()))):
    count += 1;
print(count)

#Part 2 

count = 0;
for phrase in input:
  wlist = phrase.split();
  for i in range(len(wlist)):
    wlist[i] = ''.join(sorted(wlist[i]))
  if(len(wlist) == len(set(wlist))):
    count += 1;
print(count)
