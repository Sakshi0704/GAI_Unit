nums = [2, 7, 11, 15]
target = 9

nums.sort()

def targetSum(nums, target):
    nums_to_index = []
    p1 = 0
    p2 = len(nums)-1
    while p1<p2:
        sum = nums[p1]+nums[p2]
        if sum==target:
            nums_to_index.append(p1)
            nums_to_index.append(p2)
            break
        elif sum<target:
            p1+=1
        else:
            p2-=1
    return nums_to_index


result = targetSum(nums,target)
print(result)