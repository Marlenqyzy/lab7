def not_string(str):
    strr = str.split()
    if strr[0] == "not":
      return str
    else: return "not " + str