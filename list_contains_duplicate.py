"""
# Blind 75
Leet 217
Given an integer array nums,return True if any of the nums appear atleast twice in the arrary, return false if every element is distinct

eg.
input_nums [1,2,3,1]
return True

input_nums =[1,2,3,4,5]
return False


input_nums =[1,1,1,3,3,5,7,8]
return True
"""

def containsDuplicate(nums:list[int])->bool:
    hash_set =set()
    for n in nums:
        if n in hash_set:
            return True
        hash_set.add(n)

    return False

print(containsDuplicate([1,2,3,1]))