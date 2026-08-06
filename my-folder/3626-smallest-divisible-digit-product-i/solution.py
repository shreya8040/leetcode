class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        for i in range (n,101):
            d = 1
            k = i
            if i<9 and i%t == 0:
                return i
            while k>0:
                dig = k % 10
                d = d*dig
                k = k //10
            if d == 0:
                return i
            if d%t == 0:
                return i
                break



