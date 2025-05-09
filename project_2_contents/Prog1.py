import sys

#table provided (nested dictionary)
parse_table = {
    'E': {'a': ['T', 'Q'], '(': ['T', 'Q']},
    'Q': {'+': ['+', 'T', 'Q'], '-': ['-', 'T', 'Q'], ')': ['epsilon'], '$': ['epsilon']},
    'T': {'a': ['F', 'R'], '(': ['F', 'R']},
    'R': {'+': ['epsilon'], '-': ['epsilon'], '*': ['*', 'F', 'R'], '/': ['/', 'F', 'R'], ')': ['epsilon'], '$': ['epsilon']},
    'F': {'a': ['a'], '(': ['(', 'E', ')']}
}

terminals = ['a', '+', '-', '*', '/', '(', ')', '$']
non_terminals = ['E', 'Q', 'T', 'R', 'F']

def predictive_parser(input_string):

    print(f"Input: {input_string}")

    #edge case: end marker not present.
    if not input_string.endswith('$'):

        print("Error: Input string must end with $")
        return False
    
    #initializes stack with $ and start symbol "E"
    stack = ['$', 'E']
    input_buffer = list(input_string)
    pointer = 0

    print(f"Initial Stack: {stack}")

    while len(stack) > 0:
        #peeks at top of the stack
        top = stack[-1]
        #print(f"The top is: '{top}'")
        current_input = input_buffer[pointer]

        #prints current state for tracing
        print(f"\nCurrent Input: '{current_input}', Top of Stack: '{top}', Stack: {stack}")

        if top in terminals:
            if top == current_input:
                matched_terminal = stack.pop()
                pointer += 1
                print(f"Action: Match '{matched_terminal}'. Stack after match {stack}")
            else:
                print(f"Error: Mismatch - Expected terminal '{top}', got '{current_input}'")
                return False
        elif top in non_terminals:
            try:
                production = parse_table[top][current_input]
                print(f"Action: Apply rule {top} -> {''.join(production)}")
                stack.pop()
                if production != ['epsilon']:
                    stack.extend(production[::-1])
            except KeyError:
                print(f"Error: No parsing table entry for ('{top}', '{current_input}')")
                return False
        else:
            #edge case
            print(f"Error: Invalid symbol '{top}' on stack.")
            return False
        
        #if stack is empty and input is not fully processed yet.
        if len(stack) == 0 and pointer < len(input_buffer):
            print("Error: Stack empty but input remaining.")
            return False
        
    #double checks stack is empty and input fully read
    if pointer == len(input_buffer): #this checks if $ is the last symbol read
        print("\nFinal Stack: [] (Empty after matching $)")
        return True

    else:
        #in case the loop is terminated unexpectedly
        print(f"\nError: Parsing finished but input not fulled consumed. Remaining input: {''.join(input_buffer[pointer:])}")
        return False


#testing with provided input strings
        
if __name__ == "__main__":

    test_strings = ["(a+a)*a$", "a*(a/a)$","a(a+a)$", "(a+a)$", "(a+a)e$", "(a+a)"]

    #enumerate() takes a list and assigns numbers to them
    #i is the number, s is the string
    for i, s in enumerate(test_strings):
        print(f"\nTesting String {i + 1} : {s}.")
        is_accepted = predictive_parser(s)

        if is_accepted:
            print("Output: String is accepted/valid.")
        else:
            print("Output: String is not accepted/In valid.")
        
        #separator for different inputs
        print("\n")
