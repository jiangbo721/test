# -*- coding:utf-8 -*-
# project: noju
# author: liujiangbo
# file: alioss.py
# ide: PyCharm
# time: 2019-06-18 16:37

from aliyunsdkcore import client
from aliyunsdksts.request.v20150401 import AssumeRoleRequest
import json
import oss2

endpoint = 'oss-cn-beijing.aliyuncs.com'
access_key_id = 'LTAIQHIqr8pFhb4P'
access_key_secret = 'fTLeO591R6otcuzbpZkQiIVJNegMir'
bucket_name = 'vfine-test'
# role_arn是角色的资源名称。
role_arn = 'acs:ram::1401341698611558:role/nojureadonlyoss'

clt = client.AcsClient(access_key_id, access_key_secret, 'cn-beijing')
req = AssumeRoleRequest.AssumeRoleRequest()

# 设置返回值格式为JSON。
req.set_accept_format('json')
req.set_RoleArn(role_arn)
req.set_RoleSessionName('session-name')
body = clt.do_action_with_exception(req)

# 使用RAM账号的AccessKeyId和AccessKeySecret向STS申请临时token。
token = json.loads(body)
print(token)
# 使用临时token中的认证信息初始化StsAuth实例。
auth = oss2.StsAuth(token['Credentials']['AccessKeyId'],
                    token['Credentials']['AccessKeySecret'],
                    token['Credentials']['SecurityToken'])

# 使用StsAuth实例初始化存储空间。
bucket = oss2.Bucket(auth, endpoint, bucket_name)

# 上传一个字符串。
bucket.put_object('bobo/object-name.txt', b'hello world')