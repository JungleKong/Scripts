
# 生成从000000到999999的密码表

with open('passdict.txt', 'w') as f:
    for i in range(1000000):
        password = str(i).zfill(6)+'\n'
        f.write(password)

