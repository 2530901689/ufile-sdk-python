import random
import string
from ufile.compact import *
from ufile import config

config.set_default(open_ssl=True)
PUBLIC_KEY = 'TOKEN_39720417-dee0-4edb-9f8b-a1f22a863a31'  # 添加自己的账户公钥
PRIVATE_KEY = '8eca1db2-25c8-4bdd-982d-48a0a545a3e0'  # 添加自己的账户私钥
PUBLIC_BUCKET = 'youlegu-bj-test1'  # 添加公共空间名称
PRIVATE_BUCKET = 'youlegu-bj-test1'  # 添加私有空间名称


def random_string(n):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(n))


def random_bytes(n):
    return b(random_string(n))
