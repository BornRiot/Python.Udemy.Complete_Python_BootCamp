the_string = "this is just another line of text"

comprehend = [x for x in range(1,25) if x % 2 == 0]
my_dic = {'some_key': 'some_value',
          'some_num': 3,
          }




print(comprehend[0:10:3])
print(the_string[2:9:2])
#the_dict = the_list[9]
# find dictionary in list: https://bit.ly/373a4QY
the_list = [8,9,8,7,'word', 3.5, [2,5,6,9], True,(1,5,7.8,6.36), {'fish':"Grouper" } ]
new_dic = [x for x in the_list if isinstance(x,float) == True] # use isinstance to find the specific data
#type in the list
z = the_list.index({'fish':'Grouper'})
the_new_dicts = the_list[9]
print(the_new_dicts)
print(z)
print(type(z))
print(new_dic)
