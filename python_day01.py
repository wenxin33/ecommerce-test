user = {
    "username": "test001",
    "password": "123456",
    "role": "normal"
    
}

print("用户名:", user["username"])
print("密码:", user["password"])
print("角色:", user["role"])


def login(username, password):
    if username == user["username"] and password == user["password"]:
        return {
            "status": "success",
            "message": "登录成功",
            "token": "fake_token_001"
        }
    else:
        return {
            "status": "error",
            "message": "用户名或密码错误",
            "token": None
        }

result = login("test001", "123456")
if result["status"] == "success":
    print(result["message"])
    print("Token:", result["token"])
else:
    print("登录失败，原因是:", result["message"])



cases = [
    {"username": "test001","password": "123456","expected_status": "success"},
    {"username": "test001","password": "wrong_password","expected_status": "error"},
    {"username": "wrong_user","password": "123456", "expected_status": "error"}
]

for case in cases:
    actual_result = login(case["username"], case["password"])
    
    print("测试用户:", case["username"])
    print("测试结果:", result["status"])
    print("预期结果:", case["expected_status"])
    print("---")

    if actual_result== case["expected_status"]:
        print("测试通过")
    else:
        print("测试失败")   
    
    print("---" * 10)


