# init template

First template to run after creating an AWS account  

``` bash
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
# with region option(us-east-1) for log retrieval
# Manually configure logging of hostedzone
aws cloudformation create-stack \
    --region us-east-1 \
    --stack-name init-route53 \
    --template-body file://route53.yml \
    --parameters \
        ParameterKey=ProjectName,ParameterValue=<YOUR PROJECT NAME> \
        ParameterKey=DomainName,ParameterValue=<YOUR DOMAIN>

# ACM
# Manually domain authentication
aws cloudformation create-stack \
    --stack-name init-acm \
    --template-body file://acm.yml \
    --parameters \
        ParameterKey=ProjectName,ParameterValue=<YOUR PROJECT NAME> \
        ParameterKey=DomainName,ParameterValue=<YOUR DOMAIN>
```
