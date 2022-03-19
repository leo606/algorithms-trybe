def is_palindrome_iterative(word):
    if not word or word[0] != word[-1]:
        return False

    for index in range(1, len(word) - 2):
        if word[index] != word[-(index + 1)]:
            return False
    return True


word = "agua"

print(is_palindrome_iterative(word))
