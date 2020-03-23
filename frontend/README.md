# frontend template

``` bash
# Create EC2 (AutoScalingGroup)
aws cloudformation create-stack \
    --stack-name frontend-ec2 \
    --template-body file://asg-ec2.yml \
    --capabilities CAPABILITY_NAMED_IAM \
    --parameters \
        ParameterKey=ProjectName,ParameterValue=<YOUR PROJECT NAME> \
        ParameterKey=Env,ParameterValue=dev \
        ParameterKey=DomainName,ParameterValue=<YOUR DOMAIN>
```
