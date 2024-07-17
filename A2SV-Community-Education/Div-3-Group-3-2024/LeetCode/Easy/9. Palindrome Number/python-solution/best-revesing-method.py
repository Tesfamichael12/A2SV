class Solution(object):
    def isPalindrome(self, x):
        """
        :type num: int
        :rtype: bool
        """
        # reversing half of x and comparing it with the rest half of x
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        rev = 0
        while rev < x:
            rev = rev * 10 + (x % 10)
            x /= 10
        return x == rev or x == rev / 10