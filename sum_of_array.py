def sum_simple_array(array):
    """
    take an array/List ,sum all the element of the array
    eg a =[1,2,3,4,5] = 1+2+3+4+5 =15
    """

    return sum(array)


array_input =list(map(int,input().rstrip().split()))# This take input in the commandline separated by space
print(array_input)
func = sum_simple_array(array_input)
print(func)

