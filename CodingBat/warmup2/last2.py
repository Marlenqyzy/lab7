def last2(str):
  text = str[len(str)-2:len(str)]
  n = 0
  for i in range(1, len(str)-1):
    if str[i-1:i+1] == text: n += 1
  return n