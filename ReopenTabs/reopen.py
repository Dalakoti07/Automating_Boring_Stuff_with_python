import webbrowser

with open('C:\\Users\\saurabh\\Desktop\\tabs.txt') as fp:
	lines=fp.readlines()
	for link in lines:
		webbrowser.open(link)