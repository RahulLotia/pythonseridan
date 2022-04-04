def string_encrypt(s):
    stringlength=len(s)
    slicedString=s[stringlength::-1]
    return slicedString+s