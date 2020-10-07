#The highlight word function changes the given word in a sentence to its upper case version. Can you write this function in just one line?
def highlight_word(sentence, word):
    return(sentence.replace(word,word.upper()))
print(highlight_word("Have a nice day", "nice"))