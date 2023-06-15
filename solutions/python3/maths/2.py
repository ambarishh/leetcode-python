# 9. Palindrome Number
# https://leetcode.com/problems/palindrome-number/description/

class Solution:
    def isPalindrome(self, x: int) -> bool:

        #not a palindrome if x is negative or has zero in end
        if x<0 or (x%10==0 and x!=0):
            return False

        reversed_x=0
        while x>reversed_x:
            reversed_x = reversed_x*10 + x%10
            x = x//10

        #if even digits or odd digits
        return x==reversed_x or (x==reversed_x//10)