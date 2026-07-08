def move_zero(nums):
    new_nums = []
    count_zero = 0
    for num in nums:
        if num != 0:
            new_nums.append(num)
    
    count_zero = len(nums) - len(new_nums)
    for i in range(count_zero):
        new_nums.append(0)
    return new_nums

    for j in range(len(nums)):
        nums[j] = new_nums[j]
    return nums

nums = [0, 1, 0, 3, 12]
print(move_zero(nums))


"""
双指针---哨兵版本

！！！用一个指针 pos 记录“下一个非零元素应该放的位置”。
遍历数组，遇到非零元素就放到 nums[pos]，然后 pos 往后移动。
最后从 pos 到末尾全部填 0。
"""

def move_zero(nums):
    pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pos] = nums[i]
            pos += 1

    for i in range(pos, len(nums)):
        nums[i] = 0
    return nums
