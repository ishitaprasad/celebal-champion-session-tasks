class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=""
        i=0
        n=len(word1)
        m=len(word2)
        while i<m or i<n:
            if i<n:
                ans=ans+word1[i]
            if i<m:
                ans=ans+word2[i]
            i+=1
        return ans   