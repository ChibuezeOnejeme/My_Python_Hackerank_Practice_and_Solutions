def sum1(n):
    """
    Take an input n and return the sum from 0 to n
    """
    final_sum =0
    for x in range(n+1):
        print(x)
        final_sum +=x
    return final_sum
       


print(sum1(5))
