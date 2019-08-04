# what this .py would do is create json for main.py code
import json
import os

# pathTargeted is the dir where all new the .cpp files when created would have plugin data
# pathSample is the dir for coresponding dir's new file's sample code 
pathTargeted=r'C:\Users\saurabh\Desktop\Blasteroid\Competitive Programming\Coding Ninjas\Dynamic Programming'
pathSample=r''
# below is the code to covert dictionary to json upto line 15 and write 
# object to .json file 

#now loading the .json file and 
# file=open('records.json','r')
# content=file.read()
# contentList=json.loads(content)
# print(type(contentList))
# print(contentList)

# print(contentList["type1"]["FilesAlreadInDir"])
# listOfFiles=contentList["type1"]["FilesAlreadInDir"]
# initiating the program
listOfFiles=[]
for file in os.listdir(pathTargeted):
	    if file.endswith(".cpp"):
	        listOfFiles.append(file)
records={}
records["type1"]={"files":".cpp","sampleDir":"PUTTHEPATH of sample code","targetDir":pathTargeted,"FilesAlreadInDir":listOfFiles}

# print(listOfFiles)
# print(json.dumps(records)) # json.dumps() covert dictionary to json object
file=open('records.json','w')
file.write(json.dumps(records))