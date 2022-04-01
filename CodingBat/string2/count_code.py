def end_other(a, b):
  if len(b) > len(a):
    a, b = b, a
  if a[len(a) - len(b) : len(a)].lower() == b.lower():
    return True
  return False
    
