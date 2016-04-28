import os
import datetime
import string
import glob

def create_files(path_to_dir=os.getcwd()):
	for s in string.ascii_uppercase:
		with open(path_to_dir +'/'+ s + '.txt', 'a') as f:
			f.write(str(datetime.datetime.now()) + '\n')

def create_dirs(path_to_dir=os.getcwd()):
	for directory in string.ascii_uppercase[0:10]:
		if not os.path.exists(path_to_dir + '/' + directory):
				os.makedirs(path_to_dir + '/' + directory)

def get_dirs_in_current_dir(path_to_dir=os.getcwd()):
	return glob.glob(path_to_dir+'/'+'*/')

for directory in get_dirs_in_current_dir():
	create_dirs(directory)
	for directory_j in get_dirs_in_current_dir(directory):
		create_dirs(directory_j)
		for directory_k in get_dirs_in_current_dir(directory_j):
			create_files(directory_k)


