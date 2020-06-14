"""
This is my module docstring
"""


def reversed_sen_is(sentence):
    """This is my function docstring"""
    my_sen_list = [x for x in sentence.split(" ")]
    get_stuff2 = "-".join(my_sen_list[::-1])

    return get_stuff2


print(reversed_sen_is('we are ready'))
