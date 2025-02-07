# TODO intuition?
def count_contiguous_sub_arrays(n):
    count = 0
    
    for i in range(n):
        count += (i + 1)
        
    return count

a = count_contiguous_sub_arrays(3)
print(a)