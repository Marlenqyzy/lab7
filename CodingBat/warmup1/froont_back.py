def front_back(str):
  
  text = ""
  
  for i in range(len(str)):
    if i == 0 or i == len(str) - 1:
      text += str[len(str) - i - 1]
    else:
      text += str[i]
      
  return text