#Given a list of filenames, we want to rename all the files with extension hpp to extension h. To do this, we would like to generate a new list called newfilenames,
#consisting of the new fileneames. Fill in he blanks in the code using any methods you've learnt so far, like a for loop or list comprehension.

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

newfilenames = []
for file in filenames:
    if file.endswith("hpp"):
        newfilenames.append(file.replace(".hpp", ".h")) #correlates to above empty list
    else:
        newfilenames.append(file) # needs cuz otherwise stays the same

print(newfilenames)




