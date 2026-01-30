def rle(strings):
    res=[]
    for i in strings:
        j=0
        ans=""
        while j<len(i):
            count=1
            while (j+1<len(i)) and (i[j]==i[j+1]):
                count+=1
                j+=1
            ans+=str(count)+i[j]
            j+=1
        res.append(ans)
    return res
strings=["aaaabbbccc", "aabbbcc", "aaabcccc"]
print(rle(strings))
