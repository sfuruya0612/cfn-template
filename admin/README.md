# admin template

``` bash
# Create Bastion
aws cloudformation create-stack \
    --stack-name admin-bastion \
    --template-body file://bastion.yml \
    --capabilities CAPABILITY_NAMED_IAM \
    --parameters \
        ParameterKey=ProjectName,ParameterValue=<YOUR PROJECT NAME> \
        ParameterKey=Env,ParameterValue=dev \
        ParameterKey=DomainName,ParameterValue=<YOUR DOMAIN NAME>

# Update Bastion
aws cloudformation deploy \
    --stack-name admin-bastion \
    --template-file bastion.yml \
    --capabilities CAPABILITY_NAMED_IAM
```
