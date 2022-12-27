class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        x = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                i += 1
            else:
                break

        for j in range(i, -1, -1):
            if s[j] == " ":
                break
            else:
                x += 1

        return x