def solve(nums,n):
    # for unsorted array
    for i in range(0,len(nums)):
        if nums[i]==n:
            return i
    return False  
    
    #for sorted array
    #worst case comparisons
    
    
    for i in range(0,len(nums)):
        if nums[i]>=n:
            break
    if nums[i]==n:
        return i
    else:
        return False        

nums=list(map(int,input().split()))
n=int(input())
print(solve(nums,n))
