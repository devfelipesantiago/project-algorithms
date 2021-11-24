from challenges.merge_sort import merge_sort


def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if len(first_string) != len(second_string):
        return False

    first_string, second_string = merge_sort(first_string), merge_sort(
        second_string
    )

    for index in range(0, len(first_string)):
        if not first_string[index] == second_string[index]:
            return False
    return True
