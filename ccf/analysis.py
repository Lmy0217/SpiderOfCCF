import json
import re


def fuzzyfinder(user_input, collection):
    suggestions = []
    pattern = user_input
    #pattern = '.*?'.join(user_input)  # Converts 'djm' to 'd.*?j.*?m'
    regex = re.compile(pattern)  # Compiles a regex.
    for item in collection:
        match = regex.search(item)  # Checks if the current item matches the regex.
        if match:
            suggestions.append((len(match.group()), match.start(), item))
    return [x for _, _, x in sorted(suggestions)]


with open('papers.json') as f:
    papers = json.load(f)

for key,value in papers.items():
    print(key + ": ", end='')
    print(fuzzyfinder('e-id', value))