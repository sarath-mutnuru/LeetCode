class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        num_zeros = sum([1 for a in arr if a==0])
        print(num_zeros)
        for i in range(len(arr)-1, -1, -1):
            if i+num_zeros < len(arr):
                arr[i+num_zeros] = arr[i]
            if arr[i] == 0:
                num_zeros -=1
                if i+num_zeros < len(arr):
                    arr[i+num_zeros] = 0
                
                

                
                