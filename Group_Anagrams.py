class Solution(object):
    def groupAnagrams(self, strs):
        # print(strs)
        sl=[]
        al=[]
        for i in strs:
            ni=tuple(sorted(i))
            sl.append(ni)
        d={}
        for i in range(len(sl)):
            if sl[i] in d:
                d[sl[i]].append(i)
            else:
                d[sl[i]]=[i]
        for i in d.values():
            tl=[]
            for j in i:
                tl.append(strs[j])
            al.append(tl)
        return al
