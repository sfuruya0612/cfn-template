AWS_PROFILE := default
AWS_REGION := ap-northeast-1

# Project settings
PROJECT_NAME := hoge
ENV := dev
DOMAIN_NAME := hogehoge.com

# Network
VPC_ID := vpc-xxx
PUB_CIDR := 10.xx.yy.zz/aa

# Subnets
PUB_SUBNET1 := subnet-xxx
PUB_SUBNET2 := subnet-yyy
PRI_SUBNET := \"subnet-xxx,subnet-yyy\"

# ACL settings
ALLOW_IP := 111.xx.yy.zz/32
RULE := 101

# User ssh public key
SSHPUBKEY := $(shell cat ~/.ssh/id_rsa.pub)

create_server:
	aws cloudformation create-stack \
		--profile ${AWS_PROFILE} \
		--region ${AWS_REGION} \
		--stack-name ${PROJECT_NAME}-${ENV}-sftp-server \
		--template-body file://sftp-server.yml \
		--capabilities CAPABILITY_NAMED_IAM \
		--parameters \
			ParameterKey=ProjectName,ParameterValue=${PROJECT_NAME} \
			ParameterKey=Env,ParameterValue=${ENV} \
			ParameterKey=VpcId,ParameterValue=${VPC_ID} \
			ParameterKey=PublicCidr,ParameterValue=${PUB_CIDR} \
			ParameterKey=PubSubnetId1,ParameterValue=${PUB_SUBNET1} \
			ParameterKey=PubSubnetId2,ParameterValue=${PUB_SUBNET2} \
			ParameterKey=PriSubnetIds,ParameterValue=${PRI_SUBNET} \
			ParameterKey=DomainName,ParameterValue=${DOMAIN_NAME}

set_acl:
	aws cloudformation create-stack \
		--profile ${AWS_PROFILE} \
		--region ${AWS_REGION} \
		--stack-name ${PROJECT_NAME}-${ENV}-sftp-acl \
		--template-body file://sftp-acl.yml \
		--parameters \
			ParameterKey=ProjectName,ParameterValue=${PROJECT_NAME} \
			ParameterKey=Env,ParameterValue=${ENV} \
			ParameterKey=AllowIP,ParameterValue=${ALLOW_IP} \
			ParameterKey=RuleNumber,ParameterValue=${RULE}

delete_server:
	aws cloudformation delete-stack \
		--profile ${AWS_PROFILE} \
		--region ${AWS_REGION} \
		--stack-name ${PROJECT_NAME}-${ENV}-sftp-server

delete_acl:
	aws cloudformation delete-stack \
		--profile ${AWS_PROFILE} \
		--region ${AWS_REGION} \
		--stack-name ${PROJECT_NAME}-${ENV}-sftp-acl

# 環境変数でユーザ名を指定
# pattern match: [a-zA-Z][-a-zA-Z0-9]
# e.g. USER=fuga make create_user
create_user:
	aws cloudformation create-stack \
		--profile ${AWS_PROFILE} \
		--region ${AWS_REGION} \
		--stack-name ${PROJECT_NAME}-${ENV}-sftp-user-${USER} \
		--template-body file://sftp-user.yml \
		--parameters \
			ParameterKey=ProjectName,ParameterValue=${PROJECT_NAME} \
			ParameterKey=Env,ParameterValue=${ENV} \
			ParameterKey=UserName,ParameterValue=${USER} \
			ParameterKey=SshPubKey,ParameterValue="${SSHPUBKEY}"

# 環境変数でユーザ名を指定
# pattern match: [a-zA-Z][-a-zA-Z0-9]
# e.g. USER=fuga make delete_user
delete_user:
	aws cloudformation delete-stack \
		--profile ${AWS_PROFILE} \
		--region ${AWS_REGION} \
		--stack-name ${PROJECT_NAME}-${ENV}-sftp-user-${USER}
