class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)
        n = len(nums)
        while len(nums)>n-k:
            val = heapq.heappop_max(nums)
        return val
        