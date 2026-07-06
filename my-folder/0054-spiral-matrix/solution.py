class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ar =[]
        top = 0
        bottom =len(matrix)-1
        left =0
        right= len(matrix[0])-1
        while top<=bottom and left<=right:
            for i in range(left, right+1):
                ar.append(matrix[top][i])
            top +=1

            for j in range(top, bottom+1):
                ar.append(matrix[j][right])
            right -=1

            if top<=bottom:
                for k in range(right,left -1, -1):
                    ar.append(matrix[bottom][k])
                bottom -=1

            if left<=right:
                for l in range(bottom, top-1,-1):
                    ar.append(matrix[l][left])
                left +=1
            
        return ar
        

