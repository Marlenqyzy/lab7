def make_ends(nums):
  if len(nums) == 1:
    a = [nums[0], nums[0]]
    return a
  else:
    a = [nums[0], nums[len(nums) - 1]]
    return a
  