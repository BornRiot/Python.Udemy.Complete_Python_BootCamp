# is_all_equal = the_cards[the_cards_i] == the_cards[the_cards_i+1]\
#  == the_cards[the_cards_i+2]
# if is_all_equal:
"""
This module is used to create two for loops and iterate  through each element
in the loop
"""
def it_elements(*args):
    """
    This function is used to create the necessary elements to
    carry out the process of iterating
    """

    my_list = list(args)
    for my_list_i, my_list_v  in enumerate(my_list):
        print(my_list[my_list_i])
        print(my_list[my_list_i+1])
        print(my_list[my_list_i+2])
        print(my_list_v)
        print(my_list_v+3)


        print(my_list)
        break

        # for x in range(len(my_list)):
            # print(my_list[my_list_i])
            # print(my_list_v)
            #print(my_list[x])
            #break



            #To get the value of in each index: the_cards[the_cards_i:]
            # is_all_equal = is_all_equal = the_cards[the_cards_i] == \
            # the_cards[the_cards_i+1] == the_cards[the_cards_i+2]



print(it_elements(5, 1, 11))
