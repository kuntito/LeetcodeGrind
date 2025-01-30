# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/description/

# TODO https://www.youtube.com/watch?v=9vAQdmVU2ds
class Solution:
    def minOperations(self, s: str) -> int:
        zero_count = 0
        one_count = 0

        # the question, is it cheaper if the string starts with a `0` or starts with a `1`?
        # if it starts with a zero,
        # every even index should have `0` and every odd index should have `1`
        # to check if it starts with a zero, you go through every element
        # if the index, `idx` is even and the character, `ch` is `1`:
        # increment `zero_count` by 1
        # it the index, `idx` is odd and the caracter, `ch` is `0`:
        # increment `zero_count` by 1
        for idx, ch in enumerate(s):
            pass
            