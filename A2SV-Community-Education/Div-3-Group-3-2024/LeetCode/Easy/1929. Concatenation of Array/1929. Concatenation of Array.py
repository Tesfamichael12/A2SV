class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums[:]
        [ans.append(n) for n in nums]
        return ans

        # nums.extend(nums)
        # return nums

        # return nums + nums

        # return nums *2

