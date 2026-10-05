"""
Arrays & Two-Pointer Technique
DSA practice with Claude
"""


def is_palindrome(s):
    """Check if a string is a palindrome, ignoring case.
    Time: O(n), Space: O(n) (due to s.lower() creating a new string)
    """
    s = s.lower()
    first, last = 0, len(s) - 1
    while first < last:
        if s[first] != s[last]:
            return False
        first += 1
        last -= 1
    return True


def reverse_array(nums):
    """Reverse nums in place, no extra array.
    Time: O(n), Space: O(1)
    """
    left = 0
    right = len(nums) - 1

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return nums


def lowest_of_two(num1, num2):
    if num1 > num2:
        return num2
    else:
        return num1


def max_area(heights):
    """Container With Most Water.
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(heights) - 1
    max_area_seen = 0
    while left < right:
        area = lowest_of_two(heights[left], heights[right]) * (right - left)
        max_area_seen = max(max_area_seen, area)
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return max_area_seen


def move_zeroes(nums):
    """Move all zeroes to the end, keeping order of non-zeroes. In place.
    Slow/fast pointers: slow = next slot for a non-zero, fast = scanner.
    Time: O(n), Space: O(1)
    """
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            slow += 1
    for i in range(slow, len(nums)):
        nums[i] = 0
    return nums


if __name__ == "__main__":
    print(is_palindrome("Racecar"))  # True
    print(reverse_array([1, 2, 3, 4, 5]))  # [5, 4, 3, 2, 1]
    print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
    print(move_zeroes([0, 1, 0, 3, 12]))  # [1, 3, 12, 0, 0]
