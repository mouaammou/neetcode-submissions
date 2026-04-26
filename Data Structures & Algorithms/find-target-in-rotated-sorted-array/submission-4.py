class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        while l < r:
            if nums[l] < nums[r]:
                break

            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        
        pivot = l

        def binary_search(left, right):
            
            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    return mid
                elif target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        
        l = 0
        r = len(nums) - 1
        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
        else:
            r = pivot - 1

            
        return binary_search(l, r)