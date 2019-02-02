# -*- coding: utf-8 -*-
import hashlib

# 摘要算法, 散列算法
MD5 = hashlib.md5()
MD5.update("how to use md5 in hashlib".encode("utf-8"))
print(MD5.hexdigest())  # md5 生成 32 为 16 进制数, 常常用于密码加密

# 测试
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}


def login(user, password):
    MD5.update(password.encode('utf-8'))
    md5_password = MD5.hexdigest()
    if md5_password == db[user]:
        return True
    else:
        return False


assert login('michael', '1234567')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')
