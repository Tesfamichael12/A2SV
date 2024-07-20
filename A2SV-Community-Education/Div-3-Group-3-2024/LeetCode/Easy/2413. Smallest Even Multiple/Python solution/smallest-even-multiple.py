class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n & 1 ^ 1: # check if n is even
            return n
        return n * 2
        