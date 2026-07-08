from utils.yaml_reader import read_yaml


data = read_yaml("data/mock_api_cases.yaml")

print(data)

print("GET 用例：")
print(data["get_cases"])

print("POST 用例：")
print(data["post_cases"])