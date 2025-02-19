def decrypt_caesar_cipher(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift_amount - shift) % 26 + shift_amount)
        else:
            decrypted_text += char
    return decrypted_text

def brute_force_caesar_cipher(ciphertext):
    for shift in range(26):
        print(f"Shift {shift}: {decrypt_caesar_cipher(ciphertext, shift)}")

if __name__ == "__main__":
    ciphertext = input("Enter the ciphertext: ")
    brute_force_caesar_cipher(ciphertext)