import rstr
import re

def generate_strings_for_regex(regex_list, count=3):
    generated_strings_list = []
    for regex in regex_list:
        print(f"\nProcessing regex: {regex}")
        try:
            pattern = re.compile(regex)
            generated_set = set()
            generated_strings = []
            attempts = 0

            while len(generated_strings) < count and attempts < 100:
                generated_string = rstr.xeger(pattern)
                if generated_string not in generated_set:
                    transitions = generate_transitions(generated_string)
                    generated_set.add(generated_string)
                    generated_strings.append((generated_string, transitions))
                attempts += 1

            generated_strings_list.append(generated_strings)

        except re.error as e:
            print(f"Invalid regex: {regex} - {str(e)}")

    return generated_strings_list

def generate_transitions(string):
    transitions = []
    for i, char in enumerate(string):
        if i == 0:
            transitions.append(f"Start -> {char}")
        else:
            transitions.append(f"{string[i - 1]} -> {char}")
    return transitions

# --- Main Program with Keyboard Input ---
if __name__ == "__main__":
    regex_list = []
    num_regex = int(input("Enter the number of regex patterns: "))
    for i in range(num_regex):
        regex = input(f"Enter regex pattern {i + 1}: ")
        regex_list.append(regex)

    generated_strings_list = generate_strings_for_regex(regex_list)

    print("\nGenerated strings for each regex:")
    for i, regex_strings in enumerate(generated_strings_list):
        print(f"\nFor regex {i + 1}: {regex_list[i]}")
        for string, transitions in regex_strings:
            print(f"  Generated string: {string}")
            print("  Transitions:")
            for transition in transitions:
                print(f"    {transition}")
