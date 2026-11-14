import requests
import pytest

headers = {
        'Authorization': 'eyJhbGciOiJIUzUxMiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VyX25hbWUiOiJhZG1pbiIsInVzZXJfa2V5IjoiMmFhZDliMjItODY4YS00MGNhLWI1ZjctMTA0NmZlYWQ5NGZjIiwiY2xpZW50X3R5cGUiOiJFUlAifQ.Hg3lwgx6JoLFAOXWSzypRJyS6OZVOzNjpU9Xr5fXmO9bBSeIkIPQSR1Z6PJ69qHfMmi7dALGXjvawNyV7R0kWQ',
        'Content-Type': 'application/json',
        'Cookie': 'JSESSIONID=6BAF63AC98CEBFD96688554D3DE65E59'
    }


def test_add_dept():
    """
    pytest 接口自动化：新增部门
    """
    department_url = "https://dev-zhengda.nuosizhiyun.cn/miss-system/dept/add"
    payload = {
        "parentName": "总部",
        "deptCode": "D001053",
        "deptName": "测试数据10",
        "user": [
            {
                "createBy": "管理员",
                "createTime": "2026-11-12 11:32:08",
                "updateBy": None,
                "updateTime": "2026-11-12 11:39:46",
                "remark": "结算组禁用下的结算值",
                "userId": 521,
                "deptId": 79,
                "userName": "结算组禁用下的结算值",
                "nickName": "结算组禁用下的结算值",
                "email": None,
                "phonenumber": "18399999999",
                "sex": None,
                "avatar": None,
                "password": None,
                "status": "0",
                "delFlag": "0",
                "loginIp": "192.168.0.4",
                "loginDate": "2026-11-12T11:39:46.283+08:00",
                "dept": {
                    "createBy": None,
                    "createTime": None,
                    "updateBy": None,
                    "updateTime": None,
                    "remark": None,
                    "deptId": 79,
                    "parentId": None,
                    "ancestors": None,
                    "deptCode": None,
                    "deptName": "结算组禁用下的结算值",
                    "orderNum": None,
                    "leader": None,
                    "phone": None,
                    "email": None,
                    "status": None,
                    "delFlag": None,
                    "parentName": None,
                    "children": [],
                    "queryMode": None
                },
                "roles": [
                    {
                        "createBy": "管理员",
                        "createTime": "2026-11-12 11:31:05",
                        "updateBy": None,
                        "updateTime": None,
                        "remark": "结算组禁用下的结算值",
                        "roleId": 162,
                        "roleName": "结算组禁用下的结算值",
                        "roleKey": "www",
                        "roleSort": 5,
                        "dataScope": "5",
                        "status": "0",
                        "delFlag": "0",
                        "flag": False,
                        "erpMenuIds": None,
                        "laoBanTongMenuIds": None,
                        "deptIds": None,
                        "permissions": None,
                        "deviceType": 0,
                        "userId": 521,
                        "admin": False
                    }
                ],
                "roleIds": None,
                "postIds": [149],
                "storeIds": None,
                "createId": 1,
                "updateId": None,
                "idCard": None,
                "userCode": "www",
                "userType": None,
                "postNames": "结算组禁用下的结算值",
                "storeNames": "结算组禁用下的结算值",
                "first": None,
                "posPassword": None
            }
        ],
        "status": "0",
        "parentId": 1,
        "leader": "结算组禁用下的结算值"
    }

    response = requests.post(department_url, headers=headers, json=payload)
    print("响应结果：", response.text)
    
    # pytest断言，你可以根据接口实际返回修改
    assert response.status_code == 200
    # 例如：assert response.json()["code"] == 200