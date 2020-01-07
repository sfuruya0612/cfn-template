# -*- coding: utf-8 -*-

# import cfnresponse
import json
import boto3
import os

def lambda_handler(event):
    print("REQUEST RECEIVED:\n" + json.dumps(event))
    responseData = {}

    if event['RequestType'] == "Delete":
        # cfnresponse.send(event, context, cfnresponse.SUCCESS, {})
        return

    if event['RequestType'] == "Create":
        try:
            ec2 = boto3.client('ec2')
            elbv2 = boto3.client('elbv2')

            ids = event['ResourceProperties']['NetworkInterfaceIds']
            print("NetworkInterfaceIds:" + ','.join(ids))

            arn = os.environ['TARGETGROUP_ARN']
            print("TargetGroup arn:" + arn)

            for index, i in enumerate(ids):
                interface = ec2.describe_network_interfaces(
                    NetworkInterfaceIds=[
                        i,
                    ],
                )

                print(interface)

                ip = interface['NetworkInterfaces'][0]['PrivateIpAddress']
                print(ip)

                elbv2.register_targets(
                    TargetGroupArn=arn,
                    Targets=[
                        {
                            'Id': ip,
                            'Port': 22,
                        },
                    ]
                )

                responseData['IP' + str(index)] = ip

        except Exception as e:
            responseData = {'error': str(e)}
            print(responseData)
            # cfnresponse.send(event, context, cfnresponse.FAILED, responseData)
            return

    # cfnresponse.send(event, context, cfnresponse.SUCCESS, responseData)
    print(responseData)

def main():
    f = open("event.json", 'r')
    event = json.load(f)
    lambda_handler(event)

if __name__ == '__main__':
    main()
