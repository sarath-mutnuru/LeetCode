class Solution:
    def intToRoman(self, num: int) -> str:
        
        _map = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        _exceptions = {4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}
        _map.update(_exceptions)

        nums = sorted(_map.keys())
    
        def get(number):
            for i in range(len(nums)):
                if nums[i] > number:
                    return nums[i-1]
            return nums[i]
    
        s = []
        while num:
            if num in _map:
                s.append(_map[num])
                num = 0
            else:
                n = get(num)
                s.append(_map[n])
                num -= n
        return ''.join(s)
        