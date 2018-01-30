# Given an array of integers, return the indices of the two numbers such that they add to up to a specific target.
# You may assume that each input would have exactly one solution and you may not use the same element twice
# Example:
# Given nums = [2, 7, 11, 15], target = 9
# return [0, 1] (nums[0] + nums[1] = 2 + 7 = 9)

def two_sum(nums, target):
    seen = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in seen:
            return [seen[diff], i]
        else:
            seen[nums[i]] = i
    return []

if __name__ == "__main__":
    n = [2, 7, 11, 15]
    t = 9
    print(two_sum(n, t))