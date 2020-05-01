class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = 0
        for idx in range(len(nums)):
            if nums[idx] == 1:
                break
        nums[-1], nums[idx] = nums[idx], nums[-1]
        st = 0
        en = len(nums) - 2
        pvt = 1
        while st < en:
            if nums[st] <= pvt:
                st +=1
            else:
                nums[st], nums[en] = nums[en], nums[st]
                en -= 1
        if nums[st] <= pvt and st + 1 < len(nums):
            nums[st+1], nums[-1] = nums[-1],  nums[st+1]
            pvt_end = st +1
        else:
            nums[st], nums[-1] = nums[-1], nums[st]
            pvt_end = st
        #pvt_end = st + 1 if nums[st] <= pvt else st
        #nums[pvt_end], nums[-1] = nums[-1], nums[pvt_end]
        st = 0
        en = pvt_end - 1
        while st < en:
            if nums[st] < pvt:
                st +=1
            else:
                nums[en], nums[st] = nums[st], nums[en]
                en -= 1
        
                