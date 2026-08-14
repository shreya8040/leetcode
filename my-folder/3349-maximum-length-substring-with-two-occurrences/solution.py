class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = {}
        left = 0
        l= 0
        for i,ele in enumerate(s):
            count[ele] = count.get(ele,0)+1
            while count[ele]>2:
                count[s[left]] -= 1
                left+=1
            l = max(l,i-left+1)
        return l

            
        
