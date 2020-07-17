class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        def reverse(arr,st,en):
            while st < en:
                arr[st],arr[en] = arr[en], arr[st]
                st += 1
                en -= 1
        n = len(nums)
        reverse(nums, 0, n-1)
        reverse(nums,0, k-1)
        reverse(nums, k, n-1)
                