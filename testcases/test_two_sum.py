def twosum(nums,target):
    for i in range(len(nums)):
        for j in range((i+1),len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]
    return []


def test_twosum_normal():
    result = twosum([2,7,11,15],9)
    assert result == [0,1]

def test_twosum_second():
    result = twosum([3,2,4],6)
    assert result == [1,2]

def test_twosum_no_solution():
    result = twosum([2,7,11,15],3)
    assert result == []