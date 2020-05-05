const api = require('../../utils/api.js');

// pages/search/search.js
Page({

  /**
   * Page initial data
   */
  data: {
    items:''
  },

  bindDetailViewTap: function() {
    wx.navigateTo({
      url: '../detail/detail'
    })
  },

  /**
   * Lifecycle function--Called when page load
   */
  onLoad: function (options) {
    wx.showLoading({
      title: '加载中',
    });
    requestData.call(this);
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

  /**
   * Called when user click on the top right corner to share
   */
  onShareAppMessage: function () {

  }
})

function requestData() {
  api.requestItems({
  }).then((data) => {
    wx.hideLoading();
    this.setData({items:data})
  }).catch(_ => {
    this.setData({
      author:"error"
    });
    wx.hideLoading();
  });
}