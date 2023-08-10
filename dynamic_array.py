# def anagram(s1,s2):
#     """
#     Anagrams are strings with thesame length and words
#     """
#     s1 =s1.replace(' ','').lower() 
#     s2 =s2.replace(' ','').lower()
#     return sorted(s1) == sorted(s2)

# print(anagram("TOP",'pot'))

def anagram2(s1,s2):

    s1 =s1.replace(' ','').lower() 
    s2 =s2.replace(' ','').lower()

    # checking if it has the same number of letters

    if len(s1) != len(s2):
        return False
    # count frequency of each letter
    count ={}
    
    for letter in s1 : # for every letter in first string
        if letter in count: # if letter already in my dictionary,then
            count[letter] +=1

        else:
            count[letter]=1
   # reverse for second string

    for letter in s2:
        if letter in count:
            count[letter] -=1

        else:
            count[letter]=1

    for k in count:
        if count[k] !=0:
            return False
    return True


print(anagram2('MONEY','ONEYM'))