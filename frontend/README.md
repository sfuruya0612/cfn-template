# frontend template

``` bash
# Create Bastion
aws cloudformation create-stack \
    --stack-name frontend-bastion \
    --template-body file://bastion.yml \
    --capabilities CAPABILITY_NAMED_IAM \
    --parameters \
        ParameterKey=ProjectName,ParameterValue=<YOUR PROJECT NAME> \
        ParameterKey=Env,ParameterValue=dev
```
