from art import logo

def caesar_cipher(text, shift):
    cipher = ""
    for char in text:
        if not char.isalpha():
            cipher += char
        elif direction == 'encode':
            index_val = alphabet.index(char)
            index_val += shift
            cipher += alphabet[index_val]
        else:
            index_val = alphabet.index(char)
            index_val += 26
            index_val -= shift
            cipher += alphabet[index_val]
    print(f"Your {direction}d message is : {cipher}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',\
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',\
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

end_of_cipher = False

print(logo)

while not end_of_cipher:
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n").lower()

    if direction == 'encode' or direction == 'decode':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        if shift == 26:
            while shift == 26:
                print("Shifting by 26 will return your original message with no cipher scrambling.")
                shift = int(input("Please enter a number other than 26:\n"))
        elif shift > 26:
            shift = shift % 26
        else:
            shift = shift
        caesar_cipher(text=text, shift=shift)
        question = (input("Would you like to use the Caesar Cipher again? Type 'yes' or 'no':\n")).lower()
        if question == 'no':
            print("Goodbye!")
            end_of_cipher = True
        else:
            end_of_cipher = False
    else:
        print("Please enter a valid option")