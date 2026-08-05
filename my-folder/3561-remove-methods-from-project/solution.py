class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        edges = [[] for _ in range (n)]
        ind = [0] * n
        for u, v in invocations:
            edges[u].append(v)
            ind[v] += 1
        queue = collections.deque([k])
        sus = bytearray(n)
        sus[k] = 1
        while queue:
            u = queue.popleft()
            for v in edges[u]:
                ind[v] -=1
                if sus[v]==0:
                    queue.append(v)
                    sus[v] = 1
        rem = True
        for i in range(n):
            if sus[i] and ind[i]>0:
                rem = False
                break
        if not rem:
            return list(range(n))
        
        return [i for i in range(n) if sus[i] == 0]

