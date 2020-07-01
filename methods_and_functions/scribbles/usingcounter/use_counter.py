"""module docstring"""
from collections import Counter

SAMPLE_STRING = 'Hello Mr. Rogers, how are you this fine Tuesday?'
global the_result


def count_upper(sentence):
    """Function docstring"""
    global the_result
    split_string = sentence.split(" ")
    count = 0
    for item in split_string:
        if item[0].isupper():
            the_count = Counter(item[0])
            print(the_count.keys())
            count += 1
            the_result = "No. of lower case characters: {result}".format(result=count)
    return the_result


def count_lower(sentence):
    """Function docstring"""
    global the_result
    count = 0
    for item in sentence:
        if item.islower():
            the_count = Counter(item)
            print(the_count.keys())
            count += 1
            the_result = "No. of lower case characters: {result}".format(result=count)
    return the_result


print(count_upper(SAMPLE_STRING))
print(count_lower(SAMPLE_STRING))
