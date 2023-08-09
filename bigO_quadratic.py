# O(n^2)

def func_quad(lst):
    """
    Prints Pairs for every Item in the list
    """

    for item1 in lst:
        for item2 in lst:
            print(item1,item2)

func_quad([1,2,3])