def string_bits(str):
    text = ""

    for i in range(len(str)):
        if i % 2 == 0: 
            text += str[i]
    return text