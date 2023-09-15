"""
File: boggle.py
Name: Michelle
----------------------------------------
This program simulates a classic game, boggle.
In the beginning, we allow users to input the
combination of sixteen letters (4x4). Then,
we will find out all the answers recursively.
During the process of searching, as soon as a
word is found, it will print "Found: 'word'"
in the Python console. After finding out all
the possible answers, this program will show
how long the searching process is and terminate
the program.
"""

import time  # This file allows you to calculate the speed of your algorithm

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	Thinking:
		This program simulates the boggle game. First, user has to input the
		4x4 combination of letters as the base of game. Next, the program
		will start to look for all the possible answers in the base. While
		searching, it will let user know the words which have been found at
		the present by printing 'Found: word' in the Python console. The program
		also calculates the time needed by the searching process, and show the
		time right after the possible words are found. At the same time, print
		how many words exist in this boggle game. Notice that if the input by
		the user does not meet the requirement, the program will be terminated
		right away.
	"""
	arr_in = []
	for i in range(4):
		s = input(str(i + 1) + ' row of letters: ')
		# if there are only four letters in s and each letter is alpha, the flag is equal to one
		flag = 1
		tokens = s.split()
		if len(tokens) == 4:
			for j in range(len(tokens)):
				if tokens[j].isalpha() and len(tokens[j]) == 1:
					# make each letter a lowercase and rewrite the original one in tokens
					tokens[j] = tokens[j].lower()
				else:
					flag = 0
		else:
			flag = 0
		if flag:
			# create a 2D array
			arr_in.append(tokens)
		else:
			print('Illegal input')
			break
	# print(arr_in)
	start = time.time()
	###############################
	word_lst = read_dictionary()
	count = 0
	for i in range(4):
		for j in range(4):
			ans = boggle(i, j, arr_in, [(i, j)], arr_in[i][j], word_lst, [], {})
			# print(ans)
			count += len(ans)
	# print(count)
	print('There are ' + str(count) + ' words in total.')
	###############################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def boggle(i, j, arr_in, index_lst, current_str, word_lst, ans_lst, memo):
	"""
	:param i: int, row number
	:param j: int, column number
	:param arr_in: list, all input given by user
	:param index_lst: empty list for storing index
	:param current_str: str, empty string for storing current english letter
	:param word_lst: list, a list of words in the dictionary
	:param ans_lst: list, an empty list for storing the correct words found in the word_lst
	:param memo: dict, to store the sub_string
	:return: list, all the correct words
	"""
	if len(current_str) >= 4 and current_str in word_lst and current_str not in ans_lst:
		ans_lst.append(current_str)
		print(f'Found "{current_str}"')
	for k in range(i-1, i+2, 1):
		for p in range(j-1, j+2, 1):
			if 3 >= k >= 0 and 3 >= p >= 0:
				if (k, p) not in index_lst:

					# choose
					current_str += arr_in[k][p]
					index_lst.append((k, p))

					# Check if the substring has been checked before
					if current_str not in memo:
						memo[current_str] = has_prefix(current_str, word_lst)

					if memo[current_str]:
						# explore
						boggle(k, p, arr_in, index_lst, current_str, word_lst, ans_lst, memo)

					# un-choose
					current_str = current_str[:-1]
					index_lst.pop()
	return ans_lst


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	# This program is to open the file and put all the words in a list.
	# Return a word list.
	lst = []
	with open(FILE, 'r') as f:
		for line in f:
			vocab = line.strip()
			lst.append(vocab)
	return lst


def has_prefix(sub_s, word_lst):
	# """
	# :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	# :return: (bool) If there is any words with prefix stored in sub_s
	# """
	"""
	:param sub_s: string, a part of the input word
	:param word_lst: the list of words in the dictionary
	:return: boolean
	"""

	# Using binary search
	left_i, right_i = 0, len(word_lst) - 1

	while True:
		mid_i = (left_i + right_i) // 2
		mid_word = word_lst[mid_i]

		if mid_word.startswith(sub_s):
			return True
		elif sub_s > mid_word:
			left_i = mid_i + 1
		elif sub_s < mid_word:
			right_i = mid_i - 1

		if left_i > right_i:
			break

	return False


if __name__ == '__main__':
	main()

