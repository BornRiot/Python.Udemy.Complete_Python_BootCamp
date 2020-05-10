#!/usr/bin/env python
# coding: utf-8

# # Statements Assessment Test
# Let's test your knowledge!

# _____
# **Use <code>for</code>, .split(), and <code>if</code> to create a Statement that will print out words that start with 's':**

# In[86]:


st = 'Print only the words that start with s in this sentence'


# In[87]:


for item in st.split():
    if item[0] == 's':
      print(item)


# ______
# **Use range() to print all the even numbers from 0 to 10.**

# In[88]:


#Code Here
for num in range(0,11):
    if num % 2 == 0:
        print(num)


# ___
# **Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.**

# In[89]:


#Code in this cell
mylist = [x for x in range(1, 51) if x % 3 == 0]
print(mylist)


# _____
# **Go through the string below and if the length of a word is even print "even!"**

# In[90]:


st = 'Print every word in this sentence that has an even number of letters'


# In[91]:


#Code in this cell
confirmation = "is even "
for word in st.split():
    if len(word) % 2 == 0:
        print("The word:", word, confirmation)


# ____
# **Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".**

# In[92]:


my_list = list(range(1,101))
for jelly in my_list:
    if jelly % 3 == 0 and jelly % 5 == 0: 
        print('FizzBuzz')
    elif jelly % 5 == 0:
        print("Buzz")
    elif jelly % 3 == 0:
        print("Fizz")
    else:
        print(jelly)
    


# ____
# **Use List Comprehension to create a list of the first letters of every word in the string below:**

# In[108]:


st = 'Create a list of the first letters of every word in this string'


# In[112]:


#Code in this cell
sec_lis = [y for y in st.split(" ")]
print(sec_lis)
for item in sec_lis:
    print(item[0])


# ### Great Job!

# In[113]:


#Shorter correct code
st = 'Create a list of the first letters of every word in this string'
[letter[0] for letter in st.split()]


# In[ ]:




