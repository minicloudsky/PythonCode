import re
import json
post_data = """
{
  "data": {
    "id": 27,
    "name": "公募基金客户存量金额获取",
    "description": "公募基金客户存量金额获取",
    "app_id": 6,
    "datasource_id": 29,
    "es_index": null,
    "es_type": null,
    "api_code": "get_v_po_fund_stock",
    "api_sql": "select \n    mid,\n    max_load_pt,\n    subsist_amt_avg\nfrom dh_aum.vr_po_fund_stock\nwhere max_load_pt >= ' {date} '",
    "active": true
  },
  "params": [
    {
      "id": 17,
      "param_key": "date",
      "description": "开始日期",
      "type": "str",
      "demo": "2019-07-01",
      "order": 0,
      "edit": false
    }
  ]
}
"""
# post_data = json.loads(post_data)
# print(post_data)
# formdata = post_data['data']
# datasource_id = formdata.pop("datasource_id")
# sql = formdata.pop("api_sql")
# params = post_data.pop("params", [])
# param_rs = re.compile("{([^\}]*)}")
sql = """select \n    mid,\n    max_load_pt,\n    subsist_amt_avg\nfrom 
dh_aum.vr_po_fund_stock\nwhere max_load_pt >= ' {date} '"""


param_rs = re.compile("{([^\{}]*)}[^}]")
params_result = param_rs.findall(sql)
print(params_result)