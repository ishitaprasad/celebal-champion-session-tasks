class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            digits=0
            digits=len(str(abs(i)))
            if (digits%2==0):
                count+=1
        return count