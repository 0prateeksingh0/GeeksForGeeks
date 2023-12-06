class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count=0
        broken=set(brokenLetters)
        for word in text.split():
            if not set(word) & broken:
                count+=1
        return count