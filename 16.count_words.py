'''Write a Python program to count the occurrences of each word in a
given sentence'''

import re
s =input("Enter a string")
word=r'\w+'
substring=re.findall(word,s)
print("Total substrings:",len(substring))


print("-----------------------------")

s=input("Enter a string")
count=0
for i in s:
    if (i==" "):
        count=count+1
print("Total words are:",count+1)
