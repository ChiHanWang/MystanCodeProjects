"""
File: similarity.py
Name: Michelle
----------------------------
This program is an extension of assignment3!
It will compare short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    The program finds the highest similarity part of a long sequence from a short sequence.
    After the user input a long ssDNA sequence and a short ssDNA sequence, the program
    "scans through" the long ssDNA sequence to see which part matches the short DNA the most.
    """
    long_sequence = input('Please give me a DNA sequence to search: ').upper()
    short_sequence = input('What DNA sequence would you like to match? ').upper()
    match(long_sequence, short_sequence)


def match(long, short):
    """
    :param long: str, the long ssDNA sequence to be compared.
    :param short: str, the short ssDNA sequence.
    """
    maximum = 0     # The highest match score
    best_i = 0      # The index of the long ssDNA where the best matches starts from

    for i in range(len(long) - len(short) + 1):     # Has to compare at least
                                                    # (len(long) - len(short) + 1) times
        count = 0
        for j in range(len(short)):     # Compare each nucleotide and count how many matches there are
            if long[i+j] == short[j]:   # i : The index of the long ssDNA that the short ssDNA matches
                count += 1

        if count > maximum:             # To see if this score is better than previous
            maximum = count
            best_i = i

    print('The best match is ' + long[best_i:best_i + len(short)])


# --- DO NOT EDIT CODE BELOW THIS LINE --- #
if __name__ == '__main__':
    main()

