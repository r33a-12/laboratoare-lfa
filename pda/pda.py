import json

def load(filename):
    with open(filename) as f:
        return json.load(f)
    
def run(config, input_string):
    transitions = config["transitions"]
    stack = [config["start_stack_symbol"]]
    current_states = [(config["start_state"], stack.copy())]

    for symbol_index in range(len(input_string) + 1):
        next_states = []

        symbol = input_string[symbol_index] if symbol_index < len(input_string) else ""

        for state, stack in current_states:
            stack_top = stack[-1] if stack else None

            if state not in transitions or symbol not in transitions[state]:
                continue

            for top_check, actions in transitions[state][symbol].items():
                if top_check == stack_top:
                    for next_state, stack_actions in actions:
                        new_stack = stack[:-1] if top_check else stack[:]
                        new_stack.extend(reversed(stack_actions))
                        next_states.append((next_state, new_stack))

        current_states = next_states
        if not current_states:
            return False
        
    return any(state in config["accept_states"] for state, _ in current_states)

if __name__ == "__main__":
    config = load("pda_config.json")

    while True:
        user_input = input("Introduceti un sir cu paranteze (sau exit): ").strip()
        if user_input.lower() == "exit":
            break

        if run(config, user_input):
            print("Sir acceptat de PDA!")
        else:
            print("Sir respins de PDA!")