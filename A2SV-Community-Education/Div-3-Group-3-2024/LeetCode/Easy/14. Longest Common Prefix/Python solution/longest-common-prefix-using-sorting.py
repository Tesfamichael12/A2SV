class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Time Complexity : O(n * L * log n + L min )   = O(n * L * log n )
        strs.sort()
        longestPr = ""
        first = strs[0]
        last = strs[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return longestPr
            longestPr += first[i]
        return longestPr
        


# NOTE
#         [ Time taken: 1 hr ]
# Time Complexity : O(n * L * log n + L min )   = O(n * L * log n )
# where n is the size of strs and L is the avarage size of each string 
# # sorting takes TC n * log n in general but if the list to be sorted is a list of strings the the TC changes to n * L * log n where L is the avarage length of each string element.

# Space Complexity : O(1) 