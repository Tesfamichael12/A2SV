class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        count= 0
        for i in range(1, len(arr)):
            if arr[0] > arr[1] or arr[i - 1] == arr[i]:
                return False
            if arr[i - 1] > arr[i]:
                count += 1
                for j in range(i + 1, len(arr)):
                    if arr[j - 1] <= arr[j]:
                        return False
                break
                
        return True if count >= 1 else False