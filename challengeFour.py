
import urllib.request
import urllib.parse

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
# Previously 12345, then 80992, 8022
nextLink = 63579

while True:
    try:
        response = urllib.request.urlopen(url+str(nextLink))
        html = response.read()
        html = html.decode("utf-8")
        nextLink = html.strip("and the next nothing is")
    except:
        break
    print(html)
    print(nextLink)