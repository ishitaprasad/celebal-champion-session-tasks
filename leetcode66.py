class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string=""
        for i in digits:
            string=string+str(i)
        n=int(string)
        n+=1
        ans=[]
        for j in str(n):
            ans.append(int(j))
        return ans