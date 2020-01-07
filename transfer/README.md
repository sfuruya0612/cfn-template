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
    + `VPC_ID`  
    + `PUB_SUBNET`: Specifies your VPC **public** subnet id  
    + `PRI_SUBNET`: Specifies your VPC **private** subnet id  
  
`PUB_SUBNET` and `PRI_SUBNET` are supported only 1a, 1c AZ in tokyo region(ap-northeast-1)  
Not supported 1d  

#### Create resources

``` bash
# SFTP Server
make create_server

# SFTP User
USER=hoge make create_user
```

#### Delete resources

``` bash
# SFTP Server
make delete_server

# SFTP User
USER=hoge make delete_user
```

---
