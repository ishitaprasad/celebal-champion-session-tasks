class Solution:
    def romanToInt(self, s: str) -> int:
        n=len(s)
        x=0
        nums={"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for i in range(n):
            curr=nums[s[i]]
            if (i+1<n) and (curr<nums[s[i+1]]):
                x=x-curr
            else:
                x=x+curr
        return x
