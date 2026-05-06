class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        def validpuzzle(arr,i,j):
            for x,y in arr: 
                if y==j:
                    return False
                elif y-j==x-i:
                    return False
                elif y-j==i-x:
                    return False

            return True
        
        def complete(arr,i,alls):
            if i==n :
                new = ["."*n for _ in range(n)]
                for x,y in arr:
                    new[x] = new[x][:y]+"Q"+new[x][y+1:]
                alls.append(new)               
            
            else :
                for j in range(n):
                    if validpuzzle(arr,i,j):
                        complete(arr+[(i,j)],i+1,alls)
        
        alls = []
        complete([],0,alls)
        return alls
      
# Time complexity O(n^n) and space complexity O(n!)
