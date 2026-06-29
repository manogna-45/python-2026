def Two_Sum(nums,target):
    nums.sort()
    left = 0
    right = len(nums)-1
    while left < right:
        curr_sum = nums[left]+nums[right]
        if curr_sum == target:
            return nums[left],nums[right]
        elif curr_sum < target:
            left+=1
        else:
            right-=1
    return []
