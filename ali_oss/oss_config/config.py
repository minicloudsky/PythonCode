import json
import os

path = "/secret_config/aliyun_oss/config.json"


json_file = open(path)
data = json.load(json_file)

ACCESS_KEY_ID = data['ACCESS_KEY_ID']
ACCESS_KEY_SECRET = data['ACCESS_KEY_SECRET']
