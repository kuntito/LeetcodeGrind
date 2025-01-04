# https://leetcode.com/problems/unique-email-addresses/description/


class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        seen = set()

        for em in emails:
            local, domain = em.split('@')
            # write a loop that iterates through `local` appending each
            # char to a new variable called `newLocal`
            # skipping periods and shortcircuits if it finds `+`

            newLocal = []
            for ch in local:
                if ch == '.': continue
                if ch == '+': break
                newLocal.append(ch)

            newLocal = "".join(newLocal)

            item = (newLocal, domain)
            seen.add(item)

        return len(seen)
    

arr = [
    ["a@leetcode.com","b@leetcode.com","c@leetcode.com"],
    ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"],
]
foo = arr[-1]
sol = Solution()

res = sol.numUniqueEmails(foo)
print(res)

