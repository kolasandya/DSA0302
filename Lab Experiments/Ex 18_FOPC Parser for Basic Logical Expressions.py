import re

def parse_fopc(expression):
    pattern = r'([A-Za-z]+)\((.*?)\)'
    matches = re.findall(pattern, expression)

    if matches:
        print("Valid FOPC Expression")
        print("Predicate:", matches[0][0])
        print("Arguments:", matches[0][1].split(','))
    else:
        print("Invalid FOPC Expression")


expression = "Likes(John,Mary)"

print("Expression:", expression)
parse_fopc(expression)