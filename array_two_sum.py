"""
 Array pair sum, given an array,output all the unique pairs that sum up to specific value k.
 so the  input:
 [1,3,2,2] k =4
(1,3)
(2,2)
"""

def pair_two(array,k):
    if len(array)< 2:
      return   print("too small")
    
    seen = set()
    output =set()
    for num in array:
       target = k-num
       if target not in seen:
          seen.add(num)

       else:
          output.add((min(num,target),max(num,target)))

    print('\n'.join(map(str,list(output))))

pair_two([1,3,8,4,5,2,2],4)
"""
#blind 75
example 2 using a hash map(dictionary) ie for Pair Sum or Two Sum
That returns indexes of the two sum value for the target
"""
def two_sum(nums:list,target:int) ->list[int]:

   prevMap ={} # val:index

   for i,n in enumerate(nums):
      diff =target-n
      if diff in prevMap:
         return [prevMap[diff],i]
      prevMap[n]=i
   return

print(two_sum([1,3,8,4,5,2,2],4))