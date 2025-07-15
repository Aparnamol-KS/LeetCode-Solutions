def print_boundary(matrix, sr, er, sc, ec,ans):
        #first row
        for j in range(sc, ec+1):
            ans.append(matrix[sr][j])
        
        #last col
        for i in range(sr+1 ,er+1):
            ans.append(matrix[i][ec])

        #last row
        if sr!=er:
            for j in range(ec-1,sc-1,-1):
                ans.append(matrix[er][j])

        if sc!=ec:
            for i in range(er-1, sr, -1):
                ans.append(matrix[i][sc])

class Solution:
   
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        sr = 0
        sc = 0
        er = n-1
        ec = m-1

        ans = []
        while(sr<=er and sc<=ec):
            print_boundary(matrix, sr, er, sc, ec,ans)
            sr = sr+1
            sc = sc+1
            er = er-1
            ec = ec-1

        return ans

    
        