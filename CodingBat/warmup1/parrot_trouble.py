def parrot_trouble(talking, n):
    if talking == True:
        if n < 7 or 20 < n <= 23:
            return True
        else: 
            return False
    else:
        if n >= 7 or 20 > n:
            return False
        else: 
            return True