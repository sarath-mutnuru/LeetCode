class Solution:
    
    def topKFrequent(self, nums, k):
        import six
        hs = {}
        frq = {}
        for i in range(0, len(nums)):
            if nums[i] not in hs:
                hs[nums[i]] = 1
            else:
                hs[nums[i]] += 1

        for z,v in six.iteritems(hs):
            if v not in frq:
                frq[v] = [z]
            else:
                frq[v].append(z)
        
        ans = []
        
        for x in range(len(nums), 0, -1):
            if x in frq:
                ans.extend(frq[x])
                if len(ans) == k:
                    return ans