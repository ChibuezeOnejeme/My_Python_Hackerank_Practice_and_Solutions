
# find the maximum sum of array
# Largest continous sum of array
# very important


def largest_sum(array):
    if len(array) ==0:
        print('Too small')

    max_sum =current_sum =array[0]
    for num in array[1:]:
        current_sum=max(current_sum+num,num)
        max_sum= max(current_sum,max_sum)

    return max_sum

print(largest_sum([2,2,4,5,6,3]))