import re

text = "Python is easy to learn. Python is powerful."

# Match: Checks only at the beginning of the string
match_result = re.match(r"Python", text)

if match_result:
    print("Match found:", match_result.group())
else:
    print("No match found")

# Search: Finds the first occurrence anywhere in the string
search_result = re.search(r"powerful", text)

if search_result:
    print("Search found:", search_result.group())
else:
    print("Pattern not found")