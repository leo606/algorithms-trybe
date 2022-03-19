def search(array, value):
    for index, element in enumerate(array):
        if element == value:
            return index
    return False


def find_duplicate(nums):
    if not nums:
        return False

    for index, number in enumerate(nums):
        if type(number) != int or number < 1:
            return False

        duplicated_in_array = search(nums, number)
        if duplicated_in_array != index:
            return nums[duplicated_in_array]
    return False
