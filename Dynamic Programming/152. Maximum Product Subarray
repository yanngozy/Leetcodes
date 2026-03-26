def maxProduct(nums):
    max_product=nums[0]
    m=nums[0] # current max product
    M=nums[0] # current min product
    for i in range(1,len(nums)):
        if nums[i]>0:
            M,m=max(nums[i],M*nums[i]),min(nums[i],m*nums[i])
        else:
            M,m=max(nums[i],m*nums[i]),min(nums[i],M*nums[i])
        max_product=max(M,max_product)
    
    return max_product 

# time complexity O(n), space complexity O(1)
