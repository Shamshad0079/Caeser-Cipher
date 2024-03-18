def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr((ord(char) - 65 + key) % 26 + 65)
            elif char.islower():
                encrypted_text += chr((ord(char) - 97 + key) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                decrypted_text += chr((ord(char) - 65 - key) % 26 + 65)
            elif char.islower():
                decrypted_text += chr((ord(char) - 97 - key) % 26 + 97)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    while True:
        choice = input("Enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ")
        if choice == 'q':
            print("Exiting the program.")
            break
        elif choice == 'e':
            text = input("Enter the text to encrypt: ")
            key = int(input("Enter the encryption key (0-999): "))
            encrypted_text = encrypt(text, key)
            print("Encrypted text:", encrypted_text)
        elif choice == 'd':
            text = input("Enter the text to decrypt: ")
            key = int(input("Enter the decryption key (0-999): "))
            decrypted_text = decrypt(text, key)
            print("Decrypted text:", decrypted_text)
        else:
            print("Invalid choice. Please enter 'e', 'd', or 'q'.")

if __name__ == "__main__":
    main()
