def big_diff(nums):
  max = -100000
  min = 100000
  
  for i in nums:
    if i > max:
      max = i
    if i < min:
      min = i
  return max - min 
