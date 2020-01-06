# init template

First template to run after creating an AWS account  

```
# Create Buckets
aws cloudformation create-stack \
    --stack-name init-buckets \
    --template-body file://s3.yml \
    --parameters \
        ParameterKey=ProjectName,ParameterValue=<YOUR PROJECT NAME> \
        ParameterKey=Env,ParameterValue=<Environment>


# Create VPC
aws cloudformation create-stack \
    --stack-name init-vpc \
    --template-body file://vpc.yml \
    --parameters \
        ParameterKey=ProjectName,ParameterValue=<YOUR PROJECT NAME> \
        ParameterKey=Env,ParameterValue=<Environment> \
        ParameterKey=Segment,ParameterValue=<Network segment> \
        ParameterKey=Logging,ParameterValue=<true or false>

# Create Route53
aws cloudformation create-stack \
    --stack-name init-route53 \
    --template-body file://route53.yml \
    --parameters \
        ParameterKey=ProjectName,ParameterValue=<YOUR PROJECT NAME>
```
