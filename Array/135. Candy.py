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
        allocations = [0]*n
        for i in indices:
            left, right = 0, 0
            if i<n-1:right = allocations[i+1]+1 if ratings[i]>ratings[i+1] else 1
            if i>0:left = allocations[i-1]+1 if ratings[i]>ratings[i-1] else 1      
            alloc = max(left,right)
            allocations[i] = alloc
            res +=alloc
    
        return res
        
# time complexity O(nlog(n)) , space complexity O(n)
