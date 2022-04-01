def max_end3(nums):
    cnt = 0
    if nums[0] > nums[len(nums) - 1]:
        cnt = nums[0]
    else:
        cnt = nums[len(nums) - 1]
    for i in range(0, 3):
        nums[i] = cnt
    return nums