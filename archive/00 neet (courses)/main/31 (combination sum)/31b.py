class Solution:
    def combinationSum(self, candidates: list, target: int) -> list:
        res = []

        def dfs(index, sublist, total):
            if total == target:
                res.append(sublist.copy())
                return

            if index >= len(candidates) or total > target:
                return
            
            item = candidates[index]

            sublist.append(item)
            dfs(index, sublist, total + item)
            sublist.pop()

            dfs(index + 1, sublist, total)

        dfs(0, [], 0)

        return res


lst = [2, 3, 6, 7]
foo = Solution()
bar = 7
res = foo.combinationSum(lst, bar)

print(res)