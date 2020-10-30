class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        m, n = len(name), len(typed)
        i, j = 0, 0
        while j < n:
            if i < m and name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j-1]:
                j += 1
            else:
                return False
        return i == m

if __name__ == '__main__':
    print(Solution().isLongPressedName('aa','aaa'))
    print(Solution().isLongPressedName('alex', 'aaleex'))
    print(Solution().isLongPressedName('saeed', 'ssaaedd'))