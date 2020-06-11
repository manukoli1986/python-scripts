

import boto3
import datetime

client = boto3.client('iam', aws_access_key_id="xxxx", aws_secret_access_key="xxxxx", region_name='us-east-1')

response = client.list_users()
print(type(response))
# print(response['Users'])

user_list = []
for user in response['Users']:
    # print(user)
    # print("*******")
    user_list.append(user['UserName'])
# print(dir(user_list))
# print(len(user_list))

def time_diff(keycreatedtime):
    # Getting the current time in utc format
    now=datetime.datetime.now(datetime.timezone.utc)
    # Calculating diff between two datetime objects.
    diff=now-keycreatedtime
    # Returning the difference in days
    return diff.days

for each_user in user_list:
    response = client.list_access_keys(UserName=each_user)
    # print(response['AccessKeyMetadata'])
    for accessKey in response['AccessKeyMetadata']:
        # print(accessKey['CreateDate'])
        # print(dir(diff))
        # print(diff.days)
        if time_diff(accessKey['CreateDate']) > 200:
            # print("No of Days: {}".format(time_diff(accessKey['CreateDate'])))
            print("Access key: {} is {} number of days old.".format(accessKey['AccessKeyId'],time_diff(accessKey['CreateDate'])))






















# ['mayank', 'mayank1']

# [   
#     { 
#         'UserName': 'mayank',
#         'Arn': 'arn:aws:iam::342679289922:user/mayank',
#         'companyHistory': ['INS', 'tech', 'agnity']
#     },
#     {
#         'UserName': 'mayank1',
#         'Arn': 'arn:aws:iam::342679289922:user/mayank1',
#         'companyHistory': []
#     }
# ]

# list[0]['companyHistory'][1]
