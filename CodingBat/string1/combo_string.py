def combo_string(a, b):
  if len(a) < len(b): a, b = b, a
  return b+a+b