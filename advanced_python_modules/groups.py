from collections import Counter
students_grade_level = [10,12,12,10,9,9,11,11,12,10,12,9,11,9,12,10,10,12]
get_count =Counter(students_grade_level)
# Test list and tuple unpacking
top_two_classes = get_count.most_common(2)
top_class = top_two_classes[0]
sec_top_class = top_two_classes[1]
print("The top two classes with the most students are {}th and {}th grade with\
 {} and {} students respectively".format(top_class[0], sec_top_class[0], \
 top_class[1], sec_top_class[1]))
g9_counter = 0
g11_counter = 0
for keys, values  in get_count.items():
    if keys == 9:
        g9_counter = values
    elif keys== 11:
        g11_counter = values
print("There are currently {} freshmen in this year's class".format(g9_counter))
print("There are currently {} juniors in this year's class".format(g11_counter))
