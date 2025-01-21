// https://leetcode.com/problems/array-reduce-transformation/description/

var reduce = function(nums, fn, init) {
    let prev = init;
    for (let i = 0; i < nums.length; i++) {

        prev = fn(prev, nums[i]);
    }

    return prev;
};