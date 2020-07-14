class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        j = 0
        ch = False
        while j < len(bits):
            if bits[j]==0:
                j += 1
                ch = True
            else:
                j += 2
                ch = False
        return ch
                