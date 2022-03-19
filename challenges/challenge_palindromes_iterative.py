def is_palindrome_iterative(word):
    if word:
        return word == word[::-1]
    else:
        return False
