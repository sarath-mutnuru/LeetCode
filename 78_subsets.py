class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def s_util(arr):
            if not arr:
                return [[]]
            ans = s_util(arr[1:])
            t = len(ans)
            for i in ans[:t]:
                ans.append([arr[0]]+i)
            return ans
        return s_util(nums)

            