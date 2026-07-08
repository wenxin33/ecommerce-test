from api.base_client import BaseClient

client = BaseClient("http://127.0.0.1:8000")

response = client.get("/get")

print("状态码:", response.status_code)
print("响应内容:", response.json())

payload ={
    "username": "test001",
    "password": "123456"
}

response = client.post("/post", json=payload)

print("状态码:", response.status_code)
print("响应内容:", response.json())