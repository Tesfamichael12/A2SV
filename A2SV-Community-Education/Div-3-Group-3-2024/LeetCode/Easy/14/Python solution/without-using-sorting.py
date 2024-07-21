class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Time Complexity : O(n * L + L short) = O(n * L)  
        shortest = strs[0]
        longest = strs[0]

        for strs in strs:
            shortest = strs if shortest > strs else shortest
            longest = strs if longest < strs else longest
        
        i = 0
        while i < len(shortest):
            if longest[i] != shortest[i]:
                return longest[:i] # or shortest[:i] same
            i +=1
        return longest[:i]
            




# NOTE
# Better Time Complexity
# Time Complexity : O(n * L + L short) = O(n * L)  
# where n is the size of strs and L is the avarage size of each string, L short is the length of the shortest string
# # when comparing two integers TC is O(1), but for strings TC will be O(L),  since we are comparing each characters of the strings, wher L is the avarage size of the strings.

# Space Complexity : O(1) 