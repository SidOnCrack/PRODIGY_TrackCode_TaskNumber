def caeD(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            sb = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - sb + shift) % 26 + sb)
        else:
            encrypted_text += char
    return encrypted_text

def caeE(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            sb = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - sb - shift) % 26 + sb)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    print("Caesar Cipher - Prodigy Info tech")
    print("Encrypting and Decrypting 1 to 3 values")
    
    while True:
        print("\nOptions:")
        print("1.Encrypt msg")
        print("2.Decrypt msg")
        print("3.Exit\n")
        choice = input("Enter choice 1/2/3: ").strip()

        if choice == '1':
            text = input("Enter encrypt msg: ").strip()
            shift = int(input("Enter shift value: ").strip())
            encrypted_message = caeE(text, shift)
            print(f"Encrypted msg: {encrypted_message}")
        elif choice == '2':
            text = input("Enter the message to decrypt: ").strip()
            shift = int(input("Enter shift value: ").strip())
            decrypted_message = caeD(text, shift)
            print(f"Decrypted msg: {decrypted_message}")
        elif choice == '3':
            print("byebye")
            break
        else:
            print("Invalid choice. Please select 1, 2 or 3")

if __name__ == "__main__":
    main()
