class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for i in strs:
            s = ''.join(sorted(i))
            if(s in dic):
                dic[s].append(i)
            else:
                dic[s] = [i]
        k = []
        for values in dic.values():
            k.append(values)
        return k