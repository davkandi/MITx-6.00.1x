import string

def build_shift_dict(shift):
    '''
    Creates a dictionary that can be used to apply a cipher to a letter.
    The dictionary maps every uppercase and lowercase letter to a
    character shifted down the alphabet by the input shift. The dictionary
    should have 52 keys of all the uppercase letters and all the lowercase
    letters only.

    shift (integer): the amount by which to shift every letter of the
    alphabet. 0 <= shift < 26

    Returns: a dictionary mapping a letter (string) to
             another letter (string).
    '''
    dict = {}
    for i in string.ascii_lowercase:
        dict[i] = string.ascii_lowercase[(string.ascii_lowercase.index(i) + shift) % 25]

    for i in string.ascii_uppercase:
        dict[i] = string.ascii_uppercase[(string.ascii_uppercase.index(i) + shift) % 25]

    return dict


print(build_shift_dict(3))

message_text = 'bonjouR'

def apply_shift(shift):
    '''
    Applies the Caesar Cipher to self.message_text with the input shift.
    Creates a new string that is self.message_text shifted down the
    alphabet by some number of characters determined by the input shift

    shift (integer): the shift with which to encrypt the message.
    0 <= shift < 26

    Returns: the message text (string) in which every character is shifted
         down the alphabet by the input shift
    '''
    message = ''
    for i in message_text:
        if i in string.ascii_letters:
            message += str(build_shift_dict(shift)[i])
        else:
            message += i

    return message

print(apply_shift(3))