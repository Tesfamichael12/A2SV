class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        # bitwise manuplation is a very fast opration for the cpu
        return n << (n & 1)
        
        # n & 1 returns 0 if n is even else returns 1
        # <<(bitwise oprator) this is a left shift oprator i.e it puts 0 at the end or LSB of the number in binary form this means basically we are multiplying it by 2 
        # so if n & 1 is 1 the n << 1, n will be shift bits of n to the left by adding 0 at the end

        