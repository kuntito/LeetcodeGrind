# https://leetcode.com/problems/sum-of-two-integers/description/

# what happens when a = 1 and b = 2

# class Solution {
#     public int getSum(int a, int b) {
#         while (b != 0) {
#             int andResult = a & b;
#             b = a ^ b;

#             a = andResult << 1;
#             if (andResult == 0) return b;
#         }
#         return a;
#     }
# }

# class Solution {
#     public int getSum(int a, int b) {
#         while(b != 0) {
#             int temp = (a & b) << 1;
#             a = a ^ b;
#             b = temp;
#         }
#         return a;
#     }
# }