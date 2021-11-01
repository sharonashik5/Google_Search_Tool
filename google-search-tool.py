#Google Search Engine
from googlesearch import search

inp = input("Enter the text to be searched for : ")
for res in search(inp, start = 0, pause = 2):
    print(res)
