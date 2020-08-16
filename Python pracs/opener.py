import webbrowser

lines = open("hits.txt").read().splitlines()

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

for i in lines:
	webbrowser.get(chrome_path).open(str(i))
