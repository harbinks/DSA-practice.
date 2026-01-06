class Solution(object):
    def nextGreaterElements(self, nums1, nums2):
        stack = []
        next_greater = {}

        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)
        while stack:
            next_greater[stack.pop()] = -1

        return [next_greater[num] for num in nums1]
  

 