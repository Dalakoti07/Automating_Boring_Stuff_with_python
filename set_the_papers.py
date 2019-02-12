import os
import random
'''
	How to use this python script:
		add this .py file and data.txt (this contain a state and its capital,a state and its capital and next line and so on ) in same directory and change the directory in the script as per your computer and set back and see the magic
		answer in the papers are from https://state.1keydata.com/state-capitals.php
		Happy coding :)
'''
filename='data.txt'
# create 35 questions papers and 35 answer sheets, each paper containing 50 MCQ
states=[]
capitals=[]

file=open(filename,'r')
lines=file.readlines()
#print(lines)

for line in lines:
	set_mixed=line.rstrip().split('\t') # rstrip to remove \n from the right of the string 
	a=1	# one is state and another is capital   
	for i in set_mixed:
		if(a%2):
			states.append(i)
			a=a+1
		else:
			capitals.append(i)
			a=a+1

# now we have list of capitals and their correspondig states
# making the question paper, each question would be 'Captal of ___ is ____, then 4 options'
def set_one_paper(filename):
	set_s=set()	#this set will contain the states that have been added in the question paper, so that we donot add same question more than one time
	file=open(filename+'.txt','w')
	file_answer=open(filename+"_answer.txt",'w')
	i=1
	answer_sheet=""
	# this would conatin all the answers
	while len(set_s)!=50 :
		state_no=random.randint(0,49)
		if(state_no in set_s ):
			continue # if same set number generated then no need to do anything just continue
		set_s.add(state_no)
		state=states[state_no]
		capital=capitals[state_no]
		#one optimization can be done
		quest_str='\nQuestion number '+str(i)+'\n'+'What is the capital of '+state+'\n'
		answer_sheet+="answer for "+str(i)+" question is "+capital+"\n\n"
		file.write(quest_str)
		sum=1+2+3+4
		dic_option={}
		def get_option(i):
			list_op=['','option1','option2','option3','option4']
			return list_op[i]
		index_set=set()
		while len(index_set)!=3:
			ran_index=random.randint(1,4)
			ran_wa=random.randint(0,49)
			if(ran_index in index_set or ran_wa==state_no):
				continue
			index_set.add(ran_index)
			#insert wa answer in dictionary
			dic_option[get_option(ran_index)]=capitals[ran_wa]
		in_sum=0
		for z in index_set:
			in_sum=in_sum+z
		#fill the correct answer
		dic_option[get_option(sum-in_sum)]=capital
		#print(len(dic_option))
		option_str=""
		options=['option1','option2','option3','option4']
		for d in options:
			option_str+=d + " "+dic_option[d]+"\t"
		option_str+='\n'
		file.write(option_str)
		i=i+1
	file_answer.write(answer_sheet)
	file_answer.close()
	file.close()

# now create the file name like test [1,2,.....50] and answer[1,2,3,...50]
filename='test'
os.chdir('C:\\Users\\saurabh\\Desktop\\Blasteroid\\automating_boring_stuff_with_python\\test_papers')
for i in range(1,36):
	# making test for 35 students and set cwd as something else
	set_one_paper(filename+str(i))
