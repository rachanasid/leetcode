# brute force, O(2^n)
def count(nums, target, index):
    if index == len(nums):
        return 1 if target == 0 else 0

    return count(nums, target-nums[index], index+1) + count(nums, target+nums[index], index+1)


def findTargetSumBruteForce(nums, S):
    if not nums:
        return 0
    return count(nums, S, 0)


#  O(n*S)
def findTargetSum(nums, S):
    total_sum = sum(nums)
    if total_sum < S or (total_sum + S) % 2 == 1:
        return 0

    target = (total_sum - S) / 2
    dp = [0] * (target + 1)
    dp[0] = 1

    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] += dp[i - num]
    return dp[target]
