import time
import os

counter = 1
# change to file directory
cwd = os.chdir("directory")

# infinite loop to check if any additional file is present
while True:
	old_file_list = os.listdir("directory")
	# wait 1 sec to prevent overworking
	time.sleep(1)
	new_file_list = os.listdir("directory")
	if old_file_list != new_file_list:
		# get extension name
		extension = os.path.splitext(new_file_list[counter])[1]
		# add extension name to new copied file
		os.rename(new_file_list[counter], str(counter) + extension)
		counter+=1