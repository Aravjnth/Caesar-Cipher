def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

text = "Aravinth_aj"
shift = 3
encrypted_text = caesar_cipher(text, shift)
print(f"Encrypted text: {encrypted_text}")