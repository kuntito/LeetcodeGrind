# https://leetcode.com/problems/combination-sum/description/

class Solution:
    def combinationSum(self, candidates: list, target: int) -> list:
        candidates.sort()
        sublist = []

        master_list = []
        self.get_sums(0, target, candidates, sublist, master_list)
        return master_list
    

    def get_sums(
        self,
        index,
        elem,
        candidates,
        sublist,
        master_list,
    ):
        if elem == 0:
            master_list.append(sublist.copy())
            return

        for idx in range(index, len(candidates)):
            cand = candidates[idx]
            if cand > elem: break

            sublist.append(cand)
            self.get_sums(idx, elem-cand, candidates, sublist, master_list)
            sublist.pop()




lst = [2, 3, 5]
foo = Solution()
res = foo.combinationSum(lst, 8)

print(res)

