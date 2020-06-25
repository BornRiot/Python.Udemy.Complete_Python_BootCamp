"""My docstring"""


def old_macdonald1(word):
    """This is the function docstring """
    third_letter = word[3]
    first_letter = word[0]
    new_word = first_letter.capitalize() + word[1:3] + third_letter.capitalize() + word[4:]
    return new_word


def old_macdonald_c(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'Name is too short!'


print(old_macdonald1('macdonald'))
print("This is the correct answer:")
print(old_macdonald_c('macdonald'))
