import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
fp = urllib.request.urlopen("https://kingswildproject.com/collections/available-playing-cards?page=1")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

print(mystr)
fp = urllib.request.urlopen("https://kingswildproject.com/collections/available-playing-cards?page=2")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

print(mystr)
fp = urllib.request.urlopen("https://kingswildproject.com/collections/available-playing-cards?page=3")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

print(mystr)
fp = urllib.request.urlopen("https://kingswildproject.com/collections/available-playing-cards?page=4")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

print(mystr)
fp = urllib.request.urlopen("https://kingswildproject.com/collections/available-playing-cards?page=5")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

print(mystr)
fp = urllib.request.urlopen("https://kingswildproject.com/collections/available-playing-cards?page=6")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

print(mystr)