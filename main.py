import re
import requests

# get post head delete options put

r=requests.get('http://www.baidu.com')
print(r.cookies)