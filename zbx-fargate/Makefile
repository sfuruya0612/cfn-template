PROFILE := default
REGION := ap-northeast-1

PJ_NAME := ph

create:
	aws cloudformation create-stack \
		--stack-name ${PJ_NAME}-zabbix \
		--template-body file://launch_zbx_template.yml \
		--parameters ParameterKey=ProjectName,PrameterValue= ${PJ_NAME} \
				ParameterKey=VpcId,PrameterValue= \
				ParameterKey=VpcCidr,PrameterValue= \
				ParameterKey=SubnetId1,PrameterValue= \
				ParameterKey=SubnetId2,PrameterValue= \
				ParameterKey=SubnetId3,PrameterValue= \
				ParameterKey=SubnetId4,PrameterValue= \
				ParameterKey=SubnetCidr1,PrameterValue= \
				ParameterKey=SubnetCidr2,PrameterValue= \
				ParameterKey=CertifiateArn,PrameterValue= \
		--profile ${PROFILE} \
		--region ${REGION}

delete:
	aws cloudformation delete-stack \
		--stack-name ${PJ_NAME}-zabbix \
		--profile ${PROFILE} \
		--region ${REGION}

