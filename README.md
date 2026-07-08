# Ecommerce API Automation Test

## 1. 项目简介

本项目是一个基于 Python、Pytest、Requests 和 Flask Mock Server 搭建的电商接口自动化测试项目。

项目模拟了电商系统中的核心业务接口，包括登录、商品查询、购物车和订单模块，并围绕这些接口设计自动化测试用例，覆盖正常场景、参数完整性、边界值、类型错误、鉴权校验、业务规则校验和异常输入等测试维度。

项目支持 YAML 数据驱动、BaseClient 请求封装、Pytest fixture 鉴权复用、测试数据清理、日志记录、HTML 测试报告生成，以及 GitHub Actions CI 自动化执行。

---

## 2. 技术栈

- Python 3.10
- Pytest
- Requests
- Flask
- PyYAML
- pytest-html
- GitHub Actions

---

## 3. 项目结构

```text
ecommerce-api-test/
│
├── api/
│   ├── __init__.py
│   ├── base_client.py          # 请求封装层
│   ├── login_api.py            # 登录接口预留封装
│   ├── product_api.py          # 商品接口预留封装
│   ├── cart_api.py             # 购物车接口预留封装
│   └── order_api.py            # 订单接口预留封装
│
├── data/
│   ├── login_cases.yaml        # 登录接口测试数据
│   ├── product_cases.yaml      # 商品接口测试数据
│   ├── cart_cases.yaml         # 购物车接口测试数据
│   └── order_cases.yaml        # 订单接口测试数据
│
├── testcases/
│   ├── test_login.py           # 登录接口测试用例
│   ├── test_product.py         # 商品接口测试用例
│   ├── test_cart.py            # 购物车接口测试用例
│   └── test_order.py           # 订单接口测试用例
│
├── utils/
│   ├── __init__.py
│   ├── yaml_reader.py          # YAML 读取工具
│   └── logger.py               # 日志工具
│
├── .github/
│   └── workflows/
│       └── api_test.yml        # GitHub Actions CI 配置
│
├── mock_api_server.py          # Flask Mock API 服务
├── conftest.py                 # Pytest fixture 配置
├── pytest.ini                  # Pytest 配置文件
├── requirements.txt            # 项目依赖
├── README.md                   # 项目说明
└── .gitignore
```

---

## 4. Mock API 接口说明

本项目使用 Flask 搭建本地 Mock API 服务，模拟电商系统中的核心接口。

### 4.1 登录接口

| 接口 | 方法 | 说明 |
|---|---|---|
| `/login` | POST | 用户登录，成功后返回 token |

成功请求示例：

```json
{
  "username": "test001",
  "password": "123456"
}
```

成功返回示例：

```json
{
  "code": 200,
  "message": "success",
  "token": "token_abc123"
}
```

失败返回示例：

```json
{
  "code": 401,
  "message": "Invalid credentials"
}
```

---

### 4.2 商品接口

| 接口 | 方法 | 说明 |
|---|---|---|
| `/products` | GET | 查询商品列表 |
| `/products/<product_id>` | GET | 查询商品详情 |

商品列表返回示例：

```json
{
  "code": 200,
  "message": "success",
  "data": [
    {
      "id": 1,
      "name": "iPhone 15",
      "price": 5999,
      "stock": 10
    }
  ]
}
```

商品不存在返回示例：

```json
{
  "code": 404,
  "message": "Product not found"
}
```

---

### 4.3 购物车接口

| 接口 | 方法 | 说明 |
|---|---|---|
| `/cart` | POST | 添加商品到购物车，需要 token |
| `/cart` | GET | 查询购物车，需要 token |

请求头示例：

```text
Authorization: Bearer token_abc123
```

添加购物车请求示例：

```json
{
  "product_id": 1,
  "quantity": 2
}
```

成功返回示例：

```json
{
  "code": 200,
  "message": "Add to cart success",
  "data": [
    {
      "product_id": 1,
      "quantity": 2
    }
  ]
}
```

未登录返回示例：

```json
{
  "code": 401,
  "message": "Unauthorized"
}
```

---

### 4.4 订单接口

| 接口 | 方法 | 说明 |
|---|---|---|
| `/order` | POST | 创建订单，需要 token，且购物车不能为空 |
| `/order/<order_id>` | GET | 查询订单详情，需要 token |

创建订单成功返回示例：

```json
{
  "code": 200,
  "message": "Create order success",
  "data": {
    "order_id": 1,
    "items": [
      {
        "product_id": 1,
        "quantity": 1
      }
    ],
    "status": "created"
  }
}
```

购物车为空返回示例：

```json
{
  "code": 400,
  "message": "Cart is empty"
}
```

订单不存在返回示例：

```json
{
  "code": 404,
  "message": "Order not found"
}
```

---

### 4.5 数据清理接口

| 接口 | 方法 | 说明 |
|---|---|---|
| `/reset` | POST | 清理购物车和订单数据，避免测试用例之间互相影响 |

返回示例：

```json
{
  "code": 200,
  "message": "reset success"
}
```

---

## 5. 测试范围

本项目当前覆盖 4 个业务模块，共 39 条核心接口自动化测试用例。

