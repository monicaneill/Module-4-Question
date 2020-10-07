#Use a dictionary to count the frequency of letters in the input string. Only letters should be counted, no blank spaces, numbers or punctuation.
#Upper cases should be considered the same as lower cases.

def count_letters(text):
    result = {}
    text = text.strip()

    for letter in text.lower():
        if letter.isalpha():
            if letter not in result:
                result[letter] = 0
            result[letter] += 1
    return result

print(count_letters("Maths is fun!!! 2+2 = 4"))






