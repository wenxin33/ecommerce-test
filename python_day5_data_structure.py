#四个数据结构：list、str、dict、set

#1.list列表
#列表是有序的集合，可以随时添加和删除其中的元素。

cases = []

cases.append({"username": "admin", "age": "18"})
cases.append({"username": "", "age": "19"})
cases.append({"username": "admin", "age": ""})

print(cases)

for case in cases:
    print(case["username"], case["age"])


cases = {
    "case_id": "TC_GET_001",
    "params": {
        "username": "test001",
        "age": "18"
    },
    "expected": {
        "code": 200,
        "msg": "success"
    }

}

print(cases["case_id"])
print(cases["params"]["username"])
print(cases["expected"]["code"])


usernames = ["test001", "test002", "test003"]

unique_usernames = set(usernames)

print(unique_usernames)

seen = set()

for username in usernames:
    if username not in seen:
        print(username)
        seen.add(username)



username = "test001"

print(username.strip())  #去掉首尾空格
print(username.startswith("test"))  #判断是否以指定字符串开头
print("001" in username)

long_username = "x" * 1000
print(len(long_username))

special_username = "test@001"
print(special_username.isalnum())  #判断是否是字母或数字
print(special_username.isalpha())  #判断是否是字母
print(special_username.isdigit())  #判断是否是数字

