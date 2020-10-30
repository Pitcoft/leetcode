class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        name += "$"
        for type in typed:
            if type == name[i]:
                i += 1
            elif type != name[i-1]:
                return False
        return i == len(name) - 1

if __name__ == '__main__':
    print(Solution().isLongPressedName('aa','aaa'))
    print(Solution().isLongPressedName('alex', 'aaleex'))
    print(Solution().isLongPressedName('saeed', 'ssaaedd'))