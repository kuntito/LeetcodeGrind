arr = ["30", "3", "34"]

arr.sort(key=lambda x: (len(x), -int(x)))

print(arr)