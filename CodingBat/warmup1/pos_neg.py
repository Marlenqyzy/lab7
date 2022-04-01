def pos_neg(a, b, negative):
  ok = False 
  if a < b: a, b = b, a
  if negative == 1 and a < 0 and b < 0: ok = True
  elif negative == 0 and a > 0 and b < 0: ok = True 
  return ok