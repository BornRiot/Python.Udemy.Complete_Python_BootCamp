"""
This is my module docstring
"""

def master_yoda_c(text):
    return ' '.join(text.split()[::-1])

def reversed_sen_is(sentence):
    """This is my function docstring"""
    my_sen_list = [x for x in sentence.split(" ")]
    get_stuff2 = "-".join(my_sen_list[::-1])

    return get_stuff2


print(reversed_sen_is('we are ready'))
print("This is the correct answer")
print(master_yoda_c("we are ready"))
