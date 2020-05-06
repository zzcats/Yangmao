// pages/search/search.js
Page({

  /**
   * Page initial data
   */
  data: {
    items:'',
    currentItem:''
  },

  bindDetailViewTap: function(e) {
    var vaitem_data = e.currentTarget.dataset.id
    wx.navigateTo({
      url: '../detail/detail?name='+ vaitem_data.name
      +'&price='+vaitem_data.price
      +'&picture='+vaitem_data.picture
      +'&detail='+vaitem_data.description
      +'&link='+vaitem_data.link
      +'&datetime='+vaitem_data.datetime,
    })
  },

  /**
   * Lifecycle function--Called when page load
   */
  onLoad: function (options) {
    var that = this;
    wx.showLoading({
      title: '加载中',
    });
    wx.request({
      url: 'https://www.iisheep.com/list',
      method: 'GET',
      header: {
        'content-type': 'text/html'
      },
      success: function (res) {
        wx.hideLoading();
        that.setData({
          items:res.data
        })
      },
      fail: function (res) {
        wx.hideLoading();
        wx.showModal({
          title: '加载失败',
          content: '重新刷新',
          showCancel: false,
          success: function (res) { 
            wx.navigateTo({
              url: '../index/index'
            })
          }
        })
      }
    });
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
