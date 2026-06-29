
def maximumLength(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    from collections import Counter
    import copy
    freq = Counter(nums)
    freq = sorted(zip(freq.keys(),freq.values()),key = lambda x:x[0])
    res = 1
    if freq[0][0]==1 and freq[0][1]>2:
        res = freq[0][1] if freq[0][1]%2 else freq[0][1]-1
    dico = {}
    for x,count in freq:
        if x==1:
            continue   
        y = math.sqrt(x)
        if int(y)==y and y in dico:
            if count>1:
                dico[x] = dico[y] + 2
            res = max(res,dico[y]+1)
        elif count>1:
            dico[x] = 2 
    
    return res
        
    
