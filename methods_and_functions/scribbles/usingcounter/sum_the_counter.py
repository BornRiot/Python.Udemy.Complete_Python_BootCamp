"""docstring"""
from collections import Counter

SAMPLE_STRING = 'Hello Mr. Rogers, how are you this fine Tuesday?'


def up_low(sentence):
    """Function docstring"""
    # Working with upper case characters
    split_sen = sentence.split(" ")
    upper_letters_list = [x for x in split_sen if x[0].isupper()]
    upper_letters_count = Counter(upper_letters_list)
    upper_letters_lenght = len(upper_letters_count)

    # Working with lower case characters
    lower_letters_list = [x for x in sentence if x.islower()]
    the_count = Counter(range(len(lower_letters_list)))
    lower_letters_count = sum(the_count.values())

    return upper_letters_lenght, lower_letters_count


upper_case, lower_case = up_low(SAMPLE_STRING)
print("Original String: {string}".format(string=SAMPLE_STRING))
print("No. of Upper case characters: {num}".format(num=upper_case))
print("No. of Lower case characters: {num}".format(num=lower_case))

# structure to follow for code
the_split = SAMPLE_STRING.split(" ")
the_upside = [x for x in the_split if x[0].isupper()]
the_upcount = Counter(the_upside)

# More experimenting
my_list = ["v", "c", "c", "s"]
count = Counter(my_list)
