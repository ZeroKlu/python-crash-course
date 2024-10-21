"""Test the morse code encoder and decoder"""

from morse import Morse

debug_mode = True

def main():
    """Run the program"""
    morse = Morse()
    if debug_mode:
        debug(morse)
    else:
        prog(morse)

def prog(morse):
    """Run the program"""
    valid_tasks = ["e", "d", "q"]
    while True:
        task = input("\nSelect a task: ([e]ncode, [d]ecode, [q]uit)\n> ")
        if task == "" or task[0].lower() not in valid_tasks:
            print("Invalid selection!")
            continue
        task = task[0].lower()
        if task == "q":
            break
        else:
            prefix = "en" if task == "e" else "de"
            message = input(f"Enter the message to {prefix}code:\n> ")
            result = morse.encode(message) if task == "e" else morse.decode(message)
            print(result)
            continue

def debug(morse):
    """Execute debug tests"""
    print(morse.decode("... --- ..."))
    print(morse.encode("SOS"))
    print(morse.decode("... -.-. --- - -_-- -.-. .-.. . .- -."))
    print(morse.encode("Scott McLean"))
    print(morse.decode("... -.-. --- - -_-- -.-. .-.. . .- -. ---..._.----." + \
                       " . -. .--- --- -.-- . .-._--- ..-._.--. -.-- - ...." + \
                       " --- -. .----."))
    print(morse.encode("Scott McLean: 'Enjoyer of Python'"))
    print(morse.decode(".- -... -.-. -.. . ..-. -.-. .... .. .--- -.- .-.." + \
                       " -- -. --- .--. --.- .-. ... - ..- ...- .-- -..-" + \
                       " -.-- --.. .---- ..--- ...-- ....- ..... -...." + \
                       " --... ---.. ----. ----- .-.-.- --..-- ..--.. -.-.-." + \
                       " ---... -....- -..-. .----. .-..-. -.--. -.--.- ..--.-"))
    print(morse.encode("ABCDEFCHIJKLMNOPQRSTUVWXYZ1234567890.,?;:-/'\"()_"))
    print(morse.encode("~"))

if __name__ == "__main__":
    main()
