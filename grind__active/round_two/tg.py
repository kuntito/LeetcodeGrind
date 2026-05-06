def rev(chars):
    if not chars:
        return ""
    
    return chars[-1] + rev(chars[:-1])

x = rev("hello")
print(x)