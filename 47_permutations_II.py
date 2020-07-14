class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def perms_util(arr):
            if len(arr) == 0:
                return [[]]
            
            t = perms_util(arr[1:])
            l = len(t)
            for p in t[:l]:
                for i in range(len(p)+1):
                    if i > 0 and p[i-1] == arr[0]:
                        break
                    v = [x for x in p]
                    v.insert(i, arr[0])
                    t.append(v)
            return t[l:]
        ans = perms_util(nums)
        #ans = list(set(tuple(a) for a in ans))
        return ans
            
            
        