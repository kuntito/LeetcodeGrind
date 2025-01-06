a = [[1,15,6,8,18,14,16,2,19,17,3,20,5], [8,5,5,7,10,10,7,9,3,4,4,10,2]]

res = []
for one, two in zip(a[0], a[1]):
    res.append((one, two))
    
res.sort()


for pos, sp in res:
    print(sp)