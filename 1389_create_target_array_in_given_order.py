class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans  = []
        for i,_ in enumerate(nums):
            if index[i] < len(ans):
                ans.insert(index[i], nums[i])
            else:
                ans.append(nums[i])
        return ans