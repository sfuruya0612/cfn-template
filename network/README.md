```
aws cloudformation create-stack \
    --stack-name default-vpc \
    --template-body file://vpc.yml

aws cloudformation create-stack \
    --stack-name default-route53 \
    --template-body file://route53.yml \
    --parameters ParameterKey=ProjectName,ProjectValue=<YOUR PROJECT NAME>
```
