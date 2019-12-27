# DataTransfer template

```
# Create Transfer for SFTP
aws cloudformation create-stack \
    --stack-name transfer-sftp \
    --template-body file://sftp-public.yml \
    --capabilities CAPABILITY_NAMED_IAM \
    --parameters \
        ParameterKey=ProjectName,ParameterValue=<YOUR PROJECT NAME> \
        ParameterKey=VpcId,ParameterValue=<VPC ID> \
        ParameterKey=SubnetIds,ParameterValue=<SUBNET IDS(e.g. \"sg-xxx,sg-yyy,sg-zzz\")>

# Create Transfer for SFTP User
aws cloudformation create-stack \
    --stack-name transfer-sftp-user \
    --template-body file://sftp-user.yml \
    --parameters \
        ParameterKey=ProjectName,ParameterValue=<YOUR PROJECT NAME> \
        ParameterKey=UserName,ParameterValue=<USER NAME>
```
