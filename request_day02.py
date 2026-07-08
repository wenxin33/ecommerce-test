import requests

url = "http://127.0.0.1:8000"


response = requests.get(f"{url}/get")


print("状态码", response.status_code)
print("响应文本", response.text)
print("JSON数据", response.json())

