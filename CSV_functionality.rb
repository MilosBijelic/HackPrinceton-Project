##################################################
# Description: a class to handle all of the data stroage for the website 
# Creates the users csv and inputs all of the data from the website into their personal csv file

# By Milos Bijelic 

# Version: 0.1.0	-	Inital release: create csv and initalize the habits and mood 
##################################################

require 'CSV'

class DATA_ORG

	#Creates a file in the storage directory with the users name
	#This file will store all of their habits and mood info
	def create_habits_csv(user)
		CSV.open("#{user}.csv", "r")
	end

	#Takes the input from the website and initalizes all their habits 
	#inside their spreadsheet
	def initialize_habits(user)
		# Change path and "habits.csv" name for git commit
		habits = CSV.read('C:\Users\Milos\Desktop\coding_projects\hack_princeton_2017\CSV_input_output\habits.csv')
		iterations = CSV.read('C:\Users\Milos\Desktop\coding_projects\hack_princeton_2017\CSV_input_output\habits.csv').length 

		CSV.open("#{user}.csv", "r") do |csv|
			i = 0

			while iterations > i do
				#on the first iteration puts "habits" as the header
				if i == 0
					csv << "habits"
				end 
				#puts all of the values in habits.csv from website into the users csv
				csv << habits[i]
				i++
			end

			#writes the last column "mood" into the csv 
			csv << "mood"
		end
	end

	# Appends the users habit and mood info for a given day 
	def append_daily_info 
		#date 
		#habit(s) 1/0 
		#mood (1-10)
	end
end

if __FILE__ == $0
	#temp way to get user name 
	puts "input a user name" 
	user_name = gets.chomp

	DATA_ORG.create_habits_csv(user_name)
	# DATA_ORG.data_initialize_habits(user_name)
end