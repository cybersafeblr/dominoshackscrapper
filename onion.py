""" THIS TOOL IS DESIGNED BY g4g5j41n """
""" USE IT AT YOUR OWN RISK """""
""" Follow me for more tools and hacks @g4g5j41n, https://github.com/cybersafeblr"""

import requests
from requests.structures import CaseInsensitiveDict
import re
import os

num_list = open("numbers.txt", "r")
content = num_list.readlines()
headers = CaseInsensitiveDict()
headers["Accept"] = "*/*"
headers["Accept-Encoding"] = "gzip, deflate, br"
headers["Accept-Language"] = "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7"
headers["Connection"] = "keep-alive"
headers["Cookie"] = "_ga=GA1.1.252407706.1621920918; _ga_7592W6XHM5=GS1.1.1621926707.2.1.1621926710.0"
headers["DNT"] = "1"
headers["Host"] = "slf2rrahypck3bwckpdohsnhpeqrb3nhvwznjmarmweofwnptowe4mad.onion.ly"
headers["Referer"] = "https://slf2rrahypck3bwckpdohsnhpeqrb3nhvwznjmarmweofwnptowe4mad.onion.ly/?s=08"
headers["sec-ch-ua-mobile"] = "?0"
headers["Sec-Fetch-Dest"] = "empty"
headers["Sec-Fetch-Mode"] = "cors"
headers["Sec-Fetch-Site"] = "same-origin"
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
for user in content:
    print("Testing user" + user.strip())
    response = requests.get('http://xcgwv22shpmuzybdsnalqcufejtjlvqoukyybnjvrd3ppzsiti4anvyd.onion.ly/api/search/' +user.strip(), headers=headers)
    print(response.text)