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




# hostname = 'http://localhost:8081'
# my_headers = {"content-type":"application/json",'User-agent':'Skor/6 Android|HUAWEI TIT-AL00|5.0|150'}
# query = '{"username":"amolch001@gmail.com","password":"ferrari1234" }'
# response = requests.post(hostname+'/profiles/api/token-auth/',data=query,headers=my_headers )
# data = response.json()
# token = data['token']
# print(token)

# demoorgkey = "6013ABCCYCLESHDEMO6713"
# liveorgkey = "6013ABCCYCLESHLIVE2186"
# # WARNING:root:abc@abc.com
# # WARNING:root:I6IIF6688FSI36I883NF8TIFNF63T388e!
# # WARNING:root:F8NITF88TDDSSDNN388SISISI3FNI3INl!

# demoemail = "demo@"+demoorgkey+".com"
# liveemail = "live@"+liveorgkey+".com"
# demosecret = "HYE7HLH3H36S6HBYSHEACBE3BYE3HSS1e!"
# livesecret = "B61YC1H1E1YC731S3B1ESESSAS3CCCE1l!"




# hostname = 'http://localhost:8081'
# my_headers = {"content-type":"application/json",'User-agent':'Skor/6 Android|HUAWEI TIT-AL00|5.0|150'}
# query = '{"username": "'+ demoemail+ '","password":"' + demosecret + '" }'
# response = requests.post(hostname+'/profiles/api/token-auth/',data=query,headers=my_headers )
# data = response.json()
# token = data['token']
# print(token)



# hostname = 'http://localhost:8081'
# tokenheaders = {"content-type":"application/json",'User-agent':'Skor/6 Android|HUAWEI TIT-AL00|5.0|150'}
# query = '{"username":"amolch001@gmail.com","password":"ferrari1234" }'
# response = requests.post(hostname+'/profiles/api/token-auth/',data=query,headers=tokenheaders )
# data = response.json()
# token = data['token']
# print(token)

# livequery = '{"username": "'+liveemail +'","password":"'+ livesecret +'" }'
# response1 = requests.post(hostname+'/profiles/api/token-auth/',data=livequery,headers=tokenheaders )
# livetokendata = response1.json()
# livetoken = livetokendata['token']
# print(livetoken)
# data['live_token'] = livetoken

# token = "49b6e9ab1a61ae4cd9eb86220e784e752eaa16b5"



token = "77e93f00a6b37fddb2afbc648260d1c6c363a52d"
hostname = 'http://localhost:8081'
my_headers = {"content-type":"application/json","User-agent":"Skor/6 Android|HUAWEI TIT-AL00|5.0|150"}

key = "Authorization"
authtoken = "Token "+ token
my_headers[key] = authtoken
print(my_headers)

# Get Rewards 
response = requests.get(hostname+'/rewards/api/rewards/',headers=my_headers )
data = response.json()
print(data)


# hostname = 'http://localhost:8081'
# tokenheaders = {"content-type":"application/json",'User-agent':'Skor/6 Android|HUAWEI TIT-AL00|5.0|150'}
# authquery = '{"username": "amolch001@gmail.com","password":"ferrari1234" }'
# demoquery = '{"username": "demo@5465W2ORGANIZADEMO6279.com", "password": "626IIZ629G7AWG769R72Z6NAZGA672AAe!"}'
# response1 = requests.post(hostname+'/profiles/api/token-auth/',data=demoquery,headers=tokenheaders )
# authtokendata = response1.json()
# authtoken = authtokendata['token']
# print(authtoken)



# createcompany = '{"img_display":"main.jpg","img_thumbnail": "imgthumbnail.jpg","name" : "tata22","slug":"tata22","domain":"www.tata.com", "country":"Singapore", "timezone":"timezone","region":"12", "business_Unit":"1", "department":"finance" }'


   
# email = "abssscd@corp.com"
# password = "10gXWOqeaf!"
# organization = "tata22"
# department = "finance-198"
# first_name = "Spur"
# last_name = "Connect Test"

# createuser = {}
# createuser["email"] = email
# createuser["password"] = password
# createuser["organization"] = organization
# createuser["department"] = department
# createuser["first_name"] = first_name
# createuser["last_name"] = last_name


# createstring = json.dumps(createuser)
# print(createstring)
# response = requests.post(hostname+'/profiles/api/createorganisation/',data=createstring,headers=my_headers)
# data = response.json()
# print(data)

    #         createcompany = {}
    #         createcompany["img_display"] = "main.jpg"
    #         createcompany["img_thumbnail"] = "imgthumbnail.jpg"
    #         createcompany["name"] =  name  ,
    #         createcompany["email"] =  email  ,
    #         createcompany["demoorgkey"]=  demoorgkey ,
    #         createcompany["liveorgkey"]=  liveorgkey ,
    #         createcompany["domain"]=  demoorgkey , 
    #         createcompany["demosecret"]=  demosecret , 
    #         createcompany["livesecret"]=  livesecret , 
    #         createcompany["country"] = "Singapore", 
    #         createcompany["timezone"] = "Asia/Singapore",
    #         createcompany["region"] = "12", 
    #         createcompany["business_Unit"] = "1",
    #         createcompany["department"] = "finance"
    #         createstring = json.dumps(createcompany)
    #         logging.warning(createstring)



            # hostname = 'http://localhost:8001'
            # tokenheaders = {"content-type":"application/json",'User-agent':'Skor/6 Android|HUAWEI TIT-AL00|5.0|150'}
            # authquery = '{"username": "amolch001@gmail.com","password":"ferrari1234" }'
   
               
            # try:
            #     logging.warning(authquery) 
            #     logging.warning("token request sent") 

            #     response1 = requests.post(hostname+'/profiles/api/token-auth/',data=authquery,headers=tokenheaders )
            #     authtokendata = response1.json()
            #     authtoken = authtokendata['token']
            #     print(authtoken)
            #     data['token'] = authtoken
            #     logging.warning(authtoken) 
            #     logging.warning("token request over") 
               
            # except requests.exceptions.RequestException as e:  # This is the correct syntax
            #     logging.warning(e)
            #     return Response({"status": "error", "data": e ,"msg": "issue"}, status=status.HTTP_200_OK)






