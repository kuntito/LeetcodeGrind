# https://leetcode.com/problems/unique-email-addresses/description/


class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        seen = set()

        for em in emails:
            # local, domain = em.split('@')
            local, domain = self.get_local_and_domain(em)
            
            newLocal = []
            for ch in local:
                if ch == '.': continue
                if ch == '+': break
                newLocal.append(ch)

            newLocal = "".join(newLocal)

            item = (newLocal, domain)
            seen.add(item)

        return len(seen)
    
    def get_local_and_domain(self, email):
        plus = '+'
        at = "@"

        local, domain = "", ""

        at_found = False
        plus_found = False
        for ch in email:
            if ch == at:
                at_found = True
            elif ch == plus:
                plus_found = True
            elif at_found:
                domain += ch
            elif not plus_found:
                local += ch

        return local, domain
            


arr = [
    ["a@leetcode.com","b@leetcode.com","c@leetcode.com"],
    ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"],
]
foo = arr[-1]
sol = Solution()

res = sol.numUniqueEmails(foo)
print(res)

