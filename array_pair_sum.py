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