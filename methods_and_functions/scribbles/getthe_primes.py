"""
This module is use to solve the get_primes program challenge.
It wuill be done on a trial basis with frequen updated code
"""

the_arg = "Forever young"
count = 0
while count < len(the_arg):
    print(the_arg[count])
    count += 1

first_list = [0, 58, 58, 98, 48, 69, 14]
count2 = 0
sec_list = []
print("This is sec_list before assignment:", sec_list)
while count2 < len(first_list):
    for x in first_list:
        sec_list.append(x)
        count2 += 1

print(sec_list)

def copy_list(orglist):
    the_count = 0
    the_new_list = []
    while the_count < len(orglist):
        for x in orglist:
            the_new_list.append(x)
            the_count += 1
        return the_new_list

sample_list = [25,36,78,96,458,4,14]
#print(copy_list(sample_list))
last_list = copy_list(sample_list)
print(last_list)
print(type(last_list))
for c in last_list:
    print(c)
