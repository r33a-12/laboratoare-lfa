import json

def load(filename):
    with open(filename) as f:
        return json.load(f)

def run(config, input_string):
    current_state = config["start_state"]
    transitions = config["transitions"]
    alphabet = set(config["alphabet"])

    for symbol in input_string:
        if symbol not in alphabet:
            print(f"Simbol invalid: {symbol}")
            return False
        
        current_state = transitions[current_state][symbol]

    return current_state in config["accept_states"]

if __name__ == "__main__":
    config = load("dfa_config.json")

    while True:
        user_input = input("Introduceti un sir (sau 'exit'): ").strip()
        if user_input.lower() == "exit":
            break

        if run(config, user_input):
            print("Sir acceptat!")
        else:
            print("Sir respins!")