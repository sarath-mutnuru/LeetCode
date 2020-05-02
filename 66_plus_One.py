class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        j = len(digits) - 1
        while j >=0 and digits[j] == 9:
            digits[j] = 0
            j -= 1
        
        if j >= 0:
            digits[j] += 1
            return digits
        digits.append(1)
        
        digits.insert(0, 1)
#         for j in range(len(digits) - 1, 0, -1):
#             digits[j], digits[j-1] = digits[j-1], digits[j]
        return digits
        
        
            
