def encrypt(text, rot):
    new_str = ""
    for char in text:
        new = rotate_character(char,rot)
        new_str = new_str + new
    return new_str

def alphabet_position(letter):
    for char in letter:
        if char.isupper():
            pos = ord(char)-65
        elif char.islower():
            pos = ord(char)-97
        return pos

def rotate_character(char, rot):
    if char.isalpha():
        pos = (alphabet_position(char))+ rot
        if pos > 25:
            pos = pos - 26

        if char.isupper():
            new_pos = pos + 65
            new_pos = chr(new_pos)

        if char.islower():
            new_pos = pos + 97
            new_pos = chr(new_pos)

        return new_pos
    else:
        return char
