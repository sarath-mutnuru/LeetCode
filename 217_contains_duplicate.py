class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d={}
        for n in nums:
            d[n] = d.get(n,0) + 1
            if d[n] > 1:
                return True
        return False
        