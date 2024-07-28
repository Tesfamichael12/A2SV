class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        i = 0
        # wlak up
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1
        
        # peak cannot be the first or the last
        if i == 0 or i == n - 1:
            return False
        
        # walk down
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1
        
        return i == n - 1