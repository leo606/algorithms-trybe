from challenges.sorting.merge_sort import merge_sort


def is_anagram(first_string, second_string):
    first_string, second_string = first_string.lower(), second_string.lower()

    if first_string != second_string:
        return merge_sort(first_string) == merge_sort(second_string)
    else:
        return True
