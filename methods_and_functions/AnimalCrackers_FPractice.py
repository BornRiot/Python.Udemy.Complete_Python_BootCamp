"""This is my module docstring for this exercise """


def animal_crackers(text):
    """This is my function docstring for the exercise """
    the_string = str(text)
    my_list = [x for x in the_string.split(" ")]
    first_word = my_list[0]
    sec_word = my_list[1]
    if first_word[0] == sec_word[0]:
        return True
    else:
        return False


print(animal_crackers("Levelheaded Llama"))
