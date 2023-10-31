
def encode(password):
    # Referenced from lab 6 pdf.
    # Empty 'encoded_pass' string.
    encoded_pass = ''
    # Loop that reiterates each character in 'password'.
    for num in password:
        # Shifts each character up by 3.
        shift_num = str((int(num) + 3))
        # Appends each character shift to the 'encoded_pass' string.
        encoded_pass += shift_num
    # Returns 'encoded_pass' string.
    return encoded_pass

def decode(password):
    # Declares decoded string
    dco = ""
    # Counter for while loop
    c=0
    # Loops through each digit in the password string
    while c < len(eco):
        # Each digit gets shifted down 3 based on starting digit
        if password[c] == "0":
            dco += "7"
        elif password[c] == "1":
            dco += "8"
        elif password[c] == "2":
            dco += "9"
        elif password[c] == "3":
            dco += "0"
        elif password[c] == "4":
            dco += "1"
        elif password[c] == "5":
            dco += "2"
        elif password[c] == "6":
            dco += "3"
        elif password[c] == "7":
            dco += "4"
        elif password[c] == "8":
            dco += "5"
        elif password[c] == "9":
            dco += "6"
        c += 1
    # Returns new decoded password
    return dco

# User menu.
def menu_display():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print()

if __name__ == '__main__':
    user_input = 0
    # While loop that displays the menu true.
    while True:
        menu_display()
        user_input = input('Please enter an option: ')

        # Encodes user input password.
        if user_input == '1':
            # Prompts user to input password to encode.
            user_pass = input('Please enter your password to encode: ')
            # Converts user input password to encoded password.
            # Stores encoded password as a variable.
            encoded_password = encode(user_pass)
            print('Your password has been encoded and stored!')
            print()

        # Decodes the stored encoded password.
        # WIP
        elif user_input == '2':
            pass

        # Ends the menu.
        # Finished.
        elif user_input == '3':
            break
