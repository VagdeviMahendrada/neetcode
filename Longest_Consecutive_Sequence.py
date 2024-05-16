from collections import OrderedDict
class Solution(object):
    def longestConsecutive(self, nums):
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        sd=OrderedDict(sorted(d.items()))
        print(sd)
        c=0
        maxc=0
        keys=sd.keys()
        vals=sd.values()
        n=len(keys)
        for i in range(n-1):
            if keys[i+1]-keys[i]==1:
                # if vals[i]
                c+=1
            else:
                if c>maxc:
                    maxc=c
                c=0
            if i==n-2:
                if c>maxc:
                    maxc=c
        if len(nums)==0:
            return 0
        elif len(nums)==2 and keys[n-1]-keys[n-2]==1:
            return maxc+1
        elif (keys[n-1]-keys[n-2]==1 and len(nums)==2) or n==0:
            return maxc
        return maxc+1
#0 0 1 2 3 4 5 6 7 8
            
