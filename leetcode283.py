class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        zeroes=[]
        for i in nums:
            if i==0:
                zeroes.append(i)
        for j in zeroes:
            nums.remove(j)
        nums.extend(zeroes)
        