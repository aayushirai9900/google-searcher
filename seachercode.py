import webbrowser
from googlesearch import search
query = input("Enter what you want to search\n")
for j in search(query, tld="co.in", num=1, stop=1, pause=1): 
    webbrowser.open_new(j)
