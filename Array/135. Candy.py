class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        if n==1:
            return 1
        res = 0
        indices = [ i for i in range(n) ]
        indices = sorted(indices, key = lambda x:ratings[x])
        alloc = [0]*n
        for i in indices:
            alloc[i] = 1
            if i<n-1 and ratings[i]>ratings[i+1]: alloc[i] = alloc[i+1]+1 
            if i>0 and ratings[i]>ratings[i-1]: alloc[i] = max(alloc[i-1]+1,alloc[i]) 
            res +=alloc[i]
    
        return res
        
# time complexity O(nlog(n)) , space complexity O(n)
