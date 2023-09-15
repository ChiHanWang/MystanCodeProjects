"""
File: caesar.py
Name: Michelle
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""

# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    This program helps users to decipher a secret sequence.
    Users need to input a number that helps the alphabet "shifts" into a different order.
    Then, when users enter the secret sequence, this program can translate
    the ciphered string into a deciphered string.
    """
    secret_num = int(input('Secret number: '))
    ciphered_string = input('What\'s the ciphered string? ')

    # Case-insensitive: reassign the ciphered string by making it to the upper-case one
    ciphered_string = ciphered_string.upper()

    ans = decode(secret_num, ciphered_string)
    print('The deciphered string is: ' + ans)


def decode(num, input_text):
    """
    :param num: int, the number that is used to offset the original order in the sequence.
    :param input_text: str, the test to be deciphered.
    :return: str, the deciphered texts.
    """
    new_seq = new_sequence(num)
    ans = ''

    for ch in input_text:

        if new_seq.find(ch) != -1:      # When the character is not a space or a symbol,
                                        # shift the character back to the original one
                                        # and add to ans.
            ans += ALPHABET[new_seq.find(ch)]

        else:                           # Add whatever string that is not an alphabet.
            ans += ch

    return ans


def new_sequence(num):
    """
    :param num: int, the number that is used to offset the original order in the sequence.
    :return: str, the "shifted" version of the ALPHABET.
    """
    first_half = ALPHABET[:len(ALPHABET)-num]
    second_half = ALPHABET[len(ALPHABET)-num:]

    return second_half + first_half


# --- DO NOT EDIT CODE BELOW THIS LINE --- #
if __name__ == '__main__':
    main()
