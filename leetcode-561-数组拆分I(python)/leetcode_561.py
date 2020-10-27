class Solution:
    def arrayPairSum(self, nums) -> int:
        return sum(sorted(nums)[::2])

if __name__ == '__main__':
    print(Solution().arrayPairSum([1,4,3,2]))
