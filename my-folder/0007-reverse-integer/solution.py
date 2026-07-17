
class Solution:
    def reverse(self, x: int) -> int:
        
        if x>0:
             d = x
             flag =0
        else:
            d = -x
            flag = 1
        rev = 0
        if x>(2**31)-1 or x<(-2)**31:
            return 0
        while(d != 0):
            dig = d%10
            rev = rev*10+dig
            d=d//10
        if flag == 1:
            rev = -rev
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev
        
