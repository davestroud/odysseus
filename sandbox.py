nums = [1, 2, 4, 6, 8, 9, 14, 15]
target = 13

def check_if_palidrome(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        curr = nums[left] + nums[right]
        if curr == target:
            return True
        if curr > target:
            right -= 1
        else:
            left += 1

    return False
