my_firstL = [2,8,9,7]
my_secL = [3,8,9,7]
print(my_secL[2])
print(my_firstL[3])
print(my_firstL[3] == my_secL[2])
for i in my_secL:
    print(i)
i = list(input("Please enter a guess:  "))
for i  in range(len(my_secL)):
    legacy = my_secL[i]
    duplicate = my_firstL[i]
    if my_firstL[0] == my_secL[0]:
        print("This matched") # Code is not checking each item in i and seeing if it matches to
        break                    # items in other list

new_list = [5,5,7,5]
next_list = [4,89,8]
for g,val in enumerate(new_list,1):
    print(g, val)


h = enumerate(next_list)
print(g)


# Below this lone will be used for scratch stuff and possible solutions
# if i == my_secL[1] or i == my_secL[0] or i == my_secL[2] or i == my_secL[3]:
#     print("you got a mach")
# elif i != my_secL[items]:
#     print("No match")
#     int(input('Please try and enter another number   '))
# Gist of python function to check common elements in two list: https://bit.ly/3gxM6Sq

# Website to gist on  how to compare two list: https://bit.ly/2XM6xm3
# ------ Solutions that did not work:
#    print(my_secL[items]),     print(items[my_secL]), results in index out of range
# for items in my_secL[0]:
# new_list = [0,5,7,9,8]
# next_list = [4,89,8,7,5,4]
# for z,y in range(len(next_list)): results in cannot unpack non-iterable int object
#     testNew = new_list[z]
#     test_Next = next_list[y]
#     print(y,z)