// https://leetcode.com/problems/apply-transform-over-each-element-in-array/


var map = function(arr, fn) {
    const res = [];
    for (let i = 0; i < arr.length; i++) {
        // Apply fn directly
        const val = fn(arr[i], i);
        res.push(val);
    }
    return res;
};
