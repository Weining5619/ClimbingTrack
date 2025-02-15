# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import pandas as pd
import os
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'climbing.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 数据库模型
class Plan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), unique=True)
    day_type = db.Column(db.String(20))  # 训练日类型
    workout = db.Column(db.JSON)        # 训练内容
    meal = db.Column(db.JSON)           # 饮食计划
    completed = db.Column(db.Boolean, default=False)

# 初始化数据库
with app.app_context():
    db.create_all()

# 6周训练模板（2025新版）
# 6周训练模板（完整版）
base_plan = [
    # ============ d1 ============ 
    {
        "day_type": "🦵下肢力量+核心日",
        "workout": {
            "动作列表": [
                "跳箱训练4×8（40cm高）",
                "保加利亚分腿蹲3×10/腿（负重5kg）",
                "单腿硬拉3×10/侧（壶铃8kg）"
            ],
            "核心训练": [
                "死虫式4×30秒（腰部贴地）",
                "侧平板抬臀3×12/侧（顶峰收缩2秒）"
            ]
        },
        "meal": {
            "早餐": ["贝果夹腌黄瓜火腿", "拿铁"],
            "午餐": ["卤牛腱150g", "蒜蓉白菜", "白米饭"],
            "晚餐": ["香煎三文鱼200g", "清炒青菜"],
            "加餐": ["希腊酸奶50g", "青提10颗"]
        }
    },
    
    # ============ d2 ============ 
    {
        "day_type": "🧗攀岩技术日",
        "workout": {
            "技术训练": [
                "静态平衡训练（每条线锁定3个点各5秒）",
                "动态抓点训练（间距30cm）",
                "坠落脱敏10次（不同高度）",
                "触觉练习（闭眼摸点攀爬V0线路）"
            ]
        },
        "meal": {
            "早餐": ["三文鱼片贝果", "溏心蛋"],
            "午餐": ["红烧鸡腿（去皮）", "凉拌白菜丝"],
            "晚餐": ["虾仁150g", "蒜蓉青菜"],
            "加餐": ["卤蛋2个", "酸奶100g"]
        }
    },
    
    # ============ d3 ============ 
    {
        "day_type": "🚶有氧恢复日",
        "workout": {
            "有氧运动": ["早晨快走40分钟（配速6'30''）", "傍晚散步30分钟"],
            "恢复训练": ["泡沫轴放松大腿前侧10分钟", "靠墙倒立3组×30秒"]
        },
        "meal": {
            "早餐": ["火腿蛋三明治（白吐司）", "香蕉1根"],
            "午餐": ["牛排150g", "焯白菜帮"],
            "晚餐": ["白菜豆腐煲（肉片50g）"],
            "加餐": ["黑巧克力（85%）2小块"]
        }
    },
    
    # ============ d4 ============ 
    {
        "day_type": "💪上肢力量日",
        "workout": {
            "拉力训练": [
                "弹力带引体（宽距）5×5",
                "澳洲划船4×10"
            ],
            "推力训练": [
                "离心俯卧撑（5秒下落）4×6",
                "钻石俯卧撑3×8"
            ]
        },
        "meal": {
            "早餐": ["麦片牛奶","卤蛋"],
            "午餐": ["炒鸡肉200g", "煎蛋2个"],
            "晚餐": ["烤鸭腿（去皮）", "蚝油青菜"],
            "加餐": ["蓝莓酸奶"]
        }
    },
    
    # ============ d5 ============ 
    {
        "day_type": "🧗攀岩力量日",
        "workout": {
            "动态训练": [
                "大点动态锁定10组（保持3秒）",
                "过线挑战：连续完成3条V0+"
            ],
            "指力训练": [
                "书本抓握3×30秒（5cm厚度）",
                "门框棱角悬挂3×15秒"
            ]
        },
        "meal": {
            "早餐": ["牛油果鸡蛋三明治（白吐司）"],
            "午餐": ["牛排150g", "黄油白菜"],
            "晚餐": ["清蒸鲈鱼半条", "蒜蓉菜心"],
            "加餐": ["一块饼干"]
        }
    },
    
    # ============ d6 ============ 
    {
        "day_type": "🧘恢复日",
        "workout": {
            "主动恢复": [
                "瑜伽序列：下犬式→猫牛式→婴儿式",
                "手指冰敷护理（每次10分钟）"
            ]
        },
        "meal": {
            "早餐": ["芝士火腿欧姆蛋（3蛋）", "拿铁"],
            "午餐": ["香煎鸡腿200g", "蘑菇炒蛋"],
            "晚餐": ["虾仁炒青菜（200g虾）"],
            "加餐": ["苹果1个", "奶酪条2根"]
        }
    },
    
    # ============ d7 ============ 
    {
        "day_type": "🍳备餐日",
        "workout": {
            "备餐任务": [
                "预处理蛋白质：水煮鸡胸/卤牛肉/烤三文鱼",
                "蔬菜预处理：白菜/青菜分装冷藏"
            ]
        },
        "meal": {
            "早餐": ["贝果双拼（腌黄瓜火腿+奶油奶酪）"],
            "午餐": ["白菜鲜虾锅（昆布汤底）"],
            "晚餐": ["卤牛肉切片100g", "水煮蛋2个", "焯青菜（香油+白芝麻）"],
            "加餐": ["蜂蜜柠檬水500ml"]
        }
    }
]

def generate_dynamic_plan():
    today = datetime.now().date()
    today_str = today.strftime("%Y-%m-%d")
    
    if not Plan.query.filter_by(date=today_str).first():
        # 计算训练周期
        first_record = Plan.query.order_by(Plan.date.asc()).first()
        start_date = datetime.strptime(first_record.date, "%Y-%m-%d").date() if first_record else today
        day_num = (today - start_date).days % len(base_plan)
        
        new_plan = Plan(
            date=today_str,
            day_type=base_plan[day_num]['day_type'],
            workout=base_plan[day_num]['workout'],
            meal=base_plan[day_num]['meal']
        )
        db.session.add(new_plan)
        db.session.commit()

# 路由定义
@app.route('/')
def index():
    generate_dynamic_plan()
    today_plan = Plan.query.filter_by(date=datetime.now().strftime("%Y-%m-%d")).first()
    
    # 计算连续打卡
    streak = 0
    check_date = datetime.now().date()
    while True:
        date_str = check_date.strftime("%Y-%m-%d")
        plan = Plan.query.filter_by(date=date_str, completed=True).first()
        if plan:
            streak += 1
            check_date -= timedelta(days=1)
        else:
            break
    
    return render_template('index.html', plan=today_plan, streak=streak)

# 其他路由保持不变...

if __name__ == '__main__':
    app.run(debug=True)