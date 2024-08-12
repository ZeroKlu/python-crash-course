def encrypt_decrypt(text: str, key: int) -> str:
    outString = []

    for i in range(len(text)):
        outString.append(chr(ord(text[i]) ^ key))
    
    return "".join(outString)

def main() -> None:
    key = 30
    
    text = "Hello World!"
    print(f"Plain Text:     {text}")

    cipherText = encrypt_decrypt(text, key)
    print(f"Encrypted Text: {cipherText}")

    plainText = encrypt_decrypt(cipherText, key)
    print(f"Decrypted Text: {plainText}")

if __name__ == "__main__":
    main()
