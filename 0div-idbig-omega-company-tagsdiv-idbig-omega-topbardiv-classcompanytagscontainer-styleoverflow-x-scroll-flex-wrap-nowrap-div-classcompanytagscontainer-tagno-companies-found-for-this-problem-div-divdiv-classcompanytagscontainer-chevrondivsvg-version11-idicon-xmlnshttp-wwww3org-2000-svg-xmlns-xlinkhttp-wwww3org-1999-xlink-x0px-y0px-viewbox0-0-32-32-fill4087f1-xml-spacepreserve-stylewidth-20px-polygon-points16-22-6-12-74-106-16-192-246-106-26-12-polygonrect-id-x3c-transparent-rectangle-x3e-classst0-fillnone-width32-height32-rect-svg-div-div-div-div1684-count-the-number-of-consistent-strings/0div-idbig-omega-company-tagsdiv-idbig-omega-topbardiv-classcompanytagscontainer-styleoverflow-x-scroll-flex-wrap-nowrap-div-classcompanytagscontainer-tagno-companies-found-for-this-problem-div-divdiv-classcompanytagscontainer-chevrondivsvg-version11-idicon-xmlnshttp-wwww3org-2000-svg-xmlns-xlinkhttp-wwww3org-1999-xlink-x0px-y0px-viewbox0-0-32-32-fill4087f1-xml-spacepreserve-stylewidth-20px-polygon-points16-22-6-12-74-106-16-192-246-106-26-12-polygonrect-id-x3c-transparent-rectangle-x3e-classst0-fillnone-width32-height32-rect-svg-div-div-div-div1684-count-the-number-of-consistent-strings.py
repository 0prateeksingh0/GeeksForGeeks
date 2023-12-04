class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        counts = 0
        for word in words:
            temp = set()
            for i in word:
                temp.add(i)
            for i in temp:
                if i not in allowed:
                    break
            else:
                counts += 1
        return counts
        