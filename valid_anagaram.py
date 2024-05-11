class Solution(object):
    def isAnagram(self, s, t):
        d1={}
        d2={}
        l1=[]
        l2=[]
        l3=[]
        l4=[]
        for i in s:
            if i in d1:
                d1[i]+=1
            else:
                d1[i]=1
        for i in t:
            if i in d2:
                d2[i]+=1
            else:
                d2[i]=1
        for i in d1.keys():
            l1.append(i)
        for i in d2.keys():
            l2.append(i)
        l1.sort()
        l2.sort()
        for i in l1:
            l3.append([i,d1[i]])
        for i in l2:
            l4.append([i,d2[i]])
        if l3==l4:
            return True
        else:
            return False   
        
