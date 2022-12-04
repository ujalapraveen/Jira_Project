
import requests
import json
import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user="root",
    password="Parveen123@",
    database="jiradata"
)

# if mydb.is_connected:
#     print("successful")


URL= "https://ujalaparveen.atlassian.net/rest/api/2/search#"
# print(URL)

Second_url= "https://ujalaparveen.atlassian.net/rest/api/3/issue/UP-6/transitions"
# print(Second_url)


headers={
    "Accept":"application/json",
    "Content-Type":"application/json"
}

payload=json.dumps({
    
    "transition": {
        "id": "21"
    }
})
respons1=requests.post(Second_url,headers=headers,data=payload ,auth=("ujalaparveen20@navgurukul.org","1YGAgWQh45TaEmarMUJjC51D"))

# print(respons1.text)

response=requests.get(URL,headers=headers,auth=("ujalaparveen20@navgurukul.org","1YGAgWQh45TaEmarMUJjC51D"))
# print(response)
data=response.json()
issues=data["issues"]
for k in issues:
    d=k["fields"]
    for j in d["status"]:
        pass
    name=(d["status"]["name"])
    # print(name)
    id=(d["status"]["id"])
    # print(id)
    for i in d["reporter"]:
        pass
    displayName=(d["reporter"]["displayName"]) 
    # print(displayName)
    emailAddress=(d["reporter"]["emailAddress"]) 
    # print(emailAddress)
    description=(d["description"])
    # print(description)
    updated=(d["updated"])
    # print(updated)
    

    cur=mydb.cursor()
    insert=("INSERT INTO jiraData(Number,name,Description,displayName,emailAddress,updated) VALUES(%S,%S,%s.%S,%S,%S)" )
    data=(id,name,description,displayName,emailAddress,updated)
    cur.execute(insert,data)
    mydb.commit()
    
    cur=mydb.cursor()
    insert="INSERT INTO jiraData(name,Number,Description,displayname,emailAddress,updated) VALUES(%s,%s,%s,%s,%s,%s)"
    data=(name,id,description,displayName,emailAddress,updated)
    cur.execute(insert,data)
    mydb.commit()
    
    









