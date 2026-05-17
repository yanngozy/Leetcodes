class Solution(object):
    def maximumJumps(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        jumps = [0]*n
        for i in range(n-2,-1,-1):
            count = -1
            for j in range(i+1,n):
                if abs(nums[j]-nums[i])<=target and jumps[j]>=0:
                    count = max(count,1+jumps[j])
            jumps[i] = count
        return jumps[0]  

# space complexity O(n), Time complexity O(n^2)
