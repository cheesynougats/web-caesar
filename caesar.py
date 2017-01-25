def alphabet_position(letter):
    if letter.isupper():
        return ord(letter) - ord("A")
    else:
        return ord(letter) - ord("a")

def rotate_character(char, rot):
    if char.isupper():
        new_pos = ord("A") + ((alphabet_position(char)+rot)%26)
    else:
        new_pos = ord("a") + ((alphabet_position(char)+rot)%26)
    return chr(new_pos)



def encrypt(text, rot):
    return_str = ''
    for char in text:
        if char.isalpha():
            return_str += rotate_character(char, rot)
        else:
            return_str += char
    return return_str
