import os,re

new_dir=os.chdir('C:\\users\\saurabh\\desktop\\blasteroid\\automating_boring_stuff_with_python\\text_files')
all_files_in_dir=os.listdir(new_dir)
# filter out all txt file with re
#print(all_files_in_dir)
file_str=' '.join(all_files_in_dir)
file_str=file_str.lstrip()
print(file_str)
txt_files=re.findall('\s?[a-z_A-Z]+[0-9]*?.txt\s?',file_str)
solution=open('solution_to_search.txt','w')
print('find all the occurences of root ,type that root')
pattern=input()
solution_str=""
print(txt_files)
for i in txt_files:
	print('reading file ',i)
	# find the pattern in the file i
	i=i.strip()
	file=open(i,'r')
	data_of_whole_file=file.readlines()
	for j in data_of_whole_file:
		all_matches=re.findall('\s'+pattern+'[a-zA-Z]+',j)
		solution_str+=' '.join(all_matches)

print(solution_str)
solution.write(solution_str)
solution.close()