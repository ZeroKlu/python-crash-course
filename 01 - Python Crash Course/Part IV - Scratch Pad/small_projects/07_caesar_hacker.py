"""Caesar Cipher Hacker - Brute-force attack (try every key)"""

print("Caesar Cipher Hacker")
message = input("Please enter the encrypted message to hack.\n> ")

SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for key in range(len(SYMBOLS)):
    translated = ""
    for symbol in message:
        if symbol not in SYMBOLS:
            translated += symbol
            continue
        pos = SYMBOLS.find(symbol) - key
        if pos < 0:
            pos += len(SYMBOLS)
        translated += SYMBOLS[pos]
    print(f"Key: #{str(key).rjust(2)} : {translated}")
