# zbx-fargate

## Launch zabbix
``` sh
aws cloudformation create-stack \
  --stack-name admin-zbx \
  --template-body file://ecs-fargate.yml \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameters ParameterKey=ProjectName,ParameterValue=<YOUR PROJECT NAME> \
               ParameterKey=MasterUserName,ParameterValue=admin \
               ParameterKey=MasterUserPassword,ParameterValue=Admin2020 \
               ParameterKey=DomainName,ParameterValue=<YOUR DOMAIN>
```
