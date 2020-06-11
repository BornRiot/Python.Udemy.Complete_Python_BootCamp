"""My docstring"""


def old_macdonald1(word):
    new_word = ""
    third_letter = word[3]
    first_letter = word[0]
    new_word = first_letter.capitalize() + word[1:3] + third_letter.capitalize() + word[4:]
    return new_word




def old_mcdonald(word):
    new_string = ""
    for i, v in enumerate(word):
        if i == 0:
            first_letter = word[i].capitalize()
            new_string = new_string + first_letter + word[1:4]
        elif i == 4:
            fourth_letter = word[i].capitalize()
            new_string = new_string + fourth_letter

    return new_string


print(old_mcdonald("macdonald"))
print(old_macdonald1('macdonald'))
