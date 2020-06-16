import boto3
import datetime
import boto.ec2

client = boto3.client('ec2', aws_access_key_id="xxx", aws_secret_access_key="xxx", region_name='eu-west-1')

# get list of all regions

all_regions = client.describe_regions()
list_of_regions = [] # create an empty list to store all regions
for each_region in all_regions['Regions']:
    list_of_regions.append(each_region['RegionName'])


for each_region in list_of_regions:
    resource = boto3.resource('ec2', aws_access_key_id="xxx", aws_secret_access_key="xxx", region_name=each_region)
    sgs = resource.security_groups.all()
    all_sgs_ids = set([sg.id for sg in sgs])
    #print("region name : {} {} length {}".format(each_region, all_sgs_ids, len(all_sgs_ids)))
    if len(all_sgs_ids) > 0:
        print("..............................................................")
        print("region name : {} {} length {}".format(each_region, all_sgs_ids, len(all_sgs_ids)))
        for each_sg in all_sgs_ids:
            client = boto3.client('ec2', aws_access_key_id="xxx", aws_secret_access_key="xxx", region_name=each_region)
            response = client.describe_security_groups(GroupIds=[each_sg])
            for sg_rule in response['SecurityGroups'][0]['IpPermissions']:
                if 'IpRanges' in sg_rule:
                    if len(sg_rule['IpRanges']) > 0:
                        for i in sg_rule['IpRanges']:
                            if i['CidrIp'] == '0.0.0.0/0':
                                if sg_rule['FromPort'] == 80 or sg_rule['FromPort'] == 443:
                                    print("No worries ! It's a internet port {}".format(sg_rule['FromPort']))
                                    print("region name  : {} contains {} ".format(each_region, each_sg))
                                    continue
                                else:
                                    print("  {} PORT  IP V 4   is open from anywhere           ???".format(sg_rule['FromPort']))
                                    print("                     >>>> region name  : {} contains {} security from anywhere {} protocol".format(each_region, each_sg, sg_rule['IpProtocol']))
                                    revoke_response = client.revoke_security_group_ingress
                                    ec2_sg = boto3.resource('ec2', aws_access_key_id="xxx", aws_secret_access_key="xxx", region_name=each_region)
                                    security_group_var = ec2_sg.SecurityGroup(each_sg)
                                    resp = security_group_var.revoke_ingress(IpPermissions=response['SecurityGroups'][0]['IpPermissions'])

                if 'Ipv6Ranges' in sg_rule:
                    if len(sg_rule['Ipv6Ranges']) > 0:
                        for i in sg_rule['Ipv6Ranges']:
                            if i['CidrIpv6'] == '::/0':
                                print("????        I P V 6                 ???")
                                print("                     >>>> region name  : {} contains {} security from anywhere".format(each_region, each_sg))

                print("..............................................................")
                #print (sg_rule['FromPort'])