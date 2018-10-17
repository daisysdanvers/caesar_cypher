def CaesarCipher(string, shift=3):
    #we create our variables and transform the string in all lowercase so
    #to make the decryption easier.
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    result = []
    lower_string = string.lower()
    #the shift can be max of 26 positions.
    if shift > 26:
        return 'Shift value not valid.'
    #we decrypt each letter, catching first the blank space cases
    for letter in lower_string:
        if letter == ' ':
            result.append(letter)
        else:
            new_index = alphabet.index(letter) + shift
            #we catch the cases where the new index would go out of range
            if new_index > 25:
                new_index = new_index - 25
            decrypted_letter = alphabet[new_index]
            result.append(decrypted_letter)
    return ''.join(result)

def all_solutions(string):
    for i in range(1, 26):
        print i, CaesarCipher(string, i)


print all_solutions('LQIRUPDWLRQ VHFXULWB')
