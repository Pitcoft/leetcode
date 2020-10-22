class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        # 定义双指针
        p, q = len(S) - 1, len(T) - 1
        # 定义变量记录 '#' 的数量
        count_S, count_T = 0, 0
        while p >= 0 or q >= 0:
            # 遍历字符串 S
            while p >= 0:
                # 字符为 '#'，count_S 加 1，p指针左移
                if S[p] == '#':
                    count_S += 1
                    p -= 1
                # 字符为普通字符，count_S>0，删除该字符，count_S，p左移继续遍历
                elif count_S > 0:
                    count_S -= 1
                    p -= 1
                # 字符为普通字符，count_S=0，跳出循环，等待与另一个字符串判断
                else:
                    break
            # 遍历字符串 T
            while q >= 0:
                if T[q] == '#':
                    count_T += 1
                    q -= 1
                elif count_T > 0:
                    count_T -= 1
                    q -= 1
                else:
                    break
            # 判断字符串两个未遍历完，跳出循环时，两个指针对应的字符是否相等
            if p >= 0 and q >= 0:
                if S[p] != T[q]:
                    return False
            # 只有一个字符串遍历完，另一个跳出循环
            elif p >= 0 or q >= 0:
                return False
            p -= 1
            q -= 1
        return True
if __name__ == '__main__':
    S = "a##c"
    T = "#a#c"
    print(Solution().backspaceCompare(S, T))