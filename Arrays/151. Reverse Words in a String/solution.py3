import typing


class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        sList = s.split(' ')
        resStr = ""
        print(sList)

        for i in range(len(sList)-1, -1, -1):
            if sList[i] == '':
                con
            resStr += sList[i] + " "


        return resStr.strip()


print(Solution.reverseWords("", "a good   example"))
