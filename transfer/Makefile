AWS_PROFILE := default
AWS_REGION := ap-northeast-1

PROJECT_NAME := hoge
ENV := dev

VPC_ID := vpc-xxx
VPC_CIDR := $(shell aws ec2 describe-vpcs --profile ${AWS_PROFILE} --region ${AWS_REGION} --vpc-id ${VPC_ID} | jq -r '.Vpcs[].CidrBlock')
SUBNET_IDS := \"subnet-xxx,subnet-yyy\"

SSHPUBKEY := $(shell cat ~/.ssh/id_rsa.pub)

create_server:
	aws cloudformation create-stack \
		--profile ${AWS_PROFILE} \
		--region ${AWS_REGION} \
		--stack-name ${PROJECT_NAME}-${ENV}-sftp-server \
		--template-body file://sftp-public.yml \
		--capabilities CAPABILITY_NAMED_IAM \
		--parameters \
			ParameterKey=ProjectName,ParameterValue=${PROJECT_NAME} \
			ParameterKey=Env,ParameterValue=${ENV} \
			ParameterKey=VpcId,ParameterValue=${VPC_ID} \
			ParameterKey=VpcCidr,ParameterValue=${VPC_CIDR} \
			ParameterKey=SubnetIds,ParameterValue=${SUBNET_IDS} \
	&& aws cloudformation wait stack-create-complete \
		--profile ${AWS_PROFILE} \
		--region ${AWS_REGION} \
		--stack-name ${PROJECT_NAME}-${ENV}-sftp-server \
	&& sh scripts/add-targets.sh ${AWS_PROFILE} ${AWS_REGION} ${PROJECT_NAME} ${ENV}

delete_server:
	aws cloudformation delete-stack \
		--profile ${AWS_PROFILE} \
		--region ${AWS_REGION} \
		--stack-name ${PROJECT_NAME}-${ENV}-sftp-server

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
