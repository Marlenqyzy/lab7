def array123(nums):
    text = ""
    for i in nums:
        text += str(i)

    if( text.find("123") != -1): return True
    return False