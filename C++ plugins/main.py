import os
import json
# file=open('test.cpp') # this file has the content which need to be copied to each and every file
# content=file.read()

# # path where .cpp file need to changed when they are made
# path='C:\\Users\\saurabh\\Desktop\\Blasteroid\\Competitive Programming'
# os.chdir(path)


# read json and start working
file=open('records.json','r')
content=file.read()
contentList=json.loads(content)
taskOne=contentList["type1"]
filesAlreadyPresent=taskOne["FilesAlreadInDir"]

def writeToFile(files):
	content=open(taskOne["sampleDir"]).read()
	for file_name in files:
		filePath=os.path.join(taskOne["targetDir"],file_name)
		file=open(filePath,"w")
		file.write(content)
		file.close();	

while True:
	filesAlreadyPresent =[] # read it from .json file
	newFiles=[]
	# reading the content
	print(taskOne["targetDir"])
	for file in os.listdir(taskOne["targetDir"]):
	    if file.endswith(taskOne["files"]):
	        if file in filesAlreadyPresent == False:
	        	newFiles.append(file)
	        	filesAlreadyPresent.append(file) 
	
	if len(newFiles)>1:
		print(newFiles)
		writeToFile(newFiles)
	# print("waiting")