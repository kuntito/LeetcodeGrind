from collections import Counter

def solution(chars, m):
    pass
    # split `chars` into prefix and suffix
    # check all combinations i.e. (chars[0], chars[1:]), (chars[:1], chars[2:])
    # count how many times, both splits have more than `m` characters in common
    
    rightCounter = Counter(chars)
    leftCounter = Counter()
    
    count = 0
    matches = set()
    for ch in chars:
        remove_and_clean_up(ch, rightCounter)
        
        if ch in leftCounter:
            leftCounter[ch] += 1
            if ch not in rightCounter:
                matches.remove(ch)
        else:
            leftCounter[ch] = 1
            if ch in rightCounter:
                matches.add(ch)
            
        if len(matches) > m:
            count += 1
            
    return count
        
    
def remove_and_clean_up(ch, counter):
    counter[ch] -= 1
    if counter[ch] == 0:
        del counter[ch]
        
        
arr = [
    ["abbcac", 1],
    ["adbccdbada", 2],
]
foo, bar = arr[-1]
res = solution(foo, bar)
print(res)