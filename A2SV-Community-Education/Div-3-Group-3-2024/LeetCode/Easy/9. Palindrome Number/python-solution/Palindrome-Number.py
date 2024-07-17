class Solution(object):
    def isPalindrome(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # Using the two pointers technique 
        # this solution is better because it does not use another while loop, it just uses one while loop 
        # Time complexity = O(n) , Space complexity = O(1)
        if num < 0:
            return False
        num = str(num) # first change the integer  number to string to access each digit with their idex
        L, R = 0, len(num) - 1
        while L < R:
            if num[L] != num[R]:
                return False
            L += 1
            R -= 1
        return True