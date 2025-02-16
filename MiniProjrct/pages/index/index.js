// index.js
Page({
  data: {
    plan: null, // 训练计划数据
    error: ""   // 错误信息
  },
  onLoad() {
    this.getTodayPlan();
  },
  getTodayPlan() {
    wx.request({
      url: getApp().globalData.apiUrl + "/today_plan",
      method: "GET",
      success: (res) => {
        if (res.statusCode === 200) {
          this.setData({ plan: res.data });
        } else {
          this.setData({ error: "获取训练计划失败" });
        }
      },
      fail: () => {
        this.setData({ error: "服务器无法访问" });
      }
    });
  }
});

Page({
  data: {
    plan: null,
    error: ""
  },
  onLoad() {
    this.getTodayPlan();
  },
  getTodayPlan() {
    wx.request({
      url: getApp().globalData.apiUrl + "/today_plan",
      method: "GET",
      success: (res) => {
        if (res.statusCode === 200) {
          this.setData({ plan: res.data });
        } else {
          this.setData({ error: "获取训练计划失败" });
        }
      },
      fail: () => {
        this.setData({ error: "服务器无法访问" });
      }
    });
  },
  completePlan() {
    wx.request({
      url: getApp().globalData.apiUrl + "/complete",
      method: "POST",
      success: (res) => {
        if (res.statusCode === 200) {
          wx.showToast({ title: "打卡成功", icon: "success" });
          this.getTodayPlan();  // 重新获取最新计划状态
        } else {
          wx.showToast({ title: "打卡失败", icon: "none" });
        }
      },
      fail: () => {
        wx.showToast({ title: "服务器错误", icon: "none" });
      }
    });
  }
});