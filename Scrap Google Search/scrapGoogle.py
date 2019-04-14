import requests,bs4,sys,webbrowser

print('goggling the result')
res=requests.get('https://www.google.com/search?q='+''.join(sys.argv[1:]))
try:
	res.raise_for_status()	

except Exception as exc:
    print('There was a problem: %s' % (exc))

# res.text would give the .html format of the page 
googleSoup=bs4.BeautifulSoup(res.text)
linkElems=googleSoup.select('.r a')
maxLink=min(5,len(linkElems))

for i in range(maxLink):
	webbrowser.open('http://www.google.com' + linkElems[i].get('href'))

