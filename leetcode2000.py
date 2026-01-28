class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        x=word.find(ch)
        prefix=word[:x+1]
        suffix=word[x+1:]
        return prefix[::-1]+suffix