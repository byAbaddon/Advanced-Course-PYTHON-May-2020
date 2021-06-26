def palindrome(word, index):
    reversed_word = ''.join(list(reversed(word)))
    if word == reversed_word:
        return f'{word} is a palindrome'
    else:
        return f'{word} is not a palindrome'

