# DataTransfer template

## AWS Transfer for SFTP

### Prepare
- Edit your Makefile to fit your environment  
    + `AWS_PROFILE`  
    + `AWS_REGION`  
    + `PROJECT_NAME`  
    + `VPC_ID`  
    + `SUBNET_IDS`  
  
`SUBNET_IDS` specifies **public** subnet id  
Tokyo region(ap-northeast-1) is supported only 1a, 1c AZ  
Not supported 1d  

#### Create

```
# SFTP Server
make create_server

# SFTP User
USER=hoge make create_user
```

#### Delete
```
# SFTP Server
make delete_server

# SFTP User
USER=hoge make delete_user
```

---
