"""
File: weather_master.py
Name: Michelle
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""

EXIT = -100


def main():
	"""
	We can calculate different values of the weather's temperature.
	"""
	print('stanCode \"Weather Master 4.0"!')  # is equal to print('stanCode "Weather Master 4.0"!')
	temp = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)?'))

	if temp == EXIT:
		print('No temperatures were entered.')

	else:
		# Initial values for the Weather Master 4.0
		max_temp = temp
		min_temp = temp
		days = 1  # Count how many days there are and will be used to calculate the average temperature
		total_temp = temp

		# Check if the first temperature is a "cold day"
		if temp < 16:
			cold_day = 1
		else:
			cold_day = 0

		while True:
			temp = int(input('Next Temperature: (or' + str(EXIT) + 'to quit)?'))
			if temp == EXIT:
				break
			else:
				if temp > max_temp:  # Update max_temp when the input temperature is higher than the original value
					max_temp = temp
				if temp < min_temp:  # Update min_temp when the input temperature is lower than the original value
					min_temp = temp

				days += 1  # Update days
				total_temp += temp  # Update total temperature
				if temp < 16:  # Update cold days
					cold_day += 1

		# Show the results
		print('Highest temperature = ' + str(max_temp))
		print('Lowest temperature = ' + str(min_temp))
		print('Average = ' + str(total_temp / days))
		print(str(cold_day) + ' cold day(s)')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
