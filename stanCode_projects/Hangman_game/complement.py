"""
File: complement.py
Name: Michelle
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    """
    This program will use string manipulation
    to find the complement strand of given DNA sequences  .
    """
    dna = input("Please Give me a DNA strand and I\'ll find the complement: ")
    new_dna = build_complement(dna.upper())
    if not new_dna:
        print("DNA strand is missing.")
    else:
        print('The complement of ' + dna + ' is ' + new_dna)


def build_complement(dna):
    """
    :param dna: str, the template used to make a complement ssDNA sequence.
    :return ans: str, the complement ssDNA sequence.
    """
    ans = ""
    for ch in dna:
        if ch == 'A':
            ans += 'T'
        elif ch == 'T':
            ans += 'A'
        elif ch == 'C':
            ans += 'G'
        else:
            ans += 'C'
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
