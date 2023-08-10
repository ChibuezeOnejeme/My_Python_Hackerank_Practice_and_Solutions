"""
Array Sequences 
1.LIST []
2.TUPLE(,)
3. STRING ("")
 ** All supporting indexing

 * Memory is  stored in bits
 * 8 bits =byte
 * stored and retrieved at O(1)

"""

import sys

n=10
data =[]
for i in range(n):
    a= len(data)
    b= sys.getsizeof(data)
    print('length: {0:3d}; size in bytes : {1:4d}'.format(a,b))

    data.append(n)