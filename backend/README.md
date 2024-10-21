# IT-project-Team92

## 技术栈：
+ Python 3.12
+ FastAPI：用于构建高性能的Web API。
+ Tortoise ORM：用于与数据库进行交互。
+ Pydantic：用于数据验证和序列化。
+ JWT：用于用户认证和授权。
+ Docker：用于容器化应用，方便部署和开发。
## 项目结构
``` plaintext
.
├── app
│   ├── api                    # 路由和视图
│   │   ├── admin.py           # 管理员相关路由
│   │   ├── auth.py            # 用户认证相关路由
│   │   ├── __init__.py        # 路由初始化
│   ├── config.py              # 配置文件，管理环境变量
│   ├── db
│   │   ├── init_db.py         # 数据库初始化
│   ├── main.py                # 应用的入口文件
│   ├── models                 # 数据库模型定义
│   │   ├── company.py         # 公司模型
│   │   ├── __init__.py        # 模型初始化
│   │   ├── risk.py            # 风险评估相关模型
│   │   └── user.py            # 用户模型
│   ├── schemas                # Pydantic 模型，用于数据验证
│   │   ├── __init__.py
│   │   └── user.py            # 用户相关的 Pydantic 模型
│   └── utils                  # 实用工具和辅助函数
│       ├── security.py        # 安全相关函数（如密码哈希）
│       └── token.py           # JWT 令牌相关函数
├── docker-compose.yml         # Docker Compose 配置文件
├── Dockerfile                 # Docker 镜像构建文件
├── requirements.txt           # Python 依赖包列表
└── tests                      # 测试用例
    ├── conftest.py
    ├── __init__.py
    └── test_user.py           # 用户相关的测试
```
## 安装与运行
### 先决条件
- Docker
- Docker Compose

### 克隆项目
```bash
git clone https://github.com/RoyX0423/IT-project-Team92.git
cd IT-project-Team92/backend
```

### 使用 Docker 运行

1. 构建并启动服务
```bash
docker compose up --build -d #启动并构建docker中的所有服务，并且在后台运行
```
如需实时调试后端服务，则单独运行docker中的后端服务
```bash
docker compose up web #启动docker服务中的web服务，并且在前台运行
```

2. 数据库管理服务将在 http://localhost:8000 运行，无需额外安装数据库管理软件
3. Swagger UI 将在 http://localhost:8001/docs 提供 API 文档。

## 功能概览
### 用户管理
- [x] 用户注册：POST /users/register
- [x] 用户登录：POST /users/login
- [x] 获取当前用户信息：GET /users/me
- [x] 修改密码：PUT /users/password
### 管理员功能
- [x] 管理员面板：GET /admin/admin-dashboard
- [x] 查看所有用户：GET /admin/users
### 风险评估
- [ ] 创建和管理公司信息
- [ ] 为公司创建风险评估
- [ ] 管理风险类别和子类别

### 2024年9月11日 工作内容记录

#### 1. **ASIC查询系统功能开发**

完成了一个基于DrissionPage的ASIC（Australian Securities and Investments Commission）查询系统功能的封装。系统使用ChromiumPage浏览器模拟器实现对ASIC网站的自动化操作，具体工作内容如下：
- 实现了对ASIC搜索页面的自动访问，主要通过打开ASIC的搜索入口页面，并选择“Organisation & Business Names”选项。
- 在搜索框中输入目标公司名称，点击搜索按钮后，解析并提取搜索结果表格中的数据。筛选表格中显示的行，并从每行中提取各列数据。
- 完成代码封装为 `ASICSearcher` 类，提供两个主要方法：
  - `search_asic(query)`：负责传入查询关键字并执行搜索，返回与公司名称匹配的搜索结果。
  - `close()`：用于在完成搜索后关闭浏览器实例，释放资源。
- 最后，测试了使用`BHP`作为搜索关键字，验证程序功能正确，结果成功提取出与公司相关的ASIC登记数据。

#### 2. **Google Custom Search API封装开发**

完成了一个通过Google Custom Search API执行公司风险类型检查的封装，详细内容包括：
- 开发了 `RiskChecker` 类，用于根据不同风险类型组合对公司进行谷歌搜索。主要风险类型包括丑闻（scandal）、争议（controversy）、贿赂（bribery）、腐败（corruption）、诉讼（lawsuit）等。
- `google_search(query)`：通过Google API执行查询，返回每个查询结果的标题、链接和摘要，以便后续处理。
- `check_company_risks(company_name)`：对输入的公司名称执行多种风险类型的查询，返回包含每种风险类型的搜索结果字典，字典的键为风险类型，值为对应搜索结果的列表。
- 测试了BHP公司的风险检查，确认每种风险类型都返回了相关的谷歌搜索结果。

#### 3. **澳大利亚公司信息查询系统开发**

基于 ROR API 实现了一个澳大利亚公司信息的查询系统。通过输入公司名称或关键字，系统能自动筛选出与澳大利亚相关的公司，具体工作内容包括：
- 实现了从 ROR API 获取公司信息并筛选公司地理位置为“澳大利亚”的公司数据。
- 将数据整理为Pandas DataFrame结构，包含公司名称、公司ID、成立日期、公司网站链接、公司所在国家和城市等信息，以及公司与其他组织的关系信息。
- `AustralianCompanySearcher` 类提供了 `get_australian_companies(query)` 方法，输入查询关键字后自动获取并返回符合条件的公司数据，测试通过。
- 使用 `BHP` 作为查询关键字进行测试，成功提取到与BHP相关的澳大利亚公司信息。

#### 4. **尽职调查信息系统分析与整合**

分析了尽职调查过程中需要检查的风险类型、信息源以及查询渠道，整合了这些需求到已开发的查询系统中。具体内容包括：
- 将尽职调查中涉及的多种风险类型与各类查询工具（如Google搜索、ASIC查询、ROR API）进行匹配和自动化处理。
- 根据尽职调查的实际需求，使用Google Custom Search API、ASIC注册查询以及其他数据源，构建一个自动化的公司背景检查系统，涵盖公司背景验证、声誉风险、商业信息、法律风险等多方面信息。

#### 5. **系统测试与优化**

对上述开发的几个系统进行了集成测试和优化：
- 对Google Custom Search API查询系统进行多次测试，确保不同风险类型的查询能够返回符合预期的结果，特别是在多种不同公司名称的输入下（如BHP、Rio Tinto等）。
- 对ASIC查询系统进行了多次测试，确保系统能够稳定地访问ASIC网站并正确提取搜索结果。
- 对公司信息查询系统进行了API响应时间的优化，确保在大规模数据查询时能保持较高的性能。

#### 6. **工作总结与后续计划**
- 已完成的任务为尽职调查系统的核心功能，包括基于ASIC、Google Custom Search API和ROR API的公司信息查询与风险检查功能。
- 下一步计划是进一步优化查询结果的整合，确保各类风险信息能够在最终报告中自动生成，并根据不同的风险权重进行筛选和排序。
