def finite_state_automaton(string):
    if string.endswith("ab"):
        print("Accepted")
    else:
        print("Rejected")

# Test strings
finite_state_automaton("ab")
finite_state_automaton("aab")
finite_state_automaton("xxab")
finite_state_automaton("aba")
finite_state_automaton("abc")