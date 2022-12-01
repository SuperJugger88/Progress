class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        return [idx for idx,el in enumerate(nums) if el != sum(nums) - target and target - el in nums]
        

sol = Solution()
print(sol.twoSum([2,7,11,15],9))
print(sol.twoSum([2,4,3],6))