# what this .py would do is create json for main.py code
import json
import os

# pathTargeted is the dir where all new the .cpp files when created would have plugin data
# pathSample is the dir for coresponding dir's new file's sample code 
pathTargeted=r'C:\Users\saurabh\Desktop\Blasteroid\Competitive Programming\Coding Ninjas\Dynamic Programming'
pathSample=r'C:\Users\saurabh\Desktop\Blasteroid\automating_boring_stuff_with_python\C++ plugins\test.cpp'

listOfFiles=[]
for file in os.listdir(pathTargeted):
	    if file.endswith(".cpp"):
	        listOfFiles.append(file)
records={}
records["type1"]={"files":".cpp","sampleDir":"PUTTHEPATH of sample code","targetDir":pathTargeted,"FilesAlreadInDir":listOfFiles}

file=open('records.json','w')
file.write(json.dumps(records))