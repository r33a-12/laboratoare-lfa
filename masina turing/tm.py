import json

def load_tm_config(filename):
    with open(filename, "r") as f:
        return json.load(f)

def run_tm(tm_config, tape_input):
    tape = list(tape_input)
    head = 0
    state = tm_config["start_state"]
    accept = tm_config["accept_state"]
    transitions = tm_config["transitions"]

    marked_symbol = None  # simbolul care trebuie copiat

    while True:
        if head < 0:
            tape.insert(0, "_")
            head = 0
        elif head >= len(tape):
            tape.append("_")

        current_symbol = tape[head]

        if state == accept:
            return "".join(tape)

        if state not in transitions:
            print(f"Eroare: Stare {state} nu are tranzitii.")
            return "".join(tape)

        if current_symbol not in transitions[state]:
            print(f"Eroare: nicio tranzitie pentru ({state}, {current_symbol})")
            return "".join(tape)

        next_state, write_symbol, move_dir = transitions[state][current_symbol]

        # Setăm simbolul marcat la trecerea din q_start în q_seek_dollar
        if state == "q_start" and current_symbol in ["0", "1"]:
            marked_symbol = current_symbol

        # La scrierea în q_copy_symbol, scriem simbolul memorat
        if state == "q_copy_symbol" and write_symbol == "_":
            write_symbol = marked_symbol

        tape[head] = write_symbol
        state = next_state

        if move_dir == "R":
            head += 1
        elif move_dir == "L":
            head -= 1
        elif move_dir == "S":
            pass
        else:
            print(f"Eroare: directie necunoscuta {move_dir}")
            return "".join(tape)

def main():
    tm_config = load_tm_config("tm_config.json")
    tape_input = input("Introduceti sir binar cu delimitatori $ si #: ")
    result = run_tm(tm_config, tape_input)
    print("Banda finala:")
    print(result)

if __name__ == "__main__":
    main()
