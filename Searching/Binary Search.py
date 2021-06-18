def solve(nums,n):
    start=0
    end=len(nums)-1

    while start <= end:
        mid=start+end-start//2
        if n==nums[mid]:
            return mid
        elif n<nums[mid]:
            end=mid-1
        elif n>nums[mid]:
            start=mid+1
    return False    


nums=list(map(int,input().split()))
n=int(input())
print(solve(nums,n))
