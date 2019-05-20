from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    output = ""
    for letter in text:
        if letter.isalpha() == True:
            output += rotate_character(letter, rot)
        else:
            output += letter
    return output

def main():
    from sys import argv
    message = input("Type a message to be encodened:\n")
    if argv[1].isdigit() == True:
        coded = encrypt(message, int(argv[1]))
    #     # text = input("Type your message to be encrypted.\n")
    #     # rot = input("Enter your rotation.\n")
    #     # rot = int(rot)
    #     # message = encrypt(text, rot)
        print("Your encrypted message is:\n",coded)
    else:
        print("Please type a whole number next time, you dingus.")
    

if __name__ == "__main__":
    main()
