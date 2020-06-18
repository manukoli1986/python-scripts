
import sys, time

try:
    import boto3
except ModuleNotFoundError:
    print("Boto3 module is not installed. Please try boto3 using pip.")
    sys.exit(1)
except Exception as e:
    print(e)

#There are 2 methods to start boto3 code.
#1. With Session Object.
#2. Without Session Object.


console = boto3.session.Session(aws_access_key_id="AKIAU7SKHABBEZKFUDNY", aws_secret_access_key="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", region_name="ap-south-1")
print(console)
aws_resource_obj=console.resource(service_name="ec2")
aws_client_obj=console.client(service_name="ec2")


#####################1. With Session Object.
instance = aws_resource_obj.Instance('i-013a70797a0dc8465')
# print(dir(instance))
# print(instance.state)

instance.stop()
while True:
    instance = aws_resource_obj.Instance('i-013a70797a0dc8465')
    print(instance.state['Name'])
    if instance.state['Name']=='stopped':
        break
    time.sleep(5)
print("ec2 instance is stopped")
