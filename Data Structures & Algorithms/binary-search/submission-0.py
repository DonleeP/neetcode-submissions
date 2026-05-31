class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        count=0
        for n in range(len(nums)):
            if nums[n] == target:
                return count
            count+=1