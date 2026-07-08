# 217. Contains Duplicate
# 给一个整数数组 nums，如果任意一个值出现至少两次，返回 True；如果每个元素都不相同，返回 False。


def containsDuplicate(nums):

    for num in nums:
     if nums.count(num) > 1:
          return True
    return False

nums = [1, 2, 3, 1]
print(containsDuplicate(nums))  # 输出: True

nums = [1, 2, 3, 4]
print(containsDuplicate(nums))  # 输出: False


def containsDuplicate_02(nums):
   seen = set()
   for num in nums:
      if num in seen:
        return True
      else:
        seen.add(num)
   return False

nums = [1, 2, 3, 1]
print(containsDuplicate_02(nums))  # 输出: True

nums = [1, 2, 3, 4] 
print(containsDuplicate_02(nums))  # 输出: False
