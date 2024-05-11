class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}
        al=[]
        for i in nums:
            if i in d:
                continue
            else:
                d[i]=target-i
        # print(d)
        for k,v in d.items():
            if target==(k*2):
                na=nums[::-1]
                # return [nums.index(k),(len(nums)-na.index(k)-1)]
                al.append([nums.index(k),(len(nums)-na.index(k)-1)])
            else:
                if v in nums:
                    # return [nums.index(k),nums.index(v)]
                    al.append([nums.index(k),nums.index(v)])
        for i in al:
            if i[0]==i[1]:
                continue
            else:
                return i
        
