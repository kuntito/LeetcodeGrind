# https://leetcode.com/problems/unique-email-addresses/description/


class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        email_map = {}

        count = 0
        for m in emails:
            local, domain = m.split('@')

            if domain not in email_map:
                email_map[domain] = set()

            plus = '+'
            period = '.'
            if plus in local:
                local = local.split(plus)[0]

            if period in local:
                local = local.replace(period, '')

            if local not in email_map[domain]:
                email_map[domain].add(local)
                count += 1
                

        # print(email_map)

        return count
    

arr = [
    ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"],
    ["a@leetcode.com","b@leetcode.com","c@leetcode.com"],
]
foo = arr[-1]
sol = Solution()

res = sol.numUniqueEmails(foo)
print(res)