# ClimbingTrack
# 攀岩训练智能管理系统 🧗‍♂️

[![Flask](https://img.shields.io/badge/Flask-3.0.0-green)](https://flask.palletsprojects.com)
[![License](https://img.shields.io/badge/License-MIT-blue)](https://opensource.org/licenses/MIT)

**本地部署的攀岩训练解决方案** | 小程序版本开发中 🚧


## 🌟 核心亮点
- 📅 智能周期训练计划（7天循环+动态调整）
- 🔄 中断恢复算法（≤3天/4-7天/＞7天三级策略）
- 🚨 Server酱微信提醒集成（定时推送+完成通知）
- 📊 本地数据可视化（训练时长/营养摄入）
- 🏆 成就系统（连续打卡解锁特殊奖励）


## 🛠️ 技术架构

CLIMBING_TRACKER/
├── backend/              # Flask服务端
│   ├── app.py            # API核心逻辑
│   ├── climbing.db       # SQLite数据库
│   └── templates/        # 网页模板
├── frontend/             # 小程序源码（待发布）
└── plan_template.csv     # CSV训练模板


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
