# DataTransfer template

## AWS Transfer for SFTP

### Image
<img src="https://github.com/sfuruya0612/cfn-template/blob/master/images/transfer-sftp.png" width="320px">

### Prepare
- Edit your Makefile to fit your environment  
    + `AWS_PROFILE`  
    + `AWS_REGION`  
    + `PROJECT_NAME`  
    + `ENV`: Specifies value is *dev*, *stg* and *prd*  
    + `DOMAIN_NAME`  
    + `VPC_ID`  
    + `PUB_CIDR`: NLB is located subnet cidr  
    + `PUB_SUBNET1` and `PUB_SUBNET2`: Specifies your VPC **public** subnet id  
    + `PRI_SUBNET`: Specifies your VPC **private** subnet id(only 1a, 1c)  
    + `ALLOW_IP`  
    + `RULE`: Network acl rule number  
  
`PRI_SUBNET`  
VPC endpoint is supported only 1a, 1c AZ in tokyo region(ap-northeast-1)  
Not supported 1d  

#### Create resources

``` bash
# SFTP Server
make create_server

# Network acl
make set_acl

# SFTP User
USER=hoge make create_user
```

#### Delete resources

``` bash
# Network acl
make delete_acl

# SFTP Server
make delete_server

# SFTP User
USER=hoge make delete_user
```

### Connection test

``` bash
$ sftp -i ${SSH_KEY_PATH} -P 22 ${USER}@${SFTP_DOMAIN_NAME}
```

---
