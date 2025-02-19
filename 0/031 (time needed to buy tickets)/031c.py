# https://leetcode.com/problems/time-needed-to-buy-tickets/description/

# TODO https://neetcode.io/solutions/time-needed-to-buy-tickets
class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        pass
        # every body before the kth person has to buy at most k tickets
        # before `k` can finish buying
        
        # because, it's a queue, if k is greater than `1`
        # everyone after k would have to buy at most (k - 1) times
        main_man = tickets[k]
        res = main_man
        for idx, n in enumerate(tickets):
            if idx < k:
                res += min(
                    main_man,
                    tickets[idx]
                )
            if idx > k:
                res += min(
                    main_man - 1,
                    tickets[idx]
                )
        

        return res






arr = [
    [[2,3,2], 2],
    [[5,1,1,1], 0],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.timeRequiredToBuy(foo, bar)
print(res)
