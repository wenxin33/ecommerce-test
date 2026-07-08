user = {
    "username": "test001",
    "password": "123456",
    "role": "normal"
    
}


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
    

def test_login_success():
    result = login("test001", "123456")
    assert result["status"] == "success"
    assert result["token"] is not None

def test_login_failure():
    result = login("test001", "wrong_password")
    assert result["status"] == "error"
    assert result["token"] is None

def test_login_empty_username():
    result = login("", "123456")
    assert result["status"] == "error"
    assert result["token"] is None