// https://leetcode.com/problems/function-composition/description/

var compose = function(functions) {
    
    return function(x) {
        const dim = functions.length;
        let res = x;
        for (let i = dim - 1; i >= 0; i--) {
            const fn = functions[i];
            res = fn(res);
        }
        
        return res;
    }
};
