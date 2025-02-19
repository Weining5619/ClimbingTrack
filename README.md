# ClimbingTrack
# 攀岩训练打卡管理系统 🧗‍♂️

[![Flask](https://img.shields.io/badge/Flask-3.0.0-green)](https://flask.palletsprojects.com)
[![轻松使用](https://img.shields.io/badge/License-自由使用-green)]()

**仅供学习交流 | 个人兴趣项目 | 欢迎随意使用**

---

## 📋 训练饮食模板
👉 [点击下载训练计划模板](plan_template.csv)  
❗ 请务必保存为 **CSV格式** 后上传，字段顺序不可调整

---

## 🎯 项目初衷

- 这是一个兴趣驱动的项目，旨在帮助攀岩爱好者记录成长
- 所有代码可自由使用/修改/分享（保留署名即可）
- 本地部署的攀岩训练解决方案 | 小程序版本开发中 🚧




![网页预览](https://github.com/Weining5619/ClimbingTrack/blob/main/pic/Webpage_preview.jpg)

## 🌟 核心亮点
- 📅 智能周期训练计划（7天循环+动态调整）
- 🔄 中断恢复算法（≤3天/4-7天/＞7天三级策略）
- 🚨 Server酱微信提醒集成（定时推送+完成通知）
- 🏆 成就系统（连续打卡解锁特殊奖励）

### 🐦 中断恢复逻辑：
```bash
计划中断 → 执行3天应急训练 → 判断中断时长：
├─ ≤3天 → 延续当前周期（周几练周几）  
├─ 4-7天 → 重启当周（从周一开始）  
└─ ＞7天 → 重启上周（从周一开始、80%执行） + 筋膜唤醒  
```


## 🛠️ 技术架构

```bash
CLIMBING_TRACKER/
├── backend/              # Flask服务端
│   ├── app.py            # API核心逻辑
│   ├── climbing.db       # SQLite数据库
│   └── templates/        # 网页模板
├── frontend/             # 小程序源码（待发布）
└── plan_template.csv     # CSV训练模板
```


## 🚀 快速启动

```bash
# 克隆仓库
git clone https://github.com/yourname/climbing_tracker.git

# 安装依赖
cd backend && pip install -r requirements.txt

# 初始化数据库
flask --app app.py shell
>>> from app import db
>>> db.create_all()

# 启动服务（开发模式）
flask --app app.py run --host=0.0.0.0 --port=5000
```
访问 http://localhost:5000 开启训练之旅


## ⚠️ 当前局限性与注意事项
### 本地部署限制
  - 📦 **数据非云端：** 使用SQLite本地存储，不支持多设备同步

  - 👥 **单用户系统：** 未实现多用户账号体系

  - 📱 **移动端适配：** 网页版未优化移动端体验

  - 🔐 **安全警告：** 未启用CSRF保护（生产环境需配置）

### 功能待完善
  - 📈 **数据分析局限：** 仅基础统计，缺乏进阶可视化

  - ⏰ **提醒依赖：** 需自行配置Server酱服务

  - 🔄 **恢复假设：** 中断检测基于本地时间，时区敏感

  - 📤 **导入限制：** CSV模板需严格遵循格式规范

### 性能边界
  - ⚡ **并发限制：** SQLite不支持高并发访问

  - 🗄️ **扩展瓶颈：** 千条以上记录可能出现性能衰减

  - 📡 **网络要求：** 微信提醒需服务器具备公网IP

