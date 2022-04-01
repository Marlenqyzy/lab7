def string_splosion(str):
  text = ""
  for i in range(1, len(str)+1):
    text = text + str[0:i]
  return text
