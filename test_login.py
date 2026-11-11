'''
Author: lijun.ding 18301370873@163.com
Date: 2026-11-11 17:54:39
LastEditors: lijun.ding 18301370873@163.com
LastEditTime: 2026-11-11 18:04:29
FilePath: \app_erp\test_login.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import requests

# ERP登录成功
urls="https://test-zhengda.nuosizhiyun.cn/miss-auth/login"
jsons={"username":"admin","password":"admin123","erpOrPos":"erp"}
req=requests.request("Post",url=urls,json=jsons)
print(req.status_code)
print(req.json())