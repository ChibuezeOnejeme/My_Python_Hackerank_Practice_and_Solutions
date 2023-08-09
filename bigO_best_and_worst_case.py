def matcher(lst,match):
   """
    Given a list return boolean if the item is in the list
   """
   for item in lst :
        if item == match:
            return True
        
   return False
        

x = [2,3,6,7,8,9,12,13]

#print(matcher(x,2)) this is the best case scenario, it the first element in the list is O(1)-constant
# print(matcher(x,30))this is the worst case ,the for loop will search the entire n element and is brute force- O(n)