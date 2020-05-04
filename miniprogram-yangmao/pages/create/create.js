// pages/create/create.js
Page({

  /**
   * Page initial data
   */
  data: {
    tempFilePath:'等待上传图片',
    itemName: '',
    itemDetail:'',
    itemCategory:'',
    itemPrice:''
  },
  submit: function(){
    var that = this;
    //启动上传等待中...
    wx.showToast({
      title: '正在上传...',
      icon: 'loading',
      mask: true,
      duration: 10000
    })
    wx.uploadFile({
      url: 'https://www.iisheep.com' + '/create',
      filePath: that.data.tempFilePath,
      name: 'uploadfile_ant',
      formData: {
        method: 'POST',
        'itemName': that.data.itemName,
        'itemDetail': that.data.itemDetail,
        'itemCategory':that.data.itemCategory,
        'itemPrice':that.data.itemPrice
      },
      header: {
        "Content-Type": "multipart/form-data"
      },
      success: function (res) {
        wx.hideToast();
        wx.showModal({
          title: '创建成功',
          content: '商品上传成功',
          showCancel: false,
          success: function (res) { 
            wx.navigateTo({
              url: '../index/index'
            })
          }
        })
      },
      fail: function (res) {
        wx.hideToast();
        wx.showModal({
          title: '错误提示',
          content: '上传图片失败',
          showCancel: false,
          success: function (res) { }
        })
      }
    });
  },
  bindChooicePicture: function () {
    var that = this;
  
    wx.chooseImage({
      count: 1,  //最多可以选择的图片总数
      sizeType: ['compressed'], // 可以指定是原图还是压缩图，默认二者都有
      sourceType: ['album', 'camera'], // 可以指定来源是相册还是相机，默认二者都有
      success: function (res) {
        // 返回选定照片的本地文件路径列表，tempFilePath可以作为img标签的src属性显示图片
        that.setData({
          tempFilePath:res.tempFilePaths[0]
        })
        //启动上传等待中...
        for (var i = 0; i < res.tempFilePaths.length; i++) {
          console.info(res.tempFilePaths[i])
        }
        var uploadImgCount = 0;
        
      }
    });
  },
  bindItemName:function(e){
    this.setData({
      itemName:e.detail.value
    })
  },
  bindItemDetail:function(e){
    this.setData({
      itemDetail:e.detail.value
    })
  },
  bindItemPrice:function(e){
    this.setData({
      itemPrice:e.detail.value
    })
  },
  bindItemCategory:function(e){
    this.setData({
      itemCategory:e.detail.value
    })
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

  /**
   * Called when user click on the top right corner to share
   */
  onShareAppMessage: function () {

  }
})