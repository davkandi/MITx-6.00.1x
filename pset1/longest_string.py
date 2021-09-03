s = 'azcbobobegghakl'

# create a list to save the substrings
words = []

# create a variable to save each word through the process
word = s[0]

# loop through the string to compare each later
for i in range(len(s) - 1):
    if s[i + 1] >= s[i]:
        word += s[i + 1]
    else:
        words.append(word)
        word = s[i + 1]
words.append(word)

# from the list find the longest word and return it
longest = max(words, key=len)
print("Longest substring in alphabetical order is:", longest)