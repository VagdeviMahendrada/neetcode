class Solution(object):
    def maxSubarraySumCircular(self, nums):
        n=len(nums)
        tot_sum=sum(nums)
        max_sum=nums[0]
        min_sum=nums[0]
        curr_max=nums[0]
        curr_min=nums[0]
        for i in range(1,n):
            curr_max=max(nums[i],curr_max+nums[i])
            curr_min=min(nums[i],curr_min+nums[i])
            max_sum=max(max_sum,curr_max)
            min_sum=min(min_sum,curr_min)
        if min_sum == tot_sum:
            return max_sum
        return max(max_sum,tot_sum-min_sum)
