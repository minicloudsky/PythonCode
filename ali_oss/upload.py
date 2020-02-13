# coding=utf-8
from urllib.parse import urlencode, quote
import oss2
from oss_config.config import ACCESS_KEY_SECRET, ACCESS_KEY_ID
from itertools import islice
import codecs
import datetime

auth = oss2.Auth(ACCESS_KEY_ID, ACCESS_KEY_SECRET)
bucket_name = 'python_bucket'
# 通过指定Endpoint和存储空间名称，您可以在指定的地域创建新的存储空间。Endpoint以杭州为例，其它Region请按实际情况填写。
bucket = oss2.Bucket(auth, 'http://oss-cn-shenzhen.aliyuncs.com', bucket_name)

# 创建存储空间。
# 如果需要在创建存储空间时设置存储类型、存储空间访问权限、数据容灾类型，请参考以下代码。
# 以下以配置存储空间为标准存储类型，访问权限为私有，数据容灾类型为同城冗余存储为例。
bucketConfig = oss2.models.BucketCreateConfig(oss2.BUCKET_STORAGE_CLASS_STANDARD)
bucket.create_bucket(oss2.BUCKET_ACL_PUBLIC_READ_WRITE, bucketConfig)
result = bucket.create_bucket()
print(result)
