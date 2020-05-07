class Solution:
    def twoSum(self,nums,st,en,target):
        res = []
        left = st
        right = en
        while left < right:
            if nums[left] + nums[right] == target:
                res.append([nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
        return res
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            r = self.twoSum(nums,i+1,len(nums) - 1, -1*nums[i])
            for x in r:
                x.append(nums[i])
            if r:
                res.extend(r)
        # for v in res:
        #     v.sort()
        # res = [tuple(v) for v in res]
        # res = list(set(res))
        # res =[list(v) for v in res]
        return res