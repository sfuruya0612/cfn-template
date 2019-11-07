# zbx-fargate

## Launch zabbix
``` sh
aws cloudformation create-stack \
  --stack-name ph-zabbix \
  --template-body file://launch_zbx_cfn_template.yml \
  --parameters ParameterKey=ProjectName,PrameterValue= \
               ParameterKey=VpcId,PrameterValue= \
               ParameterKey=VpcCidr,PrameterValue= \
               ParameterKey=SubnetId1,PrameterValue= \
               ParameterKey=SubnetId2,PrameterValue= \
               ParameterKey=SubnetId3,PrameterValue= \
               ParameterKey=SubnetId4,PrameterValue= \
               ParameterKey=SubnetCidr1,PrameterValue= \
               ParameterKey=SubnetCidr2,PrameterValue= \
               ParameterKey=CertifiateArn,PrameterValue= \
               ParameterKey=MasterDBUser,PrameterValue= \
               ParameterKey=MasterDBPassword,PrameterValue=
```
