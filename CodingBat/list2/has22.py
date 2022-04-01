def has22(nums):
  i = 0
  
  for i in range(len(nums) - 1):
    if nums[i] == 2:
      if nums[i + 1] == 2:
        return True
  return False