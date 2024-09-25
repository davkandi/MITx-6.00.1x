current = s[0]

substrings = []
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
for i in range(len(s) - 1):
    if s[i + 1] >= s[i]:
        current += s[i + 1]
    else:
        substrings.append(current)
        current = s[i + 1]

longest = max(substrings, key=len)

# In the case of ties, print the first substring
print("Longest substring in alphabetical order is: " + longest)
