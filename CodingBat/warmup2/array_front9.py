def array_front9(nums):
  ok = False 
  for i in range(len(nums)):
    if i < 4 and nums[i] == 9: ok = True
  return ok
  