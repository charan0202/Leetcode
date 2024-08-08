def twosum(nums , target):
    
    complementMap = dict()
    
    for i in range (len(nums)):
        complement = target - nums[i]
        if complement in complementMap:
            return complementMap[complement],i
            
        else:
            complementMap[complement] = i

result = twosum([2,5,11,15],9)
print(result)