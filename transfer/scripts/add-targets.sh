#! /bin/sh

AWS_PROFILE=$1
AWS_REGION=$2
PROJECT_NAME=$3
ENV=$4

tg=`aws elbv2 describe-target-groups \
        --profile ${AWS_PROFILE} \
        --region ${AWS_REGION} \
        | jq -r '.TargetGroups[] | select(.TargetGroupName == "'${PROJECT_NAME}'-'${ENV}'-sftp-tg") | .TargetGroupArn'`

ips=`aws ec2 describe-network-interfaces \
        --profile ${AWS_PROFILE} \
        --region ${AWS_REGION} \
        | jq -r '.NetworkInterfaces[] | select(.Groups[].GroupName == "'${PROJECT_NAME}'-'${ENV}'-sftp-sg") | .PrivateIpAddress'`

for i in ${ips}; do
    aws elbv2 register-targets \
        --profile ${AWS_PROFILE} \
        --region ${AWS_REGION} \
        --target-group-arn ${tg} \
        --targets Id="${i}",Port=22
done
