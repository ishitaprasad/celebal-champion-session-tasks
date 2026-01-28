class Solution:
    def capitalizeTitle(self, title: str) -> str:
        l=title.split()
        ans=[]
        for i in l:
            if len(i)<=2:
                ans.append(i.lower())
            else:
                ans.append(i.capitalize())
        return " ".join(ans)