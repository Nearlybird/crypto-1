from helpers import alphabet_position, rotate_character

def coderots(key):
    rot_list = []
    for letter in key:
        num = alphabet_position(letter)
        rot_list.append(num)
    return rot_list

def encrypt(message, key):
    #initialize an output message
    output = ""
    rot_list = coderots(key)
    counter = 0
    #print(rot_list)
    #iterate through each letter in message
    for letter in message:
        #if it is a letter and not space or punctuation
        if letter.isalpha() == True:
            #for each letter in message iterate through key
            new_let = rotate_character(letter, rot_list[counter])
                #for each letter in key access its position in the alphabet
            counter += 1
                #Then advance letter in message by that much
            if counter > len(key)-1:
                counter = 0
            output += new_let
        #otherwise just append the punctuation to the output
        else:
            output += letter
    return output

def main():
    from sys import argv
    if argv[1].isalpha == True:
        message = input("What message do you wish to encrypt?\n")
        # key = input("What is the codeword to encrypt the message with?\n")
        key = argv[1]
        print(encrypt(message, key))
    else:
        print("Please type a code phrase or word next time, you dingus. Remember: no punctuation or numbers.")
        exit()
if __name__ == "__main__":
    main()
