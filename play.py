

nums = [0,10,20,30,40,50]

# make every first value the key and second the value

key= []

value =[]


for i in range(len(nums)):
      if i%2 ==0:
        key.append(nums[i])
        
      else:
         value.append(nums[i])

f_dic=  dict(zip(key,value))

print(f_dic)


      