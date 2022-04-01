def left2(str):
  if len(str) < 3:
    return str
  else:
    text = ""
    for i in range(2, len(str)):
      text += str[i]
    text += str[0:2]
    return text
