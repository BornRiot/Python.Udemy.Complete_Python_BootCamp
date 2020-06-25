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

def animal_crackers_c(text):
    wordlist = text.split()
    return wordlist[0][0] == wordlist[1][0]


print(animal_crackers("Levelheaded Llama"))
print("this is the correct answer:")
print(animal_crackers_c("Levelheaded Llama"))
