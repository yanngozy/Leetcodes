def constructMaximumBinaryTree(nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        def buildtree(start,end,nums):
            if start==end:
                return None
            idx = start
            for i in range(start,end):
                if nums[i]>nums[idx]:
                    idx = i
            root = TreeNode(val=nums[idx])
            root.left = buildtree(start,idx,nums)
            root.right = buildtree(idx+1,end,nums)
            return root
        
        return buildtree(0,len(nums),nums)
            
        
