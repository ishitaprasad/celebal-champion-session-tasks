class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        p={')':'(','}':'{',']':'['}
        for i in s:
            if i in p:
                if len(stack)==0:
                    return False
                top=stack.pop()
                if top!=p[i]:
                    return False
            else:
                stack.append(i)
        if len(stack)==0:
            return True
        else:
            return False