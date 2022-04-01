def string_match(a, b):
    cnt = 0
    for i in range(1, len(a)):
      for j in range(1, len(b)):
        if a[i-1:i+1] == b[j-1:j+1] and i == j: cnt += 1
    return cnt
