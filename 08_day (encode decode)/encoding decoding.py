def caesar_cipher():   
    print(''' ██████╗ ██████╗ ██████╗ ███████╗██████╗     ██████╗ ███████╗ ██████╗ ██████╗ ██████╗ ███████╗██████╗ 
    ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗    ██╔══██╗██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗
    ██║     ██║   ██║██║  ██║█████╗  ██████╔╝    ██║  ██║█████╗  ██║     ██║   ██║██║  ██║█████╗  ██████╔╝
    ██║     ██║   ██║██║  ██║██╔══╝  ██╔══██╗    ██║  ██║██╔══╝  ██║     ██║   ██║██║  ██║██╔══╝  ██╔══██╗
    ╚██████╗╚██████╔╝██████╔╝███████╗██║  ██║    ██████╔╝███████╗╚██████╗╚██████╔╝██████╔╝███████╗██║  ██║
     ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═════╝ ╚══════╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                                                          ''')
    print()
    print()
    
    
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    def encrypt():
        encrypted_text = ''
        for letter in text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = (position + shift)
                if new_position > 25:
                    new_position -= 26
                encrypted_text += alphabet[new_position]
            else: 
                encrypted_text += letter
        print(f"The encoded text is: {encrypted_text}")
    def decrypt():
        decrypted_text = ''
        for letter in text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = (position - shift)
                if new_position < 0:
                    new_position += 26
                decrypted_text += alphabet[new_position]
            else:
                decrypted_text += letter
        print(f"The decoded text is: {decrypted_text}")
    if direction == 'encode':
        encrypt()
    elif direction == 'decode':
        decrypt()
    else:
        print("Invalid option. Please type 'encode' or 'decode'.")
    print()
    print(''' ██████╗ ██████╗ ██████╗ ███████╗██████╗     ██████╗ ███████╗ ██████╗ ██████╗ ██████╗ ███████╗██████╗ 
    ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗    ██╔══██╗██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗
    ██║     ██║   ██║██║  ██║█████╗  ██████╔╝    ██║  ██║█████╗  ██║     ██║   ██║██║  ██║█████╗  ██████╔╝
    ██║     ██║   ██║██║  ██║██╔══╝  ██╔══██╗    ██║  ██║██╔══╝  ██║     ██║   ██║██║  ██║██╔══╝  ██╔══██╗
    ╚██████╗╚██████╔╝██████╔╝███████╗██║  ██║    ██████╔╝███████╗╚██████╗╚██████╔╝██████╔╝███████╗██║  ██║
     
        ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═════╝ ╚══════╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                                                            ''')
user_choice = 'yes'
while user_choice == 'yes':
    caesar_cipher()
    user_choice = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    