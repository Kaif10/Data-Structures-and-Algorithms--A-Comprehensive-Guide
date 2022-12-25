def containsDuplicate(nums):
    if len(nums) == len(list(set(nums))):
        return "false"
    else:
        return "true"


