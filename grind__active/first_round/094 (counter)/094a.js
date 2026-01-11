//  https://leetcode.com/problems/counter/description/

var createCounter = function (init) {
    return {
        first: parseInt(init),
        curr: parseInt(init),
        increment: function () {
            this.curr++;
            return this.curr;
        },
        decrement: function () {
            this.curr--;
            return this.curr;
        },
        reset: function () {
            this.curr = this.first;
            return this.curr;
        },
    };
};

const sol = createCounter(2);
console.log(sol.increment());
