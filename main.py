import random
import urllib.request

def nkar(url):
   name = random.randrange(1, 100)
   name = str(name) + ".jpeg"
   urllib.request.urlretrieve(url, name)

nkar("https://cdn.arstechnica.net/wp-content/uploads/2019/10/GettyImages-977644614-800x869.jpg")
