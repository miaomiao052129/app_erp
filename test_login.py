'''
Author: lijun.ding 18301370873@163.com
Date: 2026-11-11 17:54:39
LastEditors: lijun.ding 18301370873@163.com
LastEditTime: 2026-11-12 15:57:33
FilePath: \app_erp\test_login.py
Description: 登录测试用例
接口参数：{"username":"admin","password":"admin123","erpOrPos":"erp"}
'''
import requests
import urllib3
urllib3.disable_warnings()
import pytest


login_url = "https://dev-zhengda.nuosizhiyun.cn/miss-auth/login"


@pytest.mark.parametrize(
    "username, password, erpOrPos, expect_code, expect_msg",
    [
        ("admin", "admin123", "erp", 200, None),
        ("admin", "admin12", "erp", 500, "用户不存在/密码错误"),
        ("test", "123456", "erp", 500, "用户名或密码错误"),
        ("", "", "erp", 500, "用户/密码必须填写"),
    ]
)
def test_login_passed(username, password, erpOrPos, expect_code, expect_msg):
    login_headers = {"Content-type": "application/json"}
    login_json = {"username": username, "password": password, "erpOrPos": erpOrPos}

    req = requests.request(
        method="POST",
        url=login_url,
        json=login_json,
        headers=login_headers,
        verify=False
    )
    res = req.json()
    print(f"")
    print("==========================================================================================================")
    print(f"测试账号：{username} | 密码：{password}")
    print(f"接口返回完整数据：{res}")

    # 断言1：校验业务code
    real_code = res["code"]
    print(f"预期code：{expect_code}，实际code：{real_code}")
    assert real_code == expect_code, f"❌ code不对！预期：{expect_code}，实际：{real_code}"

    # 断言2：校验提示信息
    real_msg = res["msg"]
    print(f"预期msg：{expect_msg}，实际msg：{real_msg}")
    assert real_msg == expect_msg, f"❌ 提示文字不对！预期：{expect_msg}，实际：{real_msg}"
  