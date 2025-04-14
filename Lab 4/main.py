import re
import random

def generate_strings_for_regex(regex_list):
    generated_strings_list = []
    for regex in regex_list:
        print("Processing regex:", regex)
        try:
            pattern = re.compile(regex)
            generated_set = set()
            generated_strings = []
            attempts = 0
            while len(generated_strings) < 3 and attempts < 100:
                generated_string, transitions = generate_string(regex)
                if pattern.fullmatch(generated_string) and generated_string not in generated_set:
                    generated_set.add(generated_string)
                    generated_strings.append((generated_string, transitions))
                attempts += 1
            generated_strings_list.append(generated_strings)
        except re.error:
            print("Invalid regex:", regex)
    return generated_strings_list

def generate_string(regex):
    string = ""
    transitions = []
    i = 0
    while i < len(regex):
        if regex[i] == "(" and regex.find(")", i) != -1:
            char = random.choice(options(re.findall(r'\((.*?)\)', regex[i:])[0]))
            string += char
            transitions.append((f"{string[-2]} -> {char}" if len(string) >= 2 else f"Start -> {char}"))
            i = regex.find(")", i)
        elif regex[i] not in '(){|+*?}':
            string += regex[i]
            transitions.append((f"{string[-2]} -> {string[-1]}" if len(string) >= 2 else f"Start -> {string[-1]}"))
        i += 1
    return string, transitions

def options(sequence):
    return sequence.split("|")

# Get regex list from user input
regex_list = []
num_regex = int(input("Enter the number of regex patterns: "))
for _ in range(num_regex):
    regex_list.append(input("Enter regex pattern: "))

generated_strings_list = generate_strings_for_regex(regex_list)
print("Generated strings for each regex:")
for i, regex_strings in enumerate(generated_strings_list):
    print(f"For regex {i + 1}: {regex_list[i]}")
    for string, transitions in regex_strings:
        print(f"  Generated string: {string}")
        print("  Transitions:")
        for transition in transitions:
            print(f"    {transition}")
