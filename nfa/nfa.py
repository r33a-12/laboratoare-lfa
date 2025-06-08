import json

def load(filename):
    with open(filename) as f:
        return json.load(f)
    
def run(config, input_string):
    current_states = set([config["start_state"]])
    transitions = config["transitions"]
    alphabet = set(config["alphabet"])

    for symbol in input_string:
        if symbol not in alphabet:
            print(f"Simbol invalid: {symbol}")
            return False
        
        next_states = set()

        for state in current_states:
            if symbol in transitions.get(state, {}):
                next_states.update(transitions[state][symbol])

        current_states = next_states

        if not current_states:
            break

    return any(state in config["accept_states"] for state in current_states)

if __name__ == "__main__":
    config = load("nfa_config.json")

    while True:
        user_input = input("Introduceti un sir (sau 'exit'): ").strip()
        if user_input.lower() == "exit":
            break

        if run(config, user_input):
            print("Sir acceptat de NFA!")
        else:
            print("Sir respins de NFA!")