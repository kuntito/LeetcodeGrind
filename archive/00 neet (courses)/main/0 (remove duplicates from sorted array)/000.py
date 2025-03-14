# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

nums = [1, 1, 2, 3, 3]

start = 0
end = 0

for idx in range(1, len(nums)):
    if nums[idx] != nums[start]:
        start += 1
        nums[start] = nums[idx]

print(start)