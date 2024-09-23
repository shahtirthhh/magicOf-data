# https://python.langchain.com/v0.2/docs/introduction/
# https://python.langchain.com/v0.2/docs/concepts/
# https://python.langchain.com/v0.2/docs/tutorials/
import threading
import requests
from bs4 import BeautifulSoup

urls = ["https://python.langchain.com/v0.2/docs/introduction/","https://python.langchain.com/v0.2/docs/concepts/","https://python.langchain.com/v0.2/docs/tutorials/"]

def fetch_content(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content,"html.parser")
    print(soup.text)
    print(f"Fetched {len(soup.text)} from {url}")

threads = []

for url in urls:
    thread = threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()