
dfa = {
    'q0': {'a': 'q1', 'b': 'q0'},
    'q1': {'a': 'q1', 'b': 'q2'},
    'q2': {'a': 'q1', 'b': 'q0'}
}

initial_state = 'q0'
final_states = ['q2']


string = input("Enter the input string: ")

current_state = initial_state
path = [current_state]

valid = True

for ch in string:
    if ch not in ['a', 'b']:
        valid = False
        break
    current_state = dfa[current_state][ch]
    path.append(current_state)

if not valid:
    print("Invalid Input (Only 'a' and 'b' are allowed)")
else:
    print("Transition Path:")
    print(" → ".join(path))

    if current_state in final_states:
        print("Accepted")
    else:
        print("Rejected")
