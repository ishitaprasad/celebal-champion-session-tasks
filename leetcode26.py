class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique=[]
        for i in nums:
            if i not in unique:
                unique.append(i)
        nums.clear()
        for i in unique:
            nums.append(i)
        return len(nums)