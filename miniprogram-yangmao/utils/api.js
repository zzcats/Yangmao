const API_BASE = 'https://www.iisheep.com';

/**
 * 网路请求
 */
function request(url, data) {
  return new Promise(function (resolve, reject) {
    wx.request({
      url: url,
      method: 'POST',
      data: data,
      header: {
        'content-type': 'text/html'
      },
      success: function (res) {
        if (res.statusCode === 200) {
          resolve(res.data);
        } else
          console.error(res);
          reject();
      },
      fail: function () {
        reject();
      }
    });
  });
}

/**
 * 搜索图书
 */
function requestSearchItem(data) {
  return request(API_BASE, data);
}

/**
 * 搜索商品
 */
function requestItems(data) {
  return request(API_BASE+'/list', data);
}

module.exports = {
  requestSearchItem: requestSearchItem,
  requestItems: requestItems
}