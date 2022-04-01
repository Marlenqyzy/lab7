def sum13(nums):
  istree = False
  cnt = 0
  
  for i in nums:
    if i == 13:
      istree = True
      continue
    
    if istree == True:
      istree = False
      continue
    
    cnt += i
  return cnt