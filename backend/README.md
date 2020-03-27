# backend template

``` bash
# Create Serverless Aurora
aws cloudformation create-stack \
    --stack-name backend-rds \
    --template-body file://serverless-aurora.yml \
    --parameters \
        ParameterKey=ProjectName,ParameterValue=<YOUR PROJECT NAME> \
        ParameterKey=Env,ParameterValue=dev \
        ParameterKey=MasterUserPassword,ParameterValue=Admin2020 \
        ParameterKey=DomainName,ParameterValue=<YOUR DOMAIN>

# Create Elasticsearch
aws cloudformation create-stack \
    --stack-name backend-es \
    --template-body file://elasticsearch.yml \
    --parameters \
        ParameterKey=ProjectName,ParameterValue=<YOUR PROJECT NAME> \
        ParameterKey=Env,ParameterValue=dev \
        ParameterKey=DomainName,ParameterValue=<YOUR DOMAIN>
```
