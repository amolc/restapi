import requests
import logging
import json

# These two lines enable debugging at httplib level (requests->urllib3->http.client)
# You will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
# The only thing missing will be the response.body which is not logged.
try:
    import http.client as http_client
except ImportError:
    # Python 2
    import httplib as http_client
http_client.HTTPConnection.debuglevel = 1

# You must initialize logging, otherwise you'll not see debug output.
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


hostname = 'http://localhost:8081'
# my_headers = {"content-type":"application/json",'User-agent':'Skor/6 Android|HUAWEI TIT-AL00|5.0|150'}
# query = '{"username":"amolch001@gmail.com","password":"10gXWOqeaf!" }'
# response = requests.post(hostname+'/profiles/api/token-auth/',data=query,headers=my_headers )
# data = response.json()
# token = data['token']
# print(token)

token = "83f298fab6bc6f7a28df6bfab00f3fd163384da9"
hostname = 'http://localhost:8081'
my_headers = {"content-type":"application/json","User-agent":"Skor/6 Android|HUAWEI TIT-AL00|5.0|150"}

key = "Authorization"
authtoken = "Token "+ token
my_headers[key] = authtoken
# print(my_headers)


# response = requests.get(hostname+'/profiles/api/departments/',headers=my_headers )
# data = response.json()
# print(data)



createcompany = '{"img_display":"main.jpg","img_thumbnail": "imgthumbnail.jpg","name" : "tata22","slug":"tata22","domain":"www.tata.com", "country":"Singapore", "timezone":"timezone","region":"12", "business_Unit":"1", "department":"finance" }'


   
email = "abssscd@corp.com"
password = "10gXWOqeaf!"
organization = "tata22"
department = "finance-198"
first_name = "Spur"
last_name = "Connect Test"

createuser = {}
createuser["email"] = email
createuser["password"] = password
createuser["organization"] = organization
createuser["department"] = department
createuser["first_name"] = first_name
createuser["last_name"] = last_name


createstring = json.dumps(createuser)
print(createstring)
response = requests.post(hostname+'/profiles/api/createorganisation/',data=createstring,headers=my_headers)
data = response.json()
print(data)








