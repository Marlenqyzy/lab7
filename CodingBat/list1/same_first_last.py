def same_first_last(nums):
  if len(nums) == 0:
    return False
  elif len(nums) == 1 or nums[0] == nums[len(nums) - 1]:
    return True
  else:
    return False