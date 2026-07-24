class Solution:

    def findMinimum(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return left
    def search(self, nums: List[int], target: int) -> int:

        minimum = self.findMinimum(nums)

        # Decide which half to search
        if nums[minimum] <= target <= nums[-1]:
            left = minimum
            right = len(nums) - 1
        else:
            left = 0
            right = minimum - 1

        # Normal Binary Search
        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return -1


        