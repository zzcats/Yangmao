// pages/detail/detail.js
const api = require('../../utils/api.js');

Page({

  /**
   * Page initial data
   */
  data: {
    author: "hello"
  },

  /**
   * Lifecycle function--Called when page load
   */
  onLoad: function (options) {

  },

  /**
   * Lifecycle function--Called when page is initially rendered
   */
  onReady: function () {

  },

  /**
   * Lifecycle function--Called when page show
   */
  onShow: function () {

  },

  /**
   * Lifecycle function--Called when page hide
   */
  onHide: function () {

  },

  /**
   * Lifecycle function--Called when page unload
   */
  onUnload: function () {

  },

  /**
   * Page event handler function--Called when user drop down
   */
  onPullDownRefresh: function () {

  },

  /**
   * Called when page reach bottom
   */
  onReachBottom: function () {

  },
  OnsearchClick: function() {
    wx.showLoading({
      title: '加载中',
    });
    requestData.call(this);
  },
  /**
   * Called when user click on the top right corner to share
   */
  onShareAppMessage: function () {

  }
})

function requestData() {
  wx.showLoading({
    title: '加载中',
  });

  api.requestSearchItem({
  }).then((data) => {
    wx.hideLoading();
    this.setData({author:data})
  }).catch(_ => {
    this.setData({
      author:"error"
    });
    wx.hideLoading();
  });
}