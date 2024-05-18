class Solution(object):
    def maxSubArray(self, nums):
        curr_sum=0
        max_sum=-9999999
        n=len(nums)
        if n==1:
            return nums[0]
        else:
            for i in nums:
                curr_sum=max(curr_sum,0)
                curr_sum+=i
                max_sum=max(curr_sum,max_sum)
            return max_sum
        
