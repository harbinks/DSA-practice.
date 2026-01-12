class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """        
        seen = set()
        left, window_sum, result = 0, 0, 0
        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                window_sum -= nums[left]
                left+=1
            seen.add(nums[right])
            window_sum+=nums[right]
            if right - left + 1 == k:
                result = max(result, window_sum)
                seen.remove(nums[left])
                window_sum -= nums[left]
                left+=1 
        return result