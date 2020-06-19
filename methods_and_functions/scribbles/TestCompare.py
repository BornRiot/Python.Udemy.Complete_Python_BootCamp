# Website with more info  https://bit.ly/3d5WMoR
first= (1,2,3,4,5,6)
last=(7,6,5,4,3,2,1)
for i in range(len(first)):
    l1 = first[i]
    l2 = last[i]
    if l1 < l2:
        print("l1 < l2", l1)
    elif l1 > l2:
        print("l2 > l1", l2)
    elif l1 == l2:
        print("l1 == l2",l1)
