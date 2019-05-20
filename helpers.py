def alphabet_position(letter):
    letter = letter.lower()
    alpha = "abcdefghijklmnopqrstuvwxyz"
    return alpha.find(letter)

def rotate_character(char, rot):
    output = ""
    alpha = "abcdefghijklmnopqrstuvwxyz"
    num = alphabet_position(char)
    num += rot
    if num % 26 >= 0:
        num = num % 26
        output = alpha[num]
    else:
        output = alpha[num]
    if char.isupper():
        return output.upper()
    else:
        return output.lower()
