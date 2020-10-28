class Solution:
    def arrayPairSum(self, nums) -> int:
        sum = 0
        nums.sort()
        for i,item in enumerate(nums):
            if i%2 == 0: # 取下标为偶数的值
                sum += item # 求和
        return sum

        '''
        精简写法：
        return sum(sorted(nums)[::2]) # 对数组排序，隔2取一个数并求和
        '''


if __name__ == '__main__':
    print(Solution().arrayPairSum([1,4,3,2]))
