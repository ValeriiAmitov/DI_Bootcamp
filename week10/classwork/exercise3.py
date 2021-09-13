
import os

weeks_name = ['week1', 'week2', 'week3', 'week4', 'week5']
days_name = ['day1', 'day2', 'day3', 'day4', 'day5']

for week_name in weeks_name:
	os.mkdir(week_name)

	for day_name in days_name:
		os.mkdir(os.path.join(week_name, day_name))

		os.mkdir(os.path.join(week_name, day_name, 'homework'))
		os.mkdir(os.path.join(week_name, day_name, 'lesson'))