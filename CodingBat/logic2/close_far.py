def close_far(a, b, c):
  if (abs(a - c) <= 1 and abs(a - b) >= 2) or (abs(a - b) <= 1 and abs(a - c) >= 2):
    if abs(b - c) == 1:
      return False
    else:
      return True
  else:
    return False
