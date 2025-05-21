chars = "abbc"

res = []

idx = 0
count = 1
while idx < len(chars):
    ch = chars[idx]
    if not res or ch != res[-1]:
        res.append(ch)
        
    if idx + 1 == len(chars) or ch != chars[idx + 1]:
        res.append(str(count))
        count = 0
    count += 1
    idx += 1
    
x = "".join(res)
print(x)
    