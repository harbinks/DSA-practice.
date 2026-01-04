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

# There are two arrays, nums1 and nums2, where nums1 is a subset of nums2.
# We process nums2 using a monotonic decreasing stack.
# The stack stores elements that are waiting to find their next greater element.
# As we iterate through nums2, if the stack is empty, we push the element directly.
# If the current element is greater than the top of the stack, we pop elements until the stack is empty or the top is greater than the current element.
# Each popped element is stored in prev, and we map prev to the current element in next_greater, because the current element is the first greater element to its right.
# After processing all elements in nums2, any elements left in the stack do not have a greater element to their right, so we map them to -1.
# Finally, we return the mapped results for elements in nums1.


 