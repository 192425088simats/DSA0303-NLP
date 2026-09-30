import re

text = input("Enter a text: ")
pattern = input("Enter a pattern: ")

result = re.search(pattern, text)

if result:
    print("Pattern found:", result.group())
else:
    print("Pattern not found")
