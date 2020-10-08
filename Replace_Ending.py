#The replace ending function replaces the old string in a sentence with the new string but only if the sentence ends with the old string! If there 
#is more than one occurance of the old string in the sentence, only the one at the end is replaces, NOT all of them. For example, replace_ending("abcabc","abc","xyz")
#should return abcxyz NOT xyzxyz or xyzabc. The string comparison is case sensitive so replace_ending("abcabc","ABC","xyz") should return abcabc (no changes).

def replace_ending(sentence, old, new):
    if sentence.endswith(old): #check old string at end of sentence
        i = len(sentence) - len(old) #using i as the slicing index combine part of the sentence matched up to the matched string at the end with the new string
        new_sentence = sentence[:i] + new
        return new_sentence
    else:
        return sentence #return original sentence if no match


print(replace_ending("It's raining cats and cats", "cats", "dogs"))
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
print(replace_ending("The weather is nice in May", "may", "april")) # no change, case sensitive
print(replace_ending("The weather is nice in May", "May", "April")) #changes to april due to matching cases