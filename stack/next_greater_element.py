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
# Example usage:
if __name__ == "__main__":
    sol = Solution()
    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]
    print(sol.nextGreaterElements(nums1, nums2))  # [3, -1]
