Page({
    data: {
      plan: null
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
            wx.showToast({ title: "获取计划失败", icon: "none" });
          }
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
        }
      });
    }
  });