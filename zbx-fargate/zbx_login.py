#! ~/.pyenv/shims/python

import json
import requests
import sys
#ログインしたいサーバの情報を引数で渡すバージョン

#check your arguments
if ( len(sys.argv) == 4 ):
    zabbix_username = sys.argv[1]
    zabbix_password = sys.argv[2]
    url = sys.argv[3]
    print(url)
    print(zabbix_password)
    print(zabbix_username)
else:
    print('check your arguments. they are not enough.')
    sys.exit()

#login
#I use " print" just for check variables. If it's unnecessary, you can delete the sentence which starts "print".
headers = {'content-type': 'application/json'}
def get_aut_key():
        payload= {'jsonrpc': '2.0','method':'user.login','params':{'user':zabbix_username,'password':zabbix_password},'auth':None,'id':'1'}
        print(payload)
        r = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)
        data = r.json()
        print(json.dumps(data, sort_keys=True, indent =4))
        auth_key = data['result']
        print(auth_key)
        return auth_key

print(get_aut_key())
