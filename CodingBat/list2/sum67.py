def sum67(nums):
  if len(nums) == 0:
    return 0
  istree = False
  cnt = 0
  for i in nums:
    if i == 6:
      istree = True
      continue
    
    if istree == True:
      if i == 7:
        istree = False
      continue
    
    cnt += i
  return cnt
