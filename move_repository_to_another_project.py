import urllib.request,json,requests

#login to bitbucket
repoNameList = []
URL = 'https://your.org:7990/bitbucket/rest/api/1.0/projects/<source_project_key_name>/repos?limit=300'
r = requests.get(URL,auth=('user', 'pass'))
nam = r.json()
fil_list = nam['values']
for x in fil_list:
    newLists = x['slug']
    repoNameList.append(newLists)
print(repoNameList)
    
# Move to another project
for names in repoNameList:
    URL1 = 'https://your.org:7990/bitbucket/rest/api/1.0/projects/<source_project_key_name>/repos/{}'
    headers = {'Content-type':'application/json', 'Accept':'application/json'}
    payload = "{\"project\": {\"key\": \"ac\"} }"
    response = requests.put(URL1.format(names), data=payload, auth=('user', 'password'), headers=headers)
    # print(response.status_code)
    if response.status_code != 201:
        print("!!!!!! Got ERROR for {} repository. PLease have a look whether repository was already present or not in project.!!!!!!!!!".format(names))
    else:
        print("Successfully moved {} repository to project".format(names))
    
