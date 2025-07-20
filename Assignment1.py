# James Bianca
# CSC505 Critical Thinking Assignment

# This simple shifts ascii characters by two positions if their numerical value is even
# Gather user input
word = input("Type a word: ")
# convert the string to a list
char_list = list(word)
# list to contain our modified characters
modified_chars = []
# loop over the characters in our string
for char in char_list:
    # convert chharacters into their numeric values
    ord_char = ord(char)
    # if the number is even add 2 to it
    if ord_char % 2 == 0:
        ord_char += 2
    # append characters to new list
    modified_chars.append(chr(ord_char))
# convert them to a string
new_word = "".join(modified_chars)
# display new value
print(new_word)
 