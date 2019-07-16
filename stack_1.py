import use_stack as stack
equation = "[2+(9+2)()]"
brackets_pairs  = {
    "{" : "}",
    "[" : "]",
    "(" : ")"
}
open_brackets = list(brackets_pairs.keys())
close_brackets = list(brackets_pairs.values())
brackets_list = open_brackets + close_brackets
is_equation_valid = True
simplified_equation = []
for character in equation:
    if character in brackets_list:
        simplified_equation.append(character)

# [()]

for element in simplified_equation:
    if element in open_brackets:
        stack.push(element)
    else:
        last_open_bracket = stack.pop()
        close_pair_last_open_bracket = brackets_pairs[last_open_bracket]
        if element != close_pair_last_open_bracket:
            is_equation_valid = False
            break
print(is_equation_valid)
