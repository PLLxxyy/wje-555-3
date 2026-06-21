# RentHub 房产租赁管理平台

RentHub 是面向房东、租客和平台管理员的前后端分离租赁管理平台，覆盖房源发布、租约签署、账单收缴、维修工单和审计日志。

## 主要功能

- 房源管理：发布、编辑、上下架、删除，支持类型、价格、面积、户型和状态筛选。
- 租约管理：房东创建租约，双方签约后生效，支持续签、终止和到期状态流转。
- 账单中心：自动/手动账单、支付、催缴、减免、逾期标记和统计。
- 维修工单：租客报修，房东派单、标记维修中、确认完工。
- 认证授权：JWT 登录，Landlord/Tenant/Admin 三角色，前后端 RBAC 与数据范围过滤。
- 审计日志：记录租约、账单、维修等关键操作。

## 快速启动

```bash
cp .env.example .env
docker compose up --build
```

访问地址：

- 前端：http://localhost:38205
- 后端健康检查：http://localhost:38305/api/health/
- Django Admin：http://localhost:38305/admin/

演示账号：

| 角色 | 用户名 | 密码 |
|---|---|---|
| 房东 | landlord | renthub123 |
| 租客 | tenant | renthub123 |
| 管理员 | admin | renthub123 |

## 本地开发

后端默认可用 SQLite 进行本地验证；Docker Compose 使用 MySQL 8.0。

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
cd backend
python manage.py migrate
python manage.py seed_demo
python manage.py runserver 0.0.0.0:38305
```

```bash
cd frontend
npm install
npm run dev
```

## 技术栈

| 层 | 技术 |
|---|---|
| 前端 | Vue 3, TypeScript, Vite, Element Plus, Pinia, Vue Router, Axios |
| 后端 | Django, Django REST Framework, JWT |
| 数据库 | MySQL 8.0（Docker），SQLite（本地快速验证） |
| 部署 | Docker Compose, Nginx |

## 目录结构

```text
frontend/        Vue 3 + TypeScript 前端应用
backend/         Django + DRF 后端应用
backend/apps/    auth/property/lease/bill/repair/audit/common 分层模块
backend/database/init.sql  MySQL 初始化脚本
docker-compose.yml
.env.example
README.md
```

## 环境变量

| 变量 | 说明 |
|---|---|
| COMPOSE_PROJECT_NAME | Compose 项目名，默认 wjerenthub，避免中文目录名影响容器命名 |
| MYSQL_DATABASE | MySQL 数据库名 |
| MYSQL_USER / MYSQL_PASSWORD | MySQL 应用账号 |
| MYSQL_ROOT_PASSWORD | MySQL root 密码 |
| DJANGO_SECRET_KEY | Django 密钥 |
| DJANGO_DEBUG | 是否开启调试 |
| DJANGO_ALLOWED_HOSTS | Django 允许访问主机 |
| DB_ENGINE | mysql 或 sqlite |
| DB_HOST / DB_PORT / DB_NAME / DB_USER / DB_PASSWORD | 后端数据库连接配置 |
| VITE_API_BASE_URL | 前端 API 基础路径，Docker 下为 /api |

## Docker 部署说明

`docker-compose.yml` 顶层使用 `name: wjerenthub`，并为 db/backend/frontend 配置固定容器名、内部网络、MySQL 命名卷、数据库健康检查、后端健康检查和 Nginx API 反向代理。前端暴露 `38205:80`，后端暴露 `38305:38305`。

## License

MIT

