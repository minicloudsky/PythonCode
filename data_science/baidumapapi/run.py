from baidumapapi.baidumap import *

if __name__ == '__main__':
    baidumap = BaiduMap(40.056878, 116.30815, 40.063597, 116.364973)
    data = baidumap.get_time()
    print(data)
    """
    正常返回数据:
    {
  "driving": [
    {
      "distance": {
        "text": "8公里",
        "value": 8042 // m
      },
      "duration": {
        "text": "5分钟",
        "value": 301 // s
      }
    }
  ],
  "riding": [
    {
      "distance": {
        "text": "7.2公里",
        "value": 7159
      },
      "duration": {
        "text": "36分钟",
        "value": 2161
      }
    }
  ],
  "walking": [
    {
      "distance": {
        "text": "7.2公里",
        "value": 7160
      },
      "duration": {
        "text": "1.7小时",
        "value": 6129
      }
    }
  ]
}
    """
