def sum_of_two_integers(a:int,b:int):
    """
    This function takes two integers *a,b* as an arguement and add them together

    """

    return a+b

input_a = int(input("input_ number:  "))
input_b =int(input("input_ number:  "))

func = sum_of_two_integers(input_a,input_b)

print("Output :",func)
