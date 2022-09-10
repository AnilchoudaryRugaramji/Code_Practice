#!/usr/bin/env python
# coding: utf-8

# ## 1. Code to check for Palindrome

# In[3]:


str = input('Enter the input') # taking the input as string type
rev_str = '' # considering empty string
for i in str:  # iterator to compute the reverse of the string
    rev_str = i + rev_str 
    
if str == rev_str:     # condition to check both the string are same
    print(f'{str} is a Palindrome')
else:
    print(f'{str} is not a Palidrome')


# ##   2. Code for the below Scenario 
#         Sum of 2 digits into output
# 		n1 = 1234 # int(input("Enter number1 :" ))
# 		n2 = 9999 # int(input("Enter number2 :" ))
# 		Output: 9+1 2+9 3+9 4+9 
# 		         10 + 11 + 12 + 13
# 				 46

# In[1]:


import functools    # module to import reduce fucntion 

n1 = int(input("Enter number1 :" ))   # taking the first input
n2 = int(input("Enter number2 :" ))   # tsking the second input

res1 = [int(x) for x in str(n1)]      # list comprehension to compute list of integers for n1
res2 = [int(y) for y in str(n2)]      # list comprehension to compute list of integers for n2

result = res1 + res2                  # adding both the list to create one list

final_result = functools.reduce((lambda a,b : a+b),result) # reduce function to compute 
final_result  


# # 3. Code for the below scenario
# 
#            st = "ab@#cd!ef"
#            Reverse string considering only alphabets. Symobls should not be reversed
#            Output: fe@#dc!ba

# In[8]:


def reverseString(text):
    index = -1
 
    # Loop from last index until half of the index    
    for i in range(len(text)-1, int(len(text)/2), -1):
 
        # match character is alphabet or not        
        if text[i].isalpha():
            temp = text[i]
            while True:
                index += 1
                if text[index].isalpha():
                    text[i] = text[index]
                    text[index] = temp
                    break
    return text
            


# In[27]:


st = "ab@#cd!ef"

# defining a udf
def rev_letters(string):
    
    # Separating the letters from the symbols into a  new list
    letters = [char for char in string if char.isalpha()]
    
    # empty list
    ans = []
    
    # iterating thru every element in the original string
    for char in string:
        # if the element is alphabet append the last element of the letters list ==> reversing the order of alphabets
        if char.isalpha():
            ans.append(letters.pop())
        
        # else append the symbols in their original place
        else:
            ans.append(char)
    # return the list as a string after joining the elements
    return ''.join(ans)

# calling the udf
rev_letters(st)


# In[ ]:





# ## 4. Findout elements duplicate count output in  dict format

# In[11]:


string = input('Enter the string: ') # take user input in string format

all_freq = {}  # define a empty dict
   
for i in string:      # iterator 
    if i in all_freq:   # checking if the element is present as a key 
        all_freq[i] += 1   # if present increase count by 1
    else:
        all_freq[i] = 1    # if not present add a new key value pair
print(all_freq)           # display output


# # 5. Code for the below scenario
#     t1 = (1, 2, 3, "a", "c") 
#     t2 = ("b", "d", 9, 8, 7)
#     Output: (10,10,10,"ab","cd")

# In[13]:


t1 = (1, 2, 3, "a", "c") 
t2 = ("b", "d", 9, 8, 7)

# reindexing the elements to match the datatypes
t3 = t2[2:]
t4 = t2[:2]
t5 = t3+t4

# using map function to add the respective datatypes
my_result = tuple(map(lambda i, j: i + j, t1, t5))

#displaying the result
my_result


# ## 6. Write a Python program to remove leading zeros from an IP address.
#         inp = "216.08.094.196"
#         o/p =  216.8.94.196

# In[15]:


# by using repalce function
inp = "216.08.094.196"
res = inp.replace('0','')
res


# In[14]:


# without replace
inp = "216.08.094.196"

# create a list with individual elements
list1 = list(inp)

# filtering the new list for non zero elements
a = list(filter(lambda num: num != '0', list1))

# joining the filtered elements and converted to string
listToStr = ''.join(map(str, a))

# displaying the result
print(listToStr)


# ## 7. Solve
# 
#         l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
#         output= [1,2,3,4,5,6,7,8,9,10]

# In[16]:


l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]


# In[17]:


# using a recursive udf
# appending each element to the resultant list after checking for a nested list
def flatten(l): return flatten(l[0]) + (flatten(l[1:]) if len(l) > 1 else []) if type(l) is list else [l]


# In[18]:


# applying the udf
flatten(l)


# ## 8. Solve
# 
#     Load sample content in text file.
#     Read data and find
#     
#     1. No of lines in file
# 	2. No of words in each line 
# 	3. No of chars in each line
# 	4. No of vowels and consonants
# 	5. No of special chars linewise and total 

# ## Solution: File handling topics are not yet covered 

# In[ ]:





# In[ ]:




