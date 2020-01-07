'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    count = 0
    if "th" not in word:
        return 0
    elif "th" in word[:2]:
        count += 1
    return count + count_th(word[1:])
