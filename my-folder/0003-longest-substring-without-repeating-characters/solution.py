class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        visited = []
        subs = []
        n = len(s)
        vis = ''
        for i in range(0,n):
            if s[i] in visited:
                subs.append(vis)
                idx = vis.index(s[i])
                vis = vis[idx+1:] + s[i]
                visited = list(vis)
            else:
                vis = vis + s[i]
                visited.append(s[i])
                subs.append(vis)
        return len(max(subs, key = len))
                
