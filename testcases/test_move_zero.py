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

def test_move_zero_normal():
    assert move_zero([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]

def test_move_zero_edge_cases():
    assert move_zero([0, 0, 0]) == [0, 0, 0]
    assert move_zero([1, 2, 3]) == [1, 2, 3]
    assert move_zero([]) == []
    assert move_zero([0]) == [0]
    assert move_zero([1]) == [1]