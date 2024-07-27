class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        new_arr = [0] * len(arr)
        maxval = new_arr[-1]
        new_arr[-1] = -1

        for i in range(len(arr) - 2, -1, -1):
            print(i)
            maxval = max(maxval, arr[i + 1])
            new_arr[i] = maxval
        
        return new_arr

