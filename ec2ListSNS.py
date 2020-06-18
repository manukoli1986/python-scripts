import boto3


client = boto3.client('ec2', aws_access_key_id="xxxxx", aws_secret_access_key="xxxxx", region_name='ap-south-1')
client_sns = boto3.client('sns', aws_access_key_id="xxxxx", aws_secret_access_key="xxxxx", region_name='ap-south-1')

def lambda_handler(event, context):

    ec2_list = []
    response = client.describe_instances()
    for ec2 in response['Reservations']:
        for each_instance in ec2['Instances']:
            ec2_list.append(each_instance['InstanceId'])

    # print(ec2_list)
    # for numbers in range(len(ec2_list)):
    #     print("Number {} EC2 with instanceID {}".format(numbers, ec2_list))


    print("################ Lets stop all instances ###############")
    response = client.stop_instances(InstanceIds=ec2_list)
    # print(response)

    response_sns = client_sns.publish(
        TopicArn='arn:aws:sns:ap-south-1:342679289922:AutomationAlert',
        Message='All EC2 intances are stopped by python Boto3',
        Subject='All EC2 intances are stopped by python Boto3')
        print(response_sns)


# lambda_function.lambda_handler
# #filename.functionName
# #ec2List.lambda_handler