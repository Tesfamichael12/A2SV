class Solution(object):
    def isPalindrome(self, num):
        """
        :type num: int
        :rtype: bool
        """
    # using extra while loop to get the 10th place
    # Time complexity = O(2n) = O(n)  Space complexity = O(1)
        if num < 0:
            return False 
        div = 1
        while num // div >= 10:
            div *= 10
     
        while not(num == 0):
            L = num // div
            R = num % 10
            if not(L == R):
                return False
            num = (num % div) // 10
            div /= 100
        return True
    