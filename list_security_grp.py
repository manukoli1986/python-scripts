import boto3
import datetime

client = boto3.client('iam', aws_access_key_id="%AWS_ACCESS_KEY_ID%", aws_secret_access_key="AWS_SECRET_ACCESS_KEY ", region_name='us-east-1')

response = client.list_users()
print(type(response))

# response = client.describe_security_groups()
# print(type(response))
# print(response)


client = boto3.client('ec2', aws_access_key_id="%AWS_ACCESS_KEY_ID%", aws_secret_access_key="AWS_SECRET_ACCESS_KEY ", region_name='us-east-1')


# get a full list of the available regions
# regions_dict = client.describe_regions()
# region_list = [region['RegionName'] for region in regions_dict['Regions']]
# print(region_list)

# get a list of Security GroupIDs from EC2
# response = client.describe_instances()
# listSecurityGroup = []
# for list_item in response['Reservations']:
#     for security in list_item['Instances']:
#         for grpName in security['SecurityGroups']:
#             listSecurityGroup = grpName['GroupId']

# print(type(listSecurityGroup))
# print(listSecurityGroup)

# sG = client.delete_security_group()
# print(sG)