class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sorted_num = sorted(set(nums))
        length = 1
        longest = 1
        for num in range(len(sorted_num)-1):
            if (sorted_num[num+1]- sorted_num[num]) == 1:
                length+=1
            else:
                longest = max(longest, length)
                length = 1
        return max(longest, length)
        



        
        