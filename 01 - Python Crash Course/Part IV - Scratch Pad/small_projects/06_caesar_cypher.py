"""Caesar Cipher - shift cipher to encrypt and decrypt letters."""
# https://en.wikipedia.org/wiki/Caesar_cipher

# Note: Additional symbols could be added
SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def select_action():
    """Have user decide whether to encrypt or decrypt"""
    while True:
        entry = input("Do you want to [e]ncrypt or [d]ecrypt?\n> ").lower()
        if entry.startswith("e"):
            action = "encrypt"
            break
        elif entry.startswith("d"):
            action = "decrypt"
            break
        print("Please enter a valid selection (e | d)")
    return action

def select_key():
    """Have user enter a key to shift"""
    max_key = len(SYMBOLS) - 1
    while True:
        entry = input(f"Please enter a key (0 to {max_key}) to use.\n> ")
        if not entry.isdecimal():
            continue
        key = int(entry)
        if 0 <= key <= max_key:
            return key

def translate(action, key, message):
    """Perform the translation"""
    if action == "encrypt":
        encrypt(key, message)
    else:
        decrypt(key, message)

def encrypt(key, message):
    """Encrypt the message"""
    result = ""
    for symbol in message:
        if symbol in SYMBOLS:
            pos = SYMBOLS.find(symbol) + key
            if pos >= len(SYMBOLS):
                pos -= len(SYMBOLS)
            result += SYMBOLS[pos]
        else: result += symbol
    print(f"Message encrypts to:\n\t{result}")

def decrypt(key, message):
    """Decrypt the message"""
    result = ""
    for symbol in message:
        if symbol in SYMBOLS:
            pos = SYMBOLS.find(symbol) - key
            if pos < 0:
                pos += len(SYMBOLS)
            result += SYMBOLS[pos]
        else: result += symbol
    print(f"Message decrypts to:\n\t{result}")

def main():
    """Main program"""
    print("The Caesar cipher encrypts letters by shifting them over by a key number.")
    print("For example, a key of 2 means the letter A is encrypted into C," + \
          " the letter B encrypted into D, and so on.\n")

    action = select_action()
    key = select_key()
    message = input(f"Please enter a message to {action}:\n> ").upper()
    translate(action, key, message)

if __name__ == '__main__':
    main()
