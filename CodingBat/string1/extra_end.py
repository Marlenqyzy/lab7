def extra_end(str):
  if len(str) > 2:
    return str[len(str) - 2 : len(str)]*3
  else:
    return str*3
