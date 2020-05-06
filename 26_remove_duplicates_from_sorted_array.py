class Solution:
             
    def removeDuplicates(self, vec: List[int]) -> int:
        if not vec:
            return 0
        if len(vec) == 1:
            return 1
        v = 1
        for i in range(1,len(vec)):
            if vec[v-1] != vec[i]:
                vec[v] = vec[i]
                v += 1
        return v
    