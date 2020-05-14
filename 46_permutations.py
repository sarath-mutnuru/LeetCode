class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return
        if len(nums) == 1:
            return [nums]
        perms = self.permute(nums[1:])
        res = []
        for p in perms:
            for i in range(0, len(p) + 1):
                v = [x for x in p]
                v.insert(i, nums[0])
                res.append(v)
        return res