| 模块 | 接口 | 用例数量 | 覆盖点 |
|---|---|---:|---|
| 登录模块 | `/login` | 12 | 正常登录、错误密码、空值、缺失字段、超长输入、SQL 注入、XSS |
| 商品模块 | `/products` | 8 | 商品列表、商品详情、商品不存在、非法商品 ID |
| 购物车模块 | `/cart` | 11 | token 鉴权、添加商品、缺失参数、数量边界、库存校验 |
| 订单模块 | `/order` | 8 | 创建订单、查询订单、未登录访问、购物车为空、订单不存在 |

---

## 6. 测试用例设计方法

本项目测试用例主要基于以下方法设计。

### 6.1 等价类划分

将输入数据划分为有效等价类和无效等价类，例如：

- 正确用户名和密码
- 错误密码
- 空用户名
- 缺失字段
- 非法商品 ID
- 非法购买数量

### 6.2 边界值分析

针对接口参数的边界情况进行测试，例如：

- 商品数量为 0
- 商品数量为负数
- 商品数量超过库存
- 用户名超长
- 密码长度不足

### 6.3 异常输入测试

覆盖接口中常见异常输入，例如：

- 空值
- 缺失参数
- 类型错误
- 特殊字符
- SQL 注入输入
- XSS 脚本输入

### 6.4 鉴权测试

针对需要登录态的接口，测试：

- 正确 token
- 不带 token
- 错误 token

### 6.5 状态依赖测试

订单模块依赖登录状态和购物车状态，因此通过 fixture 和前置数据准备实现：

- 登录后添加购物车
- 购物车有商品时创建订单
- 购物车为空时创建订单失败
- 创建订单后查询订单

---

## 7. 项目运行方式

### 7.1 安装依赖

```bash
pip install -r requirements.txt
```

---

### 7.2 启动 Mock API 服务

```bash
python mock_api_server.py
```

服务启动后，默认运行在：

```text
http://127.0.0.1:8000
```

---

### 7.3 执行接口自动化测试

新开一个终端，执行：

```bash
pytest testcases/test_login.py testcases/test_product.py testcases/test_cart.py testcases/test_order.py
```

或者直接执行：

```bash
pytest
```

---

### 7.4 生成 HTML 测试报告

如果 `pytest.ini` 已配置 `pytest-html`，执行 pytest 后会自动生成报告。

也可以手动执行：

```bash
pytest --html=reports/report.html --self-contained-html
```

报告路径：

```text
reports/report.html
```

---

## 8. 测试报告与日志

项目集成了 `pytest-html` 和自定义日志记录。

### 8.1 HTML 测试报告

执行测试后会生成：

```text
reports/report.html
```

### 8.2 日志文件

接口请求和响应日志会记录到：

```text
logs/test.log
```

日志中包含：

- 请求方法
- 请求 URL
- 请求参数
- 请求头
- HTTP 状态码
- 响应内容

---

## 9. GitHub Actions CI

本项目已配置 GitHub Actions，用于在代码 push 或 pull request 时自动执行接口自动化测试。

CI 流程包括：

1. 拉取仓库代码
2. 安装 Python 3.10
3. 安装项目依赖
4. 启动 Flask Mock API 服务
5. 执行 Pytest 接口自动化测试
6. 上传 HTML 测试报告和日志文件

工作流文件路径：

```text
.github/workflows/api_test.yml
```

GitHub Actions 配置后，可以在仓库的 `Actions` 页面查看自动化测试执行结果。

---

## 10. 项目亮点

- 使用 Flask 搭建 Mock API 服务，模拟电商核心业务接口
- 使用 Requests + Pytest 实现接口自动化测试
- 使用 YAML 管理测试数据，实现数据驱动测试
- 使用 BaseClient 封装请求方法，统一处理 base_url、headers、token 和 timeout
- 使用 Pytest fixture 实现 token 复用、登录态客户端和测试数据清理
- 覆盖登录、商品、购物车、订单 4 个核心业务模块
- 累计完成 39 条核心接口自动化测试用例
- 集成日志记录和 HTML 测试报告
- 配置 GitHub Actions，实现自动化测试 CI 执行

---

## 11. AI 辅助测试实践

在本项目中，结合 AI 辅助完成以下工作：

- 根据接口规则辅助拆解测试点
- 辅助生成初版测试用例
- 辅助分析 Pytest 报错和断言失败原因
- 辅助整理 README、测试文档和项目描述
- 对 AI 生成内容进行人工校验，并结合等价类划分、边界值分析和业务规则进行修正

AI 在项目中主要作为测试设计和开发提效工具，最终测试用例和断言逻辑仍基于接口规则进行人工确认。

---

## 12. 后续优化方向

后续可以继续扩展：

- 增加 Allure 测试报告
- 完善 API 分层封装，如 LoginAPI、ProductAPI、CartAPI、OrderAPI
- 增加更多异常场景和组合场景
- 增加数据库校验
- 增加环境配置管理
- 增加接口响应时间断言
- 增加并发和性能测试基础实践
- 增加更完整的测试计划和测试报告文档

---

## 13. 项目当前成果

当前项目已完成：

- 4 个业务模块接口自动化测试
- 39 条核心接口自动化测试用例
- YAML 数据驱动
- BaseClient 请求封装
- Pytest fixture 鉴权复用
- 测试数据清理
- 日志记录
- HTML 测试报告
- GitHub Actions CI 自动执行

本项目形成了一个基础但完整的接口自动化测试闭环，适合作为测试开发、自动化测试、接口测试方向的实践项目